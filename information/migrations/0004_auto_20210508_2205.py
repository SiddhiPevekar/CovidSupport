# Generated by Django 3.2.1 on 2021-05-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='p_name',
            new_name='p_firstname',
        ),
        migrations.AddField(
            model_name='patient',
            name='p_lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='p_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
