from django.contrib.contenttypes.generic import GenericRelation
from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel
from entropy.base import (
    AttributeMixin, TextMixin, EnabledMixin, SlugMixin, TitleMixin
)
from images.models import ImageInstance


class Widget(CQRSModel, EnabledMixin, SlugMixin, TextMixin, TitleMixin):
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

    template = models.ForeignKey('WidgetTemplate')
    pictures = GenericRelation(ImageInstance)


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
    pass
    # @@@ any base fields?


class WidgetLink(WidgetAspect):

    link = models.ForeignKey('menus.Link')


# class WidgetImage(WidgetAspect, ImageMixin):
#     pass


class WidgetMailChimpSignup(WidgetAspect):
    '''
    For example, create a widget that sign's up to Mailchimp
    '''
    list_name = models.CharField(
        max_length=1024)
