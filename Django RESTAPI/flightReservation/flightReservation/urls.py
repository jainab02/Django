"""
URL configuration for flightReservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from flightApi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# routers are for viewsets
router.register('flight',views.FlightViewSet)
router.register('passenger',views.PassengerViewSet)
router.register('reservation',views.ReservationViewSet)
# custom function there should be an path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('flightAPI/',include(router.urls)),
    path('flightAPI/findFlight/',views.findFind),
    path('flightAPI/savedFlight/',views.saveFlight),
    

]
