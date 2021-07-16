
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('person/', person, name='person'),
    path('technology/', Technology, name='technology'),
]