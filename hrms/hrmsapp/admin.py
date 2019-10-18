from django.contrib import admin
from  .models import Hotel,RoomType,Room,Guest,Manager,Record,Booking

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'hotel_location',)
admin.site.register(Hotel,HotelAdmin)

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name','room_rent',)
admin.site.register(RoomType,RoomTypeAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','room_type','availability','bed_number',)
admin.site.register(Room,RoomAdmin)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name',)
admin.site.register(Guest,GuestAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_name',)
admin.site.register(Manager,ManagerAdmin)

# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('hotel_name','room1','is_avilable','cancel',)
# admin.site.register(Booking,BookingAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('guest','checkin_date','checkout_date','booking_date','checked_in','manager','cancel','bill')
admin.site.register(Record,RecordAdmin)
# Register your models here.
