# Generated by Django 5.0.1 on 2024-02-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0006_rename_seat_num_booking_ticket_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ticket_number',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
