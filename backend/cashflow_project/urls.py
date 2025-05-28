from django.contrib import admin
from django.urls import path, include

handler403 = 'pages.views.error_403'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_failure_500'

app_name = 'main'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('cash/', include('cashflow.urls')),
]
