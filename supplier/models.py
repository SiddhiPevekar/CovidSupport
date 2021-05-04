from django.db import models

# Create your models here.
class Supplier(models.Model):
    s_id=models.IntegerField()
    s_agency_name=models.CharField(max_length=100)
    s_emailid=models.CharField(max_length=40)
    s_state=models.CharField(max_length=70)
    s_district=models.CharField(max_length=70)
    icu_beds=models.IntegerField()
    ventilator_beds=models.IntegerField()
    icu_ventilator_beds=models.IntegerField()
    oxygen=models.CharField(max_length=5)

    # def __str__(self):
    #     return self.s_agency_name

# ModelAdmin to show in form of table 

#Creating class
# Class ModelAdminClassName(admin.ModelAdmin):
# list_display=('fn1','fn2',...)

#registering class
#admin.site.register(ModelClassName, ModelAdminClassName)