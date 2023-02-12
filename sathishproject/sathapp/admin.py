from django.contrib import admin
from sathapp.models import sathishjai
# Register your models here.
class sathishadmin(admin.ModelAdmin):
    list=['sno','sname','sclass','saddress']
admin.site.register(sathishjai,sathishadmin)
