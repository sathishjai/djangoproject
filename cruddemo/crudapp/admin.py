from django.contrib import admin
from crudapp.models import student
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list=['sno','sname','saddress']
admin.site.register(student,studentadmin)
