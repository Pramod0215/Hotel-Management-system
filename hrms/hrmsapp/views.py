from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets,status
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

@ api_view(['GET'])
def api_hotel_list_view(request):
    hotel = Hotel.objects.all()
    if request.method == 'GET':
        serializer = HotelSerializers(hotel,many=True)

    return Response(serializer.data)

@ api_view(['GET'])
def api_hotel_details_view(request,pk):
    serializer = None
    try:
        hotel = Hotel.objects.get(id=pk)
        serializer = HotelSerializers(hotel)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def api_hotel_details_create(request):
    if request.method == 'POST':
        serializer = HotelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Create successful!'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@ api_view(['PUT'])
def api_hotel_details_update(request, pk):
    try:
        hotel = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = HotelSerializers(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['DELETE'])
def api_hotel_details_delete(request,pk):
    try:
        hotel = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = HotelSerializers(hotel, data=request.data)
        data = {}
        if serializer.is_valid():
            hotel.delete()
            data['success'] = 'delete successful'
            return Response(status=status.HTTP_200_OK)
        else:
            data['failure'] = 'delete failed!'
            return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['GET'])
def api_manager_list_view(request):
    manager = Manager.objects.all()
    if request.method == 'GET':
        serializer = ManagerSerializers(manager,many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_manager_details_view(request,pk):
    serializer = None
    try:
        manager = Manager.objects.get(id=pk)
        serializer = ManagerSerializers(manager)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def api_manager_details_create(request):
    if request.method == 'POST':
        serializer = ManagerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Create successful!'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



@ api_view(['PUT'])
def api_manager_details_update(request, pk):
    try:
        manager = Manager.objects.get(id=pk)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ManagerSerializers(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['DELETE'])
def api_manager_details_delete(request,pk):
    try:
        manager = Manager.objects.get(id=pk)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = ManagerSerializers(manager, data=request.data)
        data = {}
        if serializer.is_valid():
            manager.delete()
            data['success'] = 'delete successful'
            return Response(status=status.HTTP_200_OK)
        else:
            data['failure'] = 'delete failed!'
            return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['GET'])
def api_guest_list_view(request):
    guest = Guest.objects.all()
    if request.method == 'GET':
        serializer = GuestSerializers(guest,many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_guest_details_view(request,pk):
    serializer = None
    try:
        guest = Guest.objects.get(id=pk)
        serializer = GuestSerializers(guest)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def api_guest_details_create(request):


    if request.method == 'POST':
        serializer = GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Create successful!'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



@ api_view(['PUT'])
def api_guest_details_update(request, pk):
    try:
        guest = Guest.objects.get(id=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GuestSerializers(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['DELETE'])
def api_guest_details_delete(request,pk):
    try:
        guest = Guest.objects.get(id=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = GuestSerializers(guest, data=request.data)
        data = {}
        if serializer.is_valid():
            guest.delete()
            data['success'] = 'delete successful'
            return Response(status=status.HTTP_200_OK)
        else:
            data['failure'] = 'delete failed!'
            return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@ api_view(['GET'])
def api_record_list_view(request):
    record = Record.objects.all()
    if request.method == 'GET':
        serializer = RecordSerializers(record,many=True)

    return Response(serializer.data)

@ api_view(['GET'])
def api_record_details_view(request,pk):
    serializer = None
    try:
        record = Record.objects.get(id=pk)
        serializer = RecordSerializers(record)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def api_record_details_create(request):
    if request.method == 'POST':
        serializer = RecordSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Create successful!'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



@ api_view(['PUT'])
def api_record_details_update(request, pk):
    try:
        record = Record.objects.get(id=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = RecordSerializers(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['DELETE'])
def api_record_details_delete(request,pk):
    try:
        record = Record.objects.get(id=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = RecordSerializers(record, data=request.data)
        data = {}
        if serializer.is_valid():
            record.delete()
            data['success'] = 'delete successful'
            return Response(status=status.HTTP_200_OK)
        else:
            data['failure'] = 'delete failed!'
            return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@ api_view(['GET'])
def api_room_list_view(request):
    room = Record.objects.all()
    if request.method == 'GET':
        serializer = RoomSerializers(room,many=True)

    return Response(serializer.data)

@ api_view(['GET'])
def api_room_details_view(request,pk):
    serializer = None
    try:
        room = Record.objects.get(id=pk)
        serializer = RoomSerializers(room)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def api_room_details_create(request):
    if request.method == 'POST':
        serializer = RoomSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Create successful!'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



@ api_view(['PUT'])
def api_room_details_update(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RoomSerializers(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['DELETE'])
def api_room_details_delete(request,pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = RoomSerializers(room, data=request.data)
        data = {}
        if serializer.is_valid():
            room.delete()
            data['success'] = 'delete successful'
            return Response(status=status.HTTP_200_OK)
        else:
            data['failure'] = 'delete failed!'
            return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@ api_view(['GET'])
def api_roomtype_list_view(request):
    roomtype = RoomType.objects.all()
    if request.method == 'GET':
        serializer = RoomTypeSerializers(roomtype,many=True)

    return Response(serializer.data)

@ api_view(['GET'])
def api_roomtype_details_view(request,pk):
    serializer = None
    try:
        roomtype = RoomType.objects.get(id=pk)
        serializer = RoomTypeSerializers(roomtype)
    except RoomType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def api_roomtype_details_create(request):
    if request.method == 'POST':
        serializer = RoomSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Create successful!'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



@ api_view(['PUT'])
def api_roomtype_details_update(request, pk):
    try:
        roomtype = RoomType.objects.get(id=pk)
    except RoomType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RoomTypeSerializers(roomtype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update successful'
            return Response(data=data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@ api_view(['DELETE'])
def api_roomtype_details_delete(request,pk):
    try:
        roomtype = RoomType.objects.get(id=pk)
    except RoomType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = RoomTypeSerializers(roomtype, data=request.data)
        data = {}
        if serializer.is_valid():
            roomtype.delete()
            data['success'] = 'delete successful'
            return Response(status=status.HTTP_200_OK)
        else:
            data['failure'] = 'delete failed!'
            return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
