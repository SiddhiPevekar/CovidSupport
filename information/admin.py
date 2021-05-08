from django.contrib import admin

from .models import Supplier,Patient

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Patient)