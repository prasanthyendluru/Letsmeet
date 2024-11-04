from django.contrib import admin
from testapp.models import Event_model
# Register your models here.
class event_admin(admin.ModelAdmin):
    list_display = ['eventname','date','location','image','type_of_event']
admin.site.register(Event_model,event_admin)