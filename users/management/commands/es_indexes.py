from __future__ import unicode_literals

from django.core.management import BaseCommand
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from users.models import Users


class Command(BaseCommand):
    help = ''' Insert Data to Elasticsearch '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Users
        self.es = Elasticsearch()

    def handle(self, *args, **options):
        # Bulk inserts
        actions = [
            {
                "_index": "users",
                "_type": "doc",
                "_source": {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email
                }

            }
            for user in Users.objects.all()
        ]
        helpers.bulk(self.es, actions)
