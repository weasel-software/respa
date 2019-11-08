from rest_framework import serializers, viewsets
from django.contrib.auth.models import AnonymousUser
import django_filters
from munigeo import api as munigeo_api
from resources.api.base import NullableDateTimeField, TranslatedModelSerializer, register_view, DRFFilterBooleanWidget
from resources.models import Unit
from resources.models.resource import Resource
from .accessibility import UnitAccessibilitySerializer
from .base import ExtraDataMixin


class UnitFilterSet(django_filters.FilterSet):
    resource_group = django_filters.Filter(field_name='resources__groups__identifier', lookup_expr='in',
                                           widget=django_filters.widgets.CSVWidget, distinct=True)
    unit_has_resource = django_filters.BooleanFilter(method='filter_unit_has_resource', widget=DRFFilterBooleanWidget)

    def filter_unit_has_resource(self, queryset, name, value):
        return queryset.exclude(resources__isnull=value)

    class Meta:
        model = Unit
        fields = ('resource_group',)


class UnitSerializer(ExtraDataMixin, TranslatedModelSerializer, munigeo_api.GeoModelSerializer):
    opening_hours_today = serializers.DictField(
        source='get_opening_hours',
        child=serializers.ListField(
            child=serializers.DictField(
                child=NullableDateTimeField())
        )
    )
    # depracated, available for backwards compatibility
    reservable_days_in_advance      = serializers.ReadOnlyField(source='reservable_max_days_in_advance')
    reservable_max_days_in_advance  = serializers.ReadOnlyField()
    reservable_before               = serializers.SerializerMethodField()
    reservable_min_days_in_advance  = serializers.ReadOnlyField()
    reservable_after                = serializers.SerializerMethodField()
    hidden                          = serializers.SerializerMethodField()

    def get_extra_fields(self, includes, context):
        """ Define extra fields that can be included via query parameters. Method from ExtraDataMixin."""
        extra_fields = {}
        if 'accessibility_summaries' in includes:
            # TODO: think about populating "unknown" results here if no data is available
            extra_fields['accessibility_summaries'] = UnitAccessibilitySerializer(
                many=True, read_only=True, context=context)
        return extra_fields

    def get_reservable_before(self, obj):
        request = self.context.get('request')
        user = request.user if request else None

        if user and obj.is_admin(user):
            return None
        else:
            return obj.get_reservable_before()

    def get_reservable_after(self, obj):
        request = self.context.get('request')
        user = request.user if request else None

        if user and obj.is_admin(user):
            return None
        else:
            return obj.get_reservable_after()

    def get_hidden(self, obj):
        request = self.context.get('request')
        user = request.user
        if not isinstance(user, AnonymousUser):
            if (user.is_staff and user.has_perm('unit:can_view_unit', obj)) or user.is_general_admin or user.is_superuser:
                return False
        x = True
        for ob in Resource.objects.filter(unit=obj).all():
            if ob.public:
                x = False
        return x

    class Meta:
        model = Unit
        fields = '__all__'


class UnitViewSet(munigeo_api.GeoModelAPIView, viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = UnitFilterSet


register_view(UnitViewSet, 'unit')
