from rest_framework import serializers
from .models import Hotel,Manager,RoomType,Room,Guest,Record

class HotelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', 'hotel_location',)


class ManagerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'manager_name','manager_phone','manager_email', )

class RoomTypeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id', 'name','room_rent',)


class RoomSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id','room_number','room_type','availability','bed_number',)

class GuestSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'guest_name','guest_address','guest_phone','guest_email',)


class RecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('id','guest','booking_date','checkin_date','checkout_date','room','manager','checked_in','cancel',)


  # def is_valid(self, raise_exception=False):

