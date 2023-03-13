from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeopleList.as_view(), name='people'),
]
