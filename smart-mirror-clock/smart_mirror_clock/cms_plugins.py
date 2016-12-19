# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SmartMirrorClockPluginModel


class SmartMirrorClockPlugin(CMSPluginBase):
    model = SmartMirrorClockPluginModel
    module = _('smart mirror')

    def get_render_template(self, context, instance, placeholder):
        return 'smart_mirror_clock/{mode}.html'.format(mode=instance.mode)


plugin_pool.register_plugin(SmartMirrorClockPlugin)
