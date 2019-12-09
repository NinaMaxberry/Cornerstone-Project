from django.contrib import admin

# Register your models here.

from .models import Zipcodes
from .models import Rep
from .models import District



admin.site.register(Zipcodes)
admin.site.register(Rep)
admin.site.register(District)