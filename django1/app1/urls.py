from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('square/',views.square,name='square'),
    path('fact2/',views.fact2,name='fact2'),
    path('factorial_input/',views.factorial_input,name='factorial_input'),
    path('index/',views.index,name='index'),
     path('home1/',views.home1,name='home1'),
     path('factorial/',views.factorial,name='factorial'),
]