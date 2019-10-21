from django.contrib import admin
from django import forms
from  .models import Hotel,RoomType,Room,Guest,Manager,Record

class HotelAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HotelAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        hotel = self.cleaned_data.get('hotel_name')
        if len(hotel) < 4:
            raise forms.ValidationError("Hotel name cannot be less than 4", code='error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(HotelAdminForm, self).save(commit=commit)

class RoomAdminFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomAdminFrom,self).__init__(*args, **kwargs)


    def clean(self):
        guest_number = self.cleaned_data.get('bed_number')
        room_number1 = self.cleaned_data.get('room')
        if guest_number > 3:
            raise forms.ValidationError('In one room max 3 person only allowed',code='error')


        return self.cleaned_data

    def save(self,commit= True):
        return super(RoomAdminFrom,self).save(commit=commit)

class RecordAdminFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecordAdminFrom,self).__init__(*args, **kwargs)


    def clean(self):
        checked_out_date = self.cleaned_data.get('checkout_date')
        checked_in_date = self.cleaned_data.get('checkin_date')
        booking_date1 = self.cleaned_data.get('booking_date')
        rooms = self.cleaned_data.get('room')


        # if checked_out_date==None:
        #     raise forms.ValidationError('Checkout date invalid!', code='error')

        #Chech in date has to be greater than today's date
        #Check out date has to be greater than check in date

        if checked_in_date > checked_out_date:
            raise forms.ValidationError('Checkout date invalid!',code='error')
        if booking_date1> checked_out_date:
            raise forms.ValidationError('Checkout date invalid!', code='error')
        if booking_date1> checked_in_date:
            raise forms.ValidationError('Checkout date invalid!', code='error')
        checked_in_date_obj = Record.objects.filter(checkin_date=checked_in_date).exists()
        checked_out_date_obj=Record.objects.filter(checkout_date=checked_out_date).exists()


        if Record.objects.filter(room=rooms).exists():
            if Record.objects.filter(checked_in_date=(checked_in_date_obj,checked_out_date)):
            # if Record.objects.filter(checkin_date=checked_in_date).exists():
            #     if Record.objects.filter(checkout_date=checked_out_date).exists():
            #         if Record.objects.filter(checkin_date=checked_in_date).exists()< checked_in_date<Record.objects.filter(checkout_date=checked_out_date).exists():


                raise forms.ValidationError("Can't booked this room , this is already booked", code='error')
        return self.cleaned_data


    def save(self,commit= True):
        return super(RecordAdminFrom,self).save(commit=commit)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'hotel_location',)
    form = HotelAdminForm
admin.site.register(Hotel,HotelAdmin)

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name','room_rent',)

admin.site.register(RoomType,RoomTypeAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','room_type','availability','bed_number',)
    form = RoomAdminFrom
admin.site.register(Room,RoomAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name',)
admin.site.register(Guest,GuestAdmin)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_name','manager_phone','manager_email')
admin.site.register(Manager,ManagerAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('guest','checkin_date','checkout_date','checked_in','manager','cancel','bill')
    form = RecordAdminFrom
admin.site.register(Record,RecordAdmin)
# Register your models here.
