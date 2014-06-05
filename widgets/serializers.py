from cqrs.serializers import CQRSSerializer

from images.serializers import ImageInstanceSerializer

from .models import Widget, WidgetTemplate


class WidgetTemplateSerializer(CQRSSerializer):
    class Meta:
        model = WidgetTemplate
        fields = ('slug', )


class WidgetSerializer(CQRSSerializer):
    images = ImageInstanceSerializer(many=True)
    template = WidgetTemplateSerializer()

    class Meta:
        model = Widget
