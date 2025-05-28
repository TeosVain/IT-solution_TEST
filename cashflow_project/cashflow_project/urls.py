from django.contrib import admin
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('cash/', include('cashflow.urls')),
]
