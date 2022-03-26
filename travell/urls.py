from django.urls import path

from . import views

urlpatterns = [path('',views.index, name='index'),
               path('accounts/amintiri',views.amintiri, name='amintiri'), 
               path('accounts/send_amintiri',views.send_amintiri, name='send_amintiri') 
                ]