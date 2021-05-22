# Generated by Django 3.2.1 on 2021-05-21 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0009_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.patient'),
        ),
        migrations.AddField(
            model_name='booking',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.supplier'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='bed',
            field=models.CharField(choices=[('ICU', 'ICU beds'), ('Ventilator', 'Ventilator beds'), ('ICU+Ventilator', 'ICU+Ventilator beds')], max_length=40, null=True),
        ),
    ]
