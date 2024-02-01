from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    num_plate = models.CharField(primary_key=True,unique=True,max_length=50)  ## Primary Key
    departure_city = models.CharField(max_length=100, default=None)
    destination_city = models.CharField(max_length=100, default=None)
    departure_date = models.DateField(default=None)
    image = models.ImageField(upload_to='bus_pics', default=None)
    total_seats = models.IntegerField()
    booked_seats = models.IntegerField()
    driver_id = models.CharField(unique=True,max_length=50)
    driver_image = models.ImageField(upload_to='driver_pics', default=None)

    created_at = models.DateTimeField(auto_now_add=True)  ## gives the time and date of the first instance this was created
    updated_at = models.DateTimeField(auto_now=True)      ## gives the time and date of the last modification made into this


    def __str__(self):
        return f"{self.departure_city} to {self.destination_city} - {self.departure_date}"

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_plate = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_num = models.CharField(max_length=10, default=None)


# class Passenger(models.Model):
#     register_number = models.CharField(max_length=20)
#     ticket_number = models.IntegerField()
#     programme = models.CharField(max_length=50)
#     passenger_name = models.CharField(max_length=50)
#     destination = models.CharField(max_length=50)


#     def __str__(self):
#         return self.register_number

#     class Meta:
#         verbose_name = 'Passenger'
#         verbose_name_plural = 'Passengers'