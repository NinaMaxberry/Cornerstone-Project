from django.db import models 




# Create your models here.

# def create_connection(KentuckyProject):
#     conn = None
#     try:
#         conn=sqlite3.connect('KentuckyProject.db')
#     except Error as e:
#         print(e)

#     return conn

# def select_all_KentuckyProject(conn):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM KentuckyProject.db")

#     rows = cur.fetchall()

class KentuckyProject(models.Model):
    Zip = models.IntegerField()
    District = models.IntegerField()
    CongressDistrict = models.TextField()
    First_Name = models.TextField()
    Last_Name = models.TextField ()

    def __str__(self):
        return f'{self.Zip} {self.District} {self.CongressDistrict} {self.First_Name} {self.Last_Name}'
    

    


