from django.shortcuts import render
from .models import Flight,Passenger,Reservation
from .serializers import flightSerializer,reservationSerializer,passengerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# find the tickets and book the tickets
@api_view(['POST'])
def findFind(request):
    flights = Flight.objects.filter(departureCity= request.data['departureCity'],arrivalCity= request.data['arrivalCity'],departureDate= request.data['departureDate'])
    serializer = flightSerializer(flights, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def saveFlight(request):
    flight = Flight.objects.get(id=request.data['flightid'])

    passenger = Passenger()
    passenger.firstName= request.data['firstName']
    passenger.lastName= request.data['lastName']
    passenger.mideName= request.data['midName']
    passenger.email= request.data['email']
    passenger.phone= request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()
    return Response(status= status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = flightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = passengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = reservationSerializer


