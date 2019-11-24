from django.contrib import admin

# Register your models here.

from .models import zip
from .models import rep
from .models import district


admin.site.register(zip)
admin.site.register(rep)
admin.site.register(district)