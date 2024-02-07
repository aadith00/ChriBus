from django.db import models
from django.contrib.auth.models import User
import random

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

    def calculate_available_seats(self):
        return self.total_seats - self.booked_seats
    
    def generate_random_ticket(self):
        self.tickets_sold = []
        ticket_number = random.randint(10000, 99999)
        while ticket_number in self.tickets_sold:
            ticket_number = random.randint(10000, 99999)
        ticket_number_act = "TICKET- " + str(ticket_number)
        self.tickets_sold.append(ticket_number)
        return ticket_number_act

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
    ticket_number = models.CharField(max_length=50, default=None)
    journey_date = models.DateField(default=None)


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