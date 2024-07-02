from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Movie, Screen, Showtime, Seat, Reservation
from .forms import ReservationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'movie/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('movie_list')
    else:
        form = AuthenticationForm()
    return render(request, 'movie/login.html', {'form': form})

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

@login_required
def showtime_detail(request, showtime_id):
    showtime = Showtime.objects.get(pk=showtime_id)
    seats = Seat.objects.filter(screen=showtime.screen)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Process reservation and payment here
            # Update seat status, create reservation entry, etc.
            return redirect('confirmation')
    else:
        form = ReservationForm()
    return render(request, 'showtime_detail.html', {'showtime': showtime, 'seats': seats, 'form': form})

# Implement other views for seat selection, payment processing, and confirmation
def logout_view(request):
    logout(request)
    # Redirect to a success page or a home page.
    return redirect('home')  # Replace 'home' with the name of your home URL pattern