from django.db import models
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_location = models.CharField(max_length=100)


    def __str__(self):
        return self.hotel_name

    def hotel(self):
        return self.hotel_name+" "+self.hotel_location

class RoomType(models.Model):
    name = models.CharField("room_type_name", max_length=255)
    room_rent = models.IntegerField()

    def __str__(self):
        return self.name

    def roomtype(self):
        return self.room_rent

class Room(models.Model):
    room_number = models.IntegerField(default=101)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)
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
    # hotel_location = models.ForeignKey(Hotel,on_delete=models.CASCADE)


    def __str__(self):
        return self.manager_name



class Record(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    checked_in = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)


    def __str__(self):
        return str(self.booking_date) + self.guest.guest_name + self.manager.manager_name


    def bill(self):
        day = 1
        rent = self.room.room_type.room_rent
        if (self.checkout_date - self.checkin_date).days == 0:
            return day*rent
        else:
            day= (self.checkout_date - self.checkin_date).days
        return day*rent

@receiver(post_save, sender=Record)
def borrowed(sender, instance, **kwargs):
    #if checked_in and if it is not cancelled then make that room not available else it is available


    if instance.cancel :
        instance.room.availability = True
    else:
        instance.room.availability = False
    instance.room.save()

