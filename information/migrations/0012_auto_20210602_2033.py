# Generated by Django 3.2.1 on 2021-06-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0011_booking_oxygen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='icu_beds',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='icu_ventilator_beds',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='oxygen',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='s_district',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='s_state',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='ventilator_beds',
        ),
        migrations.CreateModel(
            name='Ventilator',
            fields=[
                ('s_ventilator', models.AutoField(primary_key=True, serialize=False)),
                ('v_state', models.CharField(blank=True, max_length=70, null=True)),
                ('v_district', models.CharField(blank=True, max_length=70, null=True)),
                ('ventilator_beds', models.IntegerField(blank=True, null=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Oxygen',
            fields=[
                ('s_oxygenr', models.AutoField(primary_key=True, serialize=False)),
                ('iv_state', models.CharField(blank=True, max_length=70, null=True)),
                ('iv_district', models.CharField(blank=True, max_length=70, null=True)),
                ('oxygen', models.CharField(blank=True, max_length=5, null=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='IcuVentilator',
            fields=[
                ('s_icu_ventilator', models.AutoField(primary_key=True, serialize=False)),
                ('iv_state', models.CharField(blank=True, max_length=70, null=True)),
                ('iv_district', models.CharField(blank=True, max_length=70, null=True)),
                ('icu_ventilator_beds', models.IntegerField(blank=True, null=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ICU',
            fields=[
                ('s_icu_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_state', models.CharField(blank=True, max_length=70, null=True)),
                ('i_district', models.CharField(blank=True, max_length=70, null=True)),
                ('icu_beds', models.IntegerField(blank=True, null=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.supplier')),
            ],
        ),
    ]
