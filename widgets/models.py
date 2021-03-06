from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel
from entropy.base import (
    AttributeMixin, TextMixin, EnabledMixin, SlugMixin, TitleMixin
)
from images.mixins import ImageMixin


class Widget(CQRSModel, AttributeMixin, EnabledMixin, SlugMixin, TextMixin,
             TitleMixin, ImageMixin):
    '''
    A Widget is a contained module of functionality that is displayed within a
    Display.

    We add functionality by adding WidgetAspects
    '''

    # title
    # short_title
    # text
    # slug
    # enabled
    # attr's
    # images

    template = models.ForeignKey('WidgetTemplate')


class WidgetTemplate(CQRSModel, AttributeMixin, SlugMixin):
    '''
    Create a Widget Template for rendering on the UI side.  This is a loose
    coupling that relies on the corresponding template file or snippet being
    available in the code base.

    @@@ there's a candidate task to create an independant templates app, which
    could probably be done about now.
    '''
    # slug
    # attr's
    pass


class WidgetAspect(CQRSPolymorphicModel):
    widget = models.ForeignKey('Widget', related_name='aspects')


class WidgetLink(WidgetAspect):
    link = models.ForeignKey('menus.Link')


class WidgetMailChimpSignup(WidgetAspect):
    '''
    For example, create a widget that sign's up to Mailchimp
    '''
    list_name = models.CharField(
        max_length=1024)
