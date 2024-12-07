from django.contrib import admin

# Register your models here.

from db.models import customer
class customerAdmin(admin.ModelAdmin):
	list_listview = ('rname','rlastname','remail','rphone','rperson','rtable','rdate','rtime','rcomment')
admin.site.register(customer,customerAdmin)