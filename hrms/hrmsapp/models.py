from django.db import models
from django.db import models
import datetime
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_location = models.CharField(max_length=100)


    def __str__(self):
        return self.hotel_name

class RoomType(models.Model):
    name = models.CharField("room_type_name", max_length=255)
    room_rent = models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.IntegerField(default=101)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    bed_number = models.IntegerField(default=2)

    def __str__(self):
        return str(self.room_number)

class Guest(models.Model):
    guest_name = models.CharField(max_length=100)
    guest_address = models.TextField()
    guest_phone = models.IntegerField()
    guest_email = models.EmailField()


    def __str__(self):
        return self.guest_name

class Manager(models.Model):
    manager_name = models.CharField(max_length=100)
    manager_phone = models.IntegerField()
    manager_email = models.EmailField()
    # # hotel_location = models.ForeignKey(Hotel,on_delete=models.CASCADE)


    def __str__(self):
        return self.manager_name

# class Booking(models.Model):
#     hotel_name = models.ForeignKey(Hotel,on_delete=models.CASCADE)
#     room1 = models.ForeignKey(Room,on_delete=models.CASCADE)
#     is_avilable = models.BooleanField(default=True)
#     cancel = models.BooleanField(default=False)
#     booking_date = models.DateTimeField()
#     checkin_date = models.DateTimeField()
#     checkout_date = models.DateTimeField()

class Record(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    checked_in = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    # total_cost = models.IntegerField()

    def __str__(self):
        return str(self.booking_date) + self.guest.guest_name + self.manager.manager_name


    def bill(self):
        day = (self.checkout_date - self.checkin_date).days
        rent = self.room.room_type.room_rent
        return day*rent