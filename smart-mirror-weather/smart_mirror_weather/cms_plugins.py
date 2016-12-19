# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SmartMirrorWeatherPluginModel


class SmartMirrorWeatherPlugin(CMSPluginBase):
    model = SmartMirrorWeatherPluginModel
    module = _('smart mirror')
    render_template = 'smart_mirror_weather/smart_mirror_weather.html'

plugin_pool.register_plugin(SmartMirrorWeatherPlugin)
