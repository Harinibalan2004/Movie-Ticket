from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/',include('details.urls')),
    path('enter/',include('Movie.urls')),
    path('tickets/',include('Tickets.urls')),
]