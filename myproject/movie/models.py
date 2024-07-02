from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

class Screen(models.Model):
    name = models.CharField(max_length=50)

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    time = models.DateTimeField()

class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

class Reservation(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Use a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Use a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )