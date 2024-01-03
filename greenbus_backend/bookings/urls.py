from django.urls import path

from .views import book_bus, cancel_booking

urlpatterns = [
    path('', book_bus, name='book_bus'),
    path('cancel/', cancel_booking, name='cancel_booking'),
]
