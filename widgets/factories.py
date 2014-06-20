import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words
from django.template.defaultfilters import slugify

from faker import Factory


fake = Factory.create()


class WidgetTemplateFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'widgets.WidgetTemplate'
    FACTORY_DJANGO_GET_OR_CREATE = ('slug', )

    slug = factory.LazyAttribute(lambda o: slugify(words(2, common=False)))


class WidgetFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'widgets.Widget'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', 'template')

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
    text = factory.LazyAttribute(lambda o: str(paragraphs(1, common=False)))
    template = factory.SubFactory(WidgetTemplateFactory)
