# -*- coding: utf-8 -*-
from functools import partial

from aldryn_client import forms


class Form(forms.BaseForm):

    def to_settings(self, data, settings):
        from aldryn_addons.utils import djsenv, boolean_ish
        env = partial(djsenv, settings=settings)

        settings['INSTALLED_APPS'].extend((
            'elasticsearch',
            'elasticsearch_dsl',
        ))

        settings['DEFAULT_ELASTICSEARCH_URL'] = env('DEFAULT_ELASTICSEARCH_URL')

        if env('DJANGO_MODE') == 'build':
            return settings

        settings['ALDRYN_ELASTICSEARCH_DEBUG'] = boolean_ish(
            env('ALDRYN_ELASTICSEARCH_DEBUG', False))

        if settings['ALDRYN_ELASTICSEARCH_DEBUG']:
            settings['LOGGING']['loggers']['elasticsearch.trace'] = {
                'handlers': ['console'],
                'level': 'INFO',
            }
        return settings
