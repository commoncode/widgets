from cqrs.serializers import CQRSSerializer

from .models import Widget, WidgetTemplate


class WidgetTemplateSerializer(CQRSSerializer):
    class Meta:
        model = WidgetTemplate


class WidgetSerializer(CQRSSerializer):
    template = WidgetTemplateSerializer()

    class Meta:
        model = Widget
