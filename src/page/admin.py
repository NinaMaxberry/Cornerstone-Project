from django.contrib import admin

# Register your models here.

from page.models import KentuckyProject, Csv



admin.site.register(KentuckyProject)
admin.site.register(Csv)
