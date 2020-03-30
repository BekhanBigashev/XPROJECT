
from django.urls import path, include
from django.contrib import admin
from landing import views

from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('', include('orders.urls')),
    path('', include('products.urls')),
]
