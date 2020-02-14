from django.core.management.base import BaseCommand
from app.utils import load_position_data


class Command(BaseCommand):
    breakpoint()
    help = 'Load position data'

    def handle(self, *args, **options):
        breakpoint()
        load_position_data('/users/milomia/Desktop/positions.csv')
