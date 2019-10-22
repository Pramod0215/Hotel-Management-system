from django.test import TestCase
from .models import Hotel, RoomType


class HotelTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(hotel_name = 'taj Hotel',hotel_location = 'Banglore')

    def test_Hotel_test_case(self):

        hotel = Hotel.objects.get(hotel_name = 'taj Hotel', hotel_location = 'Banglore')
        self.assertEqual(hotel.hotel(),'taj Hotel Banglore')
        # self.assertEqual(hotel.hotel_location, 'taj Hotel')

class RoomTypeCase(TestCase):
    def setUp(self):
        RoomType.objects.create(name = 'delux',room_rent = 7000)

    def test_RoomType_test_case(self):
        roomtype = RoomType.objects.get(name='delux',room_rent=7000)
        self.assertEqual(roomtype.roomtype(), 7000)
        self.assertEqual(roomtype.name, 'delux')

# class RecordTestCase(TestCase):
#     def setUp(self):
#         Record.objects.create(member='',b)
#
#     def test_record_test_case(self):
#
#         record1 = Record.objects.get()
#         self.assertEqual(record1.update_stock(),  "munshi premchand")




# # Create your tests here.
