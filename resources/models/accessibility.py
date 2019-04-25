from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from .base import AutoIdentifiedModel
from .resource import Resource


class AccessibilityViewpoint(AutoIdentifiedModel):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(verbose_name=_('Name'), max_length=200)
    # ordering is text based in the accessibility api
    order_text = models.CharField(verbose_name=_('Order'), max_length=200, default="0")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Time of creation'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('Time of modification'))

    class Meta:
        verbose_name = _('accessibility viewpoint')
        verbose_name_plural = _('accessibility viewpoints')
        ordering = ('order_text',)

    def __str__(self):
        return self.name


class ResourceAccessibility(AutoIdentifiedModel):
    """ Accessibility summary of a Resource related to a certain Accessibility
    Viewpoint. Value and ordering priority of values are not normalized so no
    additional JOINs are required for ordering Resources based on accessibility.
    """
    GREEN = 20
    UNKNOWN = 10
    RED = 0
    VALUES = (
        (GREEN, 'green'),
        (UNKNOWN, 'unknown'),
        (RED, 'red'),
    )
    viewpoint = models.ForeignKey(AccessibilityViewpoint, related_name='accessibility_summaries',
                                  verbose_name=_('Resource Accessibility'), on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, related_name='accessibility_summaries', verbose_name=_('Resource'),
                                 db_index=True, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VALUES, verbose_name=_('Accessibility level'))
    order = models.IntegerField(verbose_name=_('Resource ordering priority'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Time of creation'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('Time of modification'))

    class Meta:
        ordering = ('id',)
        unique_together = ('viewpoint', 'resource')
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')

    @classmethod
    def get_value_from_str(cls, string_value):
        known_values = {
            'green': cls.GREEN,
            'red': cls.RED,
            'unknown': cls.UNKNOWN,
        }
        return known_values.get(string_value.lower())

    def save(self, *args, **kwargs):
        """ Ordering follows the values. """
        self.order = self.value
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} / {}: {}'.format(self.resource, self.viewpoint, self.value)