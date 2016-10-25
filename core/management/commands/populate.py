import random
import requests
import json
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from optparse import make_option
from core.models import Product

class Command(BaseCommand):

    def get_json(self):
        self.stdout.write('Hello world.')

        url = 'https://api.randomuser.me/?results=50'

        return requests.get(url).json()['results']

    def handle(self, **options):
        for product in self.get_json():
            Product.objects.create(
                product=product['login']['username'],
                code=random.randint(0, 1000000)
            )
