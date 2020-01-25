from rest_framework import serializers
from .models import Hotel,Manager,RoomType,Room,Guest,Record

class HotelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', )


class ManagerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'manager_name', )
class RoomTypeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id', 'name', )


class RoomSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id','room_number',)

class GuestSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'guest_name',)


class RecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('id',)
