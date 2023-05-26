# Generated by Django 4.2.1 on 2023-05-25 13:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('zipcode', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=500)),
                ('longitude', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField()),
                ('location_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_delivery', to='transport.location')),
                ('location_pickup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_pickup', to='transport.location')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=500, unique=True)),
                ('capacity', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='transport.location')),
            ],
        ),
    ]
