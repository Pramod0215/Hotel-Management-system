from django.urls import path, include
#from.import views
from rest_framework import routers
from . import views


routers = routers.DefaultRouter()
routers.register('hotel',views.HotelView)
routers.register('manager',views.ManagerView)
routers.register('roomType',views.RoomTypeView)
routers.register('room',views.RoomView)
routers.register('guest',views.GuestView)
routers.register('record',views.RecordView)



urlpatterns = [
  path('',include(routers.urls)),

]