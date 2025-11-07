# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt

def bookings(request):
    # If value of request.method is equal to "POST"
    if request.method == "POST":
        # Wrap POST handling in try/except to capture errors for debugging
        try:
            # Create a variable called data and assign it the value of json.loads(request.body)
            try:
                data = json.loads(request.body)
            except Exception:
                return HttpResponse(json.dumps({"error": "Invalid JSON"}), status=400, content_type='application/json')

            # Create a variable called exist and assign the following value to it:
            # Booking.objects.filter(reservation_date=data['reservation_date']).filter(reservation_slot=data['reservation_slot']).exists()
            exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(reservation_slot=data['reservation_slot']).exists()

            # If the value of the exist variable is False:
            if exist is False:
                # Create a variable called booking and assign the value of the Booking() class object with fields
                booking = Booking(
                    first_name=data['first_name'],
                    reservation_date=data['reservation_date'],
                    reservation_slot=data['reservation_slot'],
                )
                # Call the save() function over the booking variable
                booking.save()
            else:
                # Else return HttpResponse() with error
                return HttpResponse("{'error':1}", content_type='application/json')
        except Exception as e:
            # Return the exception string for diagnosis
            return HttpResponse(json.dumps({"error": str(e)}), status=500, content_type='application/json')

    # Create a variable called date and assign it the value: request.GET.get('date',datetime.today().date())
    date = request.GET.get('date', datetime.today().date())

    # Create a variable called bookings and assign it the value: Booking.objects.all().filter(reservation_date=date)
    bookings = Booking.objects.all().filter(reservation_date=date)

    # Create a variable called booking_json and assign it the value: serializers.serialize('json', bookings)
    booking_json = serializers.serialize('json', bookings)

    # Return HttpResponse() with booking_json and content_type 'application/json'
    return HttpResponse(booking_json, content_type='application/json')