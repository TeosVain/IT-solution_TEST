from django.urls import path

from pages.views import MainPage

app_name = 'pages'

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
]
