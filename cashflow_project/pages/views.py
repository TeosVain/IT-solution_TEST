from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'pages/main.html'


def page_not_found(request, exception=None):
    return render(request, 'pages/404.html', status=404)


def server_failure_500(request):
    return render(request, 'pages/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def error_403(request, exception=None):
    return render(request, 'pages/403.html', status=403)