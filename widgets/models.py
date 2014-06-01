from django.db import models

from cqrs.models import CQRSModel, CQRSPolymorphicModel
from entropy.base import (
    AttributeMixin, TextMixin, EnabledMixin, SlugMixin, TitleMixin
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

    template = models.ForeignKey('WidgetTemplate')


class WidgetTemplate(CQRSModel, AttributeMixin, TextMixin, SlugMixin):
    '''
    Create a Widget Template for rendering on the UI side.  This is a loose
    coupling that relies on the corresponding template file or snippet being
    available in the code base.

    @@@ there's a candidate task to create an independant templates app, which
    could probably be done about now.
    '''
    # slug
    # text
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
