from django.text import TestCase


from .models import Rep, Zipcodes, District

# Create your tests here.

class ZipcodesModelTests(TestCase):
    def test_zip_creation(self):
        zip = Zipcodes.objects.create(
            zip = 40216
        )
        self.asser
