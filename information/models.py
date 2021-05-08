from django.db import models

# Create your models here.

class Supplier(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_agency_name=models.CharField(max_length=100, null=True, blank=True)
    s_emailid=models.EmailField(('email address'), unique=True, null=True, blank=True)
    s_password=models.CharField(max_length=40, default='name4587', null=True, blank=True)
    s_state=models.CharField(max_length=70, null=True, blank=True)
    s_district=models.CharField(max_length=70, null=True, blank=True)
    icu_beds=models.IntegerField(null=True, blank=True)
    ventilator_beds=models.IntegerField(null=True, blank=True)
    icu_ventilator_beds=models.IntegerField(null=True, blank=True)
    oxygen=models.CharField(max_length=5, null=True, blank=True)

class Patient(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_username=models.CharField(max_length=100, null=True, blank=True)
    p_firstname=models.CharField(max_length=100, null=True, blank=True)
    p_lastname=models.CharField(max_length=100, null=True, blank=True)
    p_emailid=models.EmailField(('email address'), unique=True,null=True, blank=True)
    p_pass1=models.CharField(max_length=40,null=True, blank=True)
    p_pass2=models.CharField(max_length=40, null=True, blank=True)


# class Supplier(models.Model):
#     s_id=models.AutoField(primary_key=True)
#     s_agency_name=models.CharField(max_length=100)
#     s_emailid=models.EmailField(('email address'), unique=True)
#     s_password=models.CharField(max_length=40, default='name4587')
#     s_state=models.CharField(max_length=70)
#     s_district=models.CharField(max_length=70)
#     icu_beds=models.IntegerField()
#     ventilator_beds=models.IntegerField()
#     icu_ventilator_beds=models.IntegerField()
#     oxygen=models.CharField(max_length=5)


#     # def __str__(self):
#     #     return self.s_agency_name

#     empAuth_objects = models.Manager()

# ModelAdmin to show in form of table 

#Creating class
# Class ModelAdminClassName(admin.ModelAdmin):
# list_display=('fn1','fn2',...)

#registering class
#admin.site.register(ModelClassName, ModelAdminClassName)