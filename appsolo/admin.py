from django.contrib import admin

# Register your models here.
from .models import viktorina,internet,mobile_internet,television
admin.site.register(viktorina)
admin.site.register(internet)
admin.site.register(mobile_internet)
admin.site.register(television)