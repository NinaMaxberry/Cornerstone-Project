from django.contrib import admin

# Register your models here.

from .models import Zipcodes
from .models import Rep
from .models import District
from .models import Reps2000
from .models import Reps2010


admin.site.register(Zipcodes)
admin.site.register(Rep)
admin.site.register(District)
admin.site.register(Reps2000)
admin.site.register(Reps2010)