from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import FlightViewSet
from django.urls import path
from .views import RealTimeFlightsView

# router = DefaultRouter()
# router.register('flights', FlightViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('flights/', RealTimeFlightsView.as_view(), name='real-time-flights'),
]