from django.core.management.base import BaseCommand
from django.db.models import get_models


def get_models_info():
    """ Get list of models with count of objects in it"""
    models_info = []

    for model in get_models():
        models_info.append(
            '[%s] - %d objects' % (
                model.__name__, model.objects.count())
        )
    return models_info


class Command(BaseCommand):
    help = 'Print all ContentType models and each count'

    def print_models_info(self, lines):
        """ printing lines to stdout """
        map(self.stdout.write, lines)

        lines = ['error: ' + line for line in lines]
        map(self.stderr.write, lines)

    def handle(self, *args, **options):
        models_info = get_models_info()

        self.print_models_info(models_info)
