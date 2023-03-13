from django.shortcuts import render
from .models import People
from django.views.generic import ListView

# Create your views here.
class PeopleList(ListView):
#    model = People
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            people_list = People.objects.filter(
                name__icontains=query)
        else:
            people_list = People.objects.all()
        return people_list
