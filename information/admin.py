from django.contrib import admin

from .models import Supplier,Patient,Booking

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Patient)
admin.site.register(Booking)