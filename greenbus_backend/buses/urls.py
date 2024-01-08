from django.urls import path
from .views import create_routes, get_buses, search_buses, get_routes, create_buses, update_bus, delete_bus, update_route

urlpatterns = [
    path('', get_buses, name='get_buses'),
    path('search/', search_buses, name='search_buses'),
    path('routes/', get_routes, name='get_routes'),
    path('routes/create/', create_routes, name='create_routes'),
    path('create/', create_buses, name='create_buses'),
    path('update/', update_bus, name='update_bus'),
    path('delete/', delete_bus, name='delete_bus'),
    path('routes/update/', update_route, name='update_route'),    
]
