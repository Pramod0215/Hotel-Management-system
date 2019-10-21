from rest_framework import serializers
from .models import Hotel,Manager,RoomType,Room,Guest,Record

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', )


# class ManagerSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Manager
#         fields = ('id', 'manager_name', )
# class RoomTypeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = RoomType
#         fields = ('id', 'name', )
#
#
# class RoomSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ('id', 'room_number',)
#
# class GuestSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Guest
#         fields = ('id', 'room_number',)


# class RecordSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Record
#         fields = ('id', 'booking_date',)
