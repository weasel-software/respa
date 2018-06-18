from django import forms
from django.forms import inlineformset_factory

from resources.models import (
    Day,
    Equipment,
    Period,
    Purpose,
    Resource,
    ResourceImage,
)


class ResourceForm(forms.ModelForm):
    purposes = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Purpose.objects.all(),
        required=True,
    )

    equipment = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Equipment.objects.all(),
    )

    class Meta:
        model = Resource
        fields = [
            'unit',
            'type',
            'name',
            'description',
            'purposes',
            'equipment',
            'responsible_contact_info',  # These fields ought to be atomic.
            'people_capacity',
            'area',
            'min_period',
            'max_period',
            'reservable_days_in_advance',
            'max_reservations_per_user',
            'reservable',
            'reservation_info',
            'need_manual_confirmation',
            'authentication',
            'access_code_type',
            'max_price_per_hour',
            'min_price_per_hour',
            'generic_terms',
            'specific_terms',
            'reservation_confirmed_notification_extra',
        ]


class PeriodFormset(forms.BaseInlineFormSet):
    DaysFormset = inlineformset_factory(
        Period,
        Day,
        fields=['weekday', 'opens', 'closes', 'closed', ],
        can_delete=False,
        extra=0,
        max_num=7,
        validate_max=True
    )

    def _get_days_formset(self, form, extra_days):
        days_formset = inlineformset_factory(
            Period,
            Day,
            fields=['weekday', 'opens', 'closes', 'closed', ],
            can_delete=False,
            extra=extra_days,
            max_num=7,
            validate_max=True
        )

        return days_formset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            prefix='days-%s' % (
                form.prefix,
            ),
        )

    def add_fields(self, form, index):
        super(PeriodFormset, self).add_fields(form, index)
        extra_days = 0

        if form['resource'].value() == '':
            extra_days = 1

        form.days = self._get_days_formset(form, extra_days)

    def is_valid(self):
        valid_form = False

        if self.is_bound:
            for form in self.forms:
                valid_form = form.is_valid()
                if hasattr(form, 'days'):
                    valid_form = valid_form and form.days.is_valid()

        return valid_form

    def save(self, commit=True):
        saved_form = super(PeriodFormset, self).save(commit=commit)

        for form in self.forms:
            form.save(commit=commit)
            if hasattr(form, 'days'):
                form.days.save(commit=commit)

        return saved_form


def get_period_formset(request=None, extra=1, instance=None):
    period_formset_with_days = inlineformset_factory(
        Resource,
        Period,
        fk_name='resource',
        fields=['name', 'start', 'end', ],
        formset=PeriodFormset,
        can_delete=False,
        extra=extra,
    )

    if request.method == 'GET':
        return period_formset_with_days(instance=instance)
    else:
        return period_formset_with_days(request.POST, instance=instance)


def get_resource_image_formset(request, extra=1, instance=None):
    resource_image_formset = inlineformset_factory(
        Resource,
        ResourceImage,
        fields=['image', 'caption', 'type'],
        can_delete=False,
        extra=extra,
    )
    if request.method == 'GET':
        return resource_image_formset(instance=instance)
    else:
        return resource_image_formset(request.POST, request.FILES, instance=instance)