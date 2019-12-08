from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pharmacy_app/', include('pharmacy_app.urls')),
    path('clients/', include('clients.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]