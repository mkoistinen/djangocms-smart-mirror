# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


ANALOG = 'analog'
DIGITAL = 'digital'

CLOCK_MODES = (
    (ANALOG, _('Analog'), ),
    (DIGITAL, _('Digital', ), ),
)

ALIGNMENTS = (
    ('left', _('left'), ),
    ('right', _('right'), ),
)

@python_2_unicode_compatible
class SmartMirrorClockPluginModel(CMSPlugin):
    mode = models.CharField(_('mode'), choices=CLOCK_MODES, default=0, max_length=8)
    show_seconds = models.BooleanField(_('show seconds?'), default=False)
    twenty_four_hour = models.BooleanField(_('24-hour'), default=False, help_text=_('Digital mode only'))
    alignment = models.CharField(_('Text alignment'), max_length=5, default='left', choices=ALIGNMENTS, blank=False)

    def __str__(self):
        return _('{mode} clock').format(mode=self.mode)
