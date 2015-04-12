from django.test import TestCase

from . import models
from . import tasks


class ImportTests(TestCase):

    def setUp(self):
        models.EventType.objects.create(name="Computers/Software/Internet/Site Management/"
                                             "Content Management")

    def test_simple_import(self):
        importer = tasks.EventImporter()
        importer.import_data()

        events = models.Event.objects.all()
        self.assertEqual(events.count(), 9)