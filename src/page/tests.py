import unittest


from .models import Rep, Zipcodes, District

# Create your tests here.

def zip(x):
    return District.objects.filter()

class RepModelTests(unittest.TestCase):
    def test(self):
        self.assertEqual(zip(40211),40216)
