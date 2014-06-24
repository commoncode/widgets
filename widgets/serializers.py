from cqrs.serializers import CQRSSerializer, CQRSPolymorphicSerializer
from images.serializers import ImageInstanceSerializer
from menus.serializers import LinkSerializer

from .models import Widget, WidgetAspect, WidgetTemplate


class WidgetTemplateSerializer(CQRSSerializer):
    class Meta:
        model = WidgetTemplate


class WidgetAspectSerializer(CQRSPolymorphicSerializer):
    link = LinkSerializer()

    class Meta:
        model = WidgetAspect


class WidgetSerializer(CQRSSerializer):
    image = ImageInstanceSerializer()
    template = WidgetTemplateSerializer()
    aspects = WidgetAspectSerializer(many=True)

    class Meta:
        model = Widget
