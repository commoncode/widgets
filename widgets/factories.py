from random import choice

import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words
from django.template.defaultfilters import slugify

from faker import Factory


fake = Factory.create()


class WidgetTemplateFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'widgets.WidgetTemplate'
    FACTORY_DJANGO_GET_OR_CREATE = ('slug', )

    text = factory.LazyAttribute(lambda o: str(paragraphs(3, common=False)))

    @factory.lazy_attribute
    def slug(self):
        templates = (
            'category-feature-1',
            'category-feature-2',
            'category-feature-3',
            'home-aside',
            'home-main'
        )

        return choice(templates)


class WidgetFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'widgets.Widget'
    FACTORY_DJANGO_GET_OR_CREATE = ('title', 'template')

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
    template = factory.SubFactory(WidgetTemplateFactory)
