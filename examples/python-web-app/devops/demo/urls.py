from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),  # Include URLs from your 'demo' app
    path('', include('demo.urls')),  # Route base URL to 'demo' app
]
