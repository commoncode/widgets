import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words
from django.template.defaultfilters import slugify

from faker import Factory


fake = Factory.create()


class WidgetTemplateFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'widgets.WidgetTemplate'

    text = factory.LazyAttribute(lambda o: str(paragraphs(3, common=False)))


class WidgetFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'widgets.Widget'

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
    template = factory.SubFactory(WidgetTemplateFactory)
