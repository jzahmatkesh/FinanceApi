from django.db.models.fields import DateTimeField
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def SimpleView(request):
    html = "<html><body>hi body</body></html>"
    return HttpResponse(html)