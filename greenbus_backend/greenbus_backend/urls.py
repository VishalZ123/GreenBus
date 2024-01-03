from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authn.urls")),
    path("buses/", include("buses.urls")),
    path("bookings/", include("bookings.urls")),
]
