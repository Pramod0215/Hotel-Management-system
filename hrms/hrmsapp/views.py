from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


class HotelView(viewsets.ModelViewSet):
    serializer_class = HotelSerializers
    queryset = Hotel.objects.all()

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializers
    queryset = Manager.objects.all()

class RoomTypeView(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializers
    queryset = RoomType.objects.all()

class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerializers
    queryset = Guest.objects.all()

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()

class RecordView(viewsets.ModelViewSet):
    serializer_class = RecordSerializers
    queryset = Hotel.objects.all()