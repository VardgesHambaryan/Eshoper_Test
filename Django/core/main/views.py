from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.
class ContactListView(ListView):
    template_name = "index.html"
    
    def get(self, request):
        contacts = Contacts.objects.all()
        return render(request , self.template_name , {"contacts": contacts})

class LoginListView(ListView):
    template_name = 'login.html'

    def get(self, request):
        return render(request , self.template_name)