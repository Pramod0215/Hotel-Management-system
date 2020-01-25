from rest_framework import serializers
from .models import Hotel,Manager,RoomType,Room,Guest,Record

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', 'hotel_location',)


class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'manager_name','manager_phone','manager_email', )

class RoomTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id', 'name','room_rent',)


class RoomSerializers(serializers.ModelSerializer):
    room_type = RoomTypeSerializers()
    class Meta:
        model = Room
        room_type = RoomTypeSerializers()
        fields = ('id','room_number','room_type','availability','bed_number',)

class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('guest_name','guest_address','guest_phone','guest_email',)


class RecordSerializers(serializers.ModelSerializer):

    guest = GuestSerializers()
    room = RoomSerializers()
    manager = ManagerSerializers()

    class Meta:
        model = Record
        fields = ('id','guest','booking_date','checkin_date','checkout_date','room','manager','checked_in', 'cancel', )
