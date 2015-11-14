from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    help = 'Print all ContentType models and each count'

    def handle(self, *args, **options):
        for model in get_models():
            self.stdout.write('%s - objects: %s' % (model.__name__, model.objects.count()))
            self.stderr.write('error: %s - objects: %s\n' % (model.__name__, model.objects.count()))
