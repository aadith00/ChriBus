# Generated by Django 5.0 on 2024-01-19 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_rename_dest_passenger_destination_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]
