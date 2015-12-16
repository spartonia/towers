from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = "<html><body>Almost there</body></html>"
    return HttpResponse(html)