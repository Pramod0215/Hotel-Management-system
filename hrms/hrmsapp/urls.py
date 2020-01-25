from django.urls import path, include
from .views import api_hotel_list_view, api_hotel_details_view, api_hotel_details_update, api_hotel_details_delete, \
  api_hotel_details_create, api_manager_list_view, api_manager_details_view, api_guest_details_create, \
  api_guest_details_delete, api_guest_details_update, api_guest_details_view, api_manager_details_create, \
  api_manager_details_delete, api_manager_details_update, api_record_details_view, api_record_list_view, \
  api_record_details_create, api_record_details_delete, api_record_details_update, api_room_list_view, \
  api_room_details_view, api_room_details_create, api_room_details_delete, api_room_details_update, \
  api_roomtype_list_view, api_roomtype_details_create, api_roomtype_details_delete, api_roomtype_details_update, \
  api_roomtype_details_view, api_guest_list_view, HotelListcreate, HotelListupdate

urlpatterns = [
  path('hotels/', api_hotel_list_view, name ='hotels'),
  path('hotels/<int:pk>/', api_hotel_details_view, name ='hotel_details'),
  path('hotels/<int:pk>/update/',api_hotel_details_update,name = 'hotel_details'),
  path('hotels/<int:pk>/delete/',api_hotel_details_delete,name = 'hotel_details'),
  path('hotels/create/',api_hotel_details_create,name = 'hotel_details'),

  path('manager/', api_manager_list_view, name ='manager'),
  path('manager/<int:pk>/', api_manager_details_view, name ='manager_details'),
  path('manager/<int:pk>/update/',api_manager_details_update,name = 'manager_details'),
  path('manager/<int:pk>/delete/',api_manager_details_delete,name = 'manager_details'),
  path('manager/create/',api_manager_details_create,name = 'manager_details'),

  path('guest/', api_guest_list_view, name ='guest'),
  path('guest/<int:pk>/', api_guest_details_view, name ='guest_details'),
  path('guest/<int:pk>/update/',api_guest_details_update,name = 'guest_details'),
  path('guest/<int:pk>/delete/',api_guest_details_delete,name = 'guest_details'),
  path('guest/create/',api_guest_details_create,name = 'guest_details'),

  path('record/', api_record_list_view, name='record'),
  path('record/<int:pk>/', api_record_details_view, name='record_details'),
  path('record/<int:pk>/update/', api_record_details_update, name='record_details'),
  path('record/<int:pk>/delete/', api_record_details_delete, name='record_details'),
  path('record/create/', api_record_details_create, name='record_details'),

  path('room/', api_room_list_view, name='room'),
  path('room/<int:pk>/', api_room_details_view, name='room_details'),
  path('room/<int:pk>/update/', api_room_details_update, name='room_details'),
  path('room/<int:pk>/delete/', api_room_details_delete, name='room_details'),
  path('room/create/', api_room_details_create, name='room_details'),


  path('roomtype/', api_roomtype_list_view, name='roomtype'),
  path('roomtype/<int:pk>/', api_roomtype_details_view, name='roomtype_details'),
  path('roomtype/<int:pk>/update/', api_roomtype_details_update, name='roomtype_details'),
  path('roomtype/<int:pk>/delete/', api_roomtype_details_delete, name='roomtype_details'),
  path('roomtype/create/', api_roomtype_details_create, name='roomtype_details'),


  path('room/listcreate/',HotelListcreate.as_view(), name='hotel_generic'),


]