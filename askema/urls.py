from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This registers the admin namespace
    path('', include('main.urls')),   # Your app URLs
]
