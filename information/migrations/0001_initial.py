# Generated by Django 3.2.1 on 2021-05-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('s_id', models.AutoField(default='0', primary_key=True, serialize=False)),
                ('s_agency_name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_emailid', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('s_password', models.CharField(blank=True, default='name4587', max_length=40, null=True)),
                ('s_state', models.CharField(blank=True, max_length=70, null=True)),
                ('s_district', models.CharField(blank=True, max_length=70, null=True)),
                ('icu_beds', models.IntegerField(blank=True, null=True)),
                ('ventilator_beds', models.IntegerField(blank=True, null=True)),
                ('icu_ventilator_beds', models.IntegerField(blank=True, null=True)),
                ('oxygen', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
