from django.test import TestCase
#from page.models import KentuckyProject

# Create your tests here.

class KentuckyProjectTestCase(TestCase):
    def setUp(self):
        KentuckyProject.objects.create(zip="00001")
        KentuckyProject.objects.create(county="Sjeij;jk")

#     def test_

# class CsvTestCase()

# conn = sqlite3.connect('KentuckyProject')
# c = conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS KentukyProject_Info (zip CHAR, District INTEGER. CongressDistrict INTEGER, First_Name TEXT, Last_Name TEXT)')
# conn.commit()