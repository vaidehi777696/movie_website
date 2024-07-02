from django.contrib import admin

# Register your models here.
from .models import Movie, Screen, Showtime, Seat, Reservation

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')

@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'screen', 'time')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('screen', 'seat_number', 'is_booked')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'showtime')