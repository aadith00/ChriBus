# Generated by Django 5.0 on 2023-12-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_alter_bus_driver_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=20)),
                ('ticket_num', models.IntegerField()),
                ('prog', models.CharField(max_length=50)),
                ('passenger_name', models.CharField(max_length=50)),
                ('dest', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Passenger',
                'verbose_name_plural': 'Passengers',
            },
        ),
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name': 'Bus', 'verbose_name_plural': 'Buses'},
        ),
    ]