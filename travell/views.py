from django.shortcuts import render,redirect
from .models import Destination,Amintiri
# Create your views here.

# metoda necesara pentru vizualizarea locatiilor de vacanta disponibile
def index(request):
    # luam obiectele din baza de date
    dests = Destination.objects.all()
    # le trimitem la pagina
    return render(request, "index.html", {'dests':dests})


# metoda necesara pentru vizualizarea amintirilor
def amintiri(request):
    
    # luam datele din baza de date
    amintiri = Amintiri.objects.all()
    # trimitem datele la pagina html
    return render(request, "amintiri.html", {'dests':amintiri})

# metoda necesara pentru adaugarea unei amintiri
def send_amintiri(request):
    # luam datele de pe pagina
    if request.method == 'POST':
        name = request.POST['name']
        img  = request.FILES['img']
        desc = request.POST['desc']
    # adaugam datele in baza de date
    amintiri_info = Amintiri(name = name,img = img,desc=desc)
    amintiri_info.save()
    # suntem redirectionati la pagina de amintiri
    return redirect("amintiri")
 