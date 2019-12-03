from django.contrib import admin

# Register your models here.

from .models import zipcodes
from .models import rep
from .models import district


admin.site.register(zipcodes)
admin.site.register(rep)
admin.site.register(district)