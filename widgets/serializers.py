from cqrs.serializers import CQRSSerializer
from images.serializers import ImageInstanceSerializer

from .models import Widget, WidgetTemplate


class WidgetTemplateSerializer(CQRSSerializer):
    class Meta:
        model = WidgetTemplate
        fields = ('slug', )


class WidgetSerializer(CQRSSerializer):
    image = ImageInstanceSerializer()
    template = WidgetTemplateSerializer()

    class Meta:
        model = Widget
