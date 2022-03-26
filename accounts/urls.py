from django.urls import path

from . import views

urlpatterns = [path("register",views.register, name = "register"),
               path("login",views.login, name= "login"),
               path("logout",views.logout, name= "logout"),
               path('amintiri',views.amintiri, name='amintiri'), 
               path('send_amintiri',views.send_amintiri, name='send_amintiri'),
               path('rezervari',views.rezervari, name='rezervari'),
               path('viz_rezervari',views.viz_rezervari,name='viz_rezervari'),
               path('adauga_locatii',views.adauga_locatii,name='adauga_locatii'),
               path('adauga_review',views.adauga_review,name='adauga_review'),
               path('viz_review',views.viz_review,name='viz_review')
               
            ]               