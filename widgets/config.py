from django.apps import AppConfig
from django.utils.importlib import import_module


class WidgetConfig(AppConfig):
    name = 'widgets'
    verbose_name = 'Widgets'
