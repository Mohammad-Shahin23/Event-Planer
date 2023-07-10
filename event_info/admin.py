from django.contrib import admin

# Register your models here.
from .models import Event, Weather, Flight

admin.site.register(Event)
admin.site.register( Weather)
admin.site.register(Flight)
