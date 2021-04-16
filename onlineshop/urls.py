from onlineshop.views import SimpleView
from django.urls import path

urlpatterns = [
    path('', SimpleView),
]