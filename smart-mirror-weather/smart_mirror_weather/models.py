# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

ALIGNMENTS = (
    ('left', _('left'), ),
    ('right', _('right'), ),
)

@python_2_unicode_compatible
class SmartMirrorWeatherPluginModel(CMSPlugin):
    zip_code = models.CharField(_('zip code (5-digit)'), max_length=5, default='20500', blank=False)
    api_key = models.CharField(_('WUnderground API key'), max_length=32, default='', blank=False)
    alignment = models.CharField(_('Text alignment'), max_length=5, default='left', choices=ALIGNMENTS, blank=False)

    def __str__(self):
        return _('Weather ({zip})').format(zip=self.zip_code)
