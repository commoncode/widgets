from random import choice

from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from displays.factories import ContentFactory
from displays.models import Display

from ...factories import WidgetFactory


class Command(BaseCommand):
    help = 'Create Widgets'

    def handle(self, *args, **options):
        print "Creating Widgets"

        displays = Display.objects.all()
        c_type = ContentType.objects.get(app_label='widgets', model='widget')

        if not displays.exists():
            call_command('create_displays')

        for display in displays:
            content = ContentFactory(content_type=c_type, display=display,
                object_id = WidgetFactory().pk)

            print "Created Widget"
