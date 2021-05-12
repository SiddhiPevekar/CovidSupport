# Generated by Django 3.2.1 on 2021-05-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_supplier_s_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(blank=True, max_length=100, null=True)),
                ('p_emailid', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('p_password1', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('p_password2', models.CharField(blank=True, max_length=40, null=True, unique=True)),
            ],
        ),
    ]