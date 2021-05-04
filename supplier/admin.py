from django.contrib import admin
from .models import Supplier

# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display=('s_id', 's_agency_name', 's_state')

#use decorator instead of this
#admin.site.register(Supplier, SupplierAdmin)

#to show in table form

#a decorator is used to register ModelAdmin Classes
#@admin.register(ModelClassName)

