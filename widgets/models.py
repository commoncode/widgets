from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel
from entropy.base import (
    EnabledMixin, SlugMixin, TitleMixin
)


class Widget(CQRSModel, EnabledMixin, SlugMixin, TitleMixin):
    '''
    A Widget is a contained module of functionality that is displayed within a
    Display.

    We add functionality by adding WidgetAspects
    '''

    # title
    # short_title
    # slug
    # enabled

    # @@@ provide a list of template choices or create a
    # WidgetTemplate class
    template_name = models.CharField(
        max_length=512)


class WidgetAspect(CQRSPolymorphicModel):
    pass
    # @@@ any base fields?


class WidgetLink(WidgetAspect):

    link = models.ForeignKey('menus.Link')


class WidgetMailChimpSignup(WidgetAspect):
    '''
    For example, create a widget that sign's up to Mailchimp
    '''
    list_name = models.CharField(
        max_length=1024)


