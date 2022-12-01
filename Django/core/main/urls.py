from django.urls import path
from .views import *
urlpatterns = [ 
    path('', ContactListView.as_view(), name= 'home' ),
    path('login/' , LoginListView.as_view() , name= 'login')

]