# Generated by Django 5.0.1 on 2024-02-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerName', models.CharField(max_length=255)),
                ('vehicleType', models.CharField(max_length=50)),
                ('vehicleModel', models.CharField(max_length=255)),
                ('rentalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imageUpload', models.ImageField(upload_to='upload')),
            ],
        ),
    ]
