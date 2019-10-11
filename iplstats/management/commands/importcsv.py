import os

from iplstats.models import Match, Delivery
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        basedir = os.path.abspath(os.path.dirname('matches.csv'))
        matches_csv = os.path.join(basedir, 'matches.csv')
        deliveries_csv = os.path.join(basedir, 'deliveries.csv')
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        matches_count = Match.objects.from_csv(matches_csv)
        deliveries_count = Delivery.objects.from_csv(deliveries_csv)
        print (f"inserted {matches_count} matches and {deliveries_count} deliveries")

    