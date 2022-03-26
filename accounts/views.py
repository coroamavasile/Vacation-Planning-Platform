from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import *
# Create your views here.


# metoda folosita pentru a ne loga
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            # daca userul exista ne logam
            auth.login(request,user)
            messages.info(request,'Succes')
            return redirect("/")
        else:
            #daca am introdus gresit datele primim un mesaj de atentionare
            messages.info(request,'Credidentiale invalide')
            return redirect('login')
    else:
        return render(request,'login.html')

# metoda folosita pentru inregistrarea unui cont nou
def register(request):

    if request.method == 'POST':
        #luam datele de pe pagina
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        #verificam daca parola initiala si cea pentru verificare sunt la fel
        if password1==password2:
            if User.objects.filter(username=username).exists():
                # verificam daca numele de utilizator ales se gaseste in baza de date
                messages.info(request,'Utilizator existent')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                #verificam daca email-ul ales a mai fost folosit de catre alt utilizator
                messages.info(request,'Email utilizat')
                return redirect('register')
            else:
                # daca ajungem aici inseamna ca am reusit sa creem contul
                # dupa care ii adaugam datele in baza de date
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Utilizator creat')
                return redirect("login")
        else:
            #in cazul in care parolele nu se potrivesc trimitem un mesaj pe pagina
            messages.info(request,'Parola nu se potriveste')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


#metoda folosita pentru a ne deloga de pe un cont
def logout(request):
    auth.logout(request)
    return redirect('/')

# metoda folosita in pagina de amintiri
# cand dorim sa incarcam o amintire
def send_amintiri(request):

    if request.method == 'POST':
        name = request.POST['name']
        img  = request.POST['img']
        desc = request.POST['desc']
    
    amintiri_trimite = Amintiri.objects.create(name='name',img='img',desc='desc')
    amintiri_trimite.save()
    return redirect('/')

def amintiri(request):
    amintiri = Amintiri.objects.all()
    return render(request, "amintiri.html", {'dests':amintiri})


# metoda folosita pentru realizarea unei rezervari
def rezervari(request):

    print("rezervari")
    # luam datele de pe pagina
    if request.method =='POST':
        nume = request.POST['nume']
        prenume = request.POST['prenume']
        nume_locatie = request.POST['nume_locatie']
        numar_persoane = request.POST['numar_persoane']
        data = request.POST['data']

        # adaugam datele in baza de date
        rezervari_info = Rezervari(nume=nume,prenume=prenume,nume_locatie= nume_locatie,numar_persoane=numar_persoane,data=data)
        rezervari_info.save()
        # print(numar_persoane)
        # print(nume_locatie)
        # print(data)
    return render(request, "rezervari.html")


# metoda necesara pentru vizualizarea rezervarilor
def viz_rezervari(request):
    # luam rezervarile din baza de date
    rezervari_viz = Rezervari.objects.all()
    # le trimitem la pagina
    return render(request, "viz_rezervari.html",{'rezervari':rezervari_viz})


# metoda responsabila pentru adaugarea de locatii
def adauga_locatii(request):

    if request.method == 'POST':
        # luam datele de pe pagina
        name = request.POST['name']
        img  = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']

        # le adaugam in baza de date
        destinatii = Destination(name = name, img = img, desc = desc, price = price)
        destinatii.save()
        # suntem redirectionati la pagina principala
        return redirect('/')
    
    return render(request, "adauga_locatii.html")

# metoda responsabila pentru adaugarea unui review
def adauga_review(request):

    if request.method == 'POST':
        # luam datele de pe pagina
        nume = request.POST['name']
        prenume  = request.POST['prenume']
        nume_locatie = request.POST['nume_locatie']
        review = request.POST['review']
        numar_stele = request.POST['rating']

        # le adaugam in baza de date
        destinatii = Review(nume = nume,prenume= prenume,nume_locatie=nume_locatie,review=review,nr_stele = numar_stele)
        destinatii.save()
        # suntem redirectionati la pagina principala
        return redirect('/')
    
    return render(request, "adauga_review.html")

# metoda responsabila pentru vizualizarea review-urilor
def viz_review(request):
    # luam datele din baza de date
    review_viz = Review.objects.all()
    # trimitem datele catre pagina
    return render(request, "viz_review.html",{'rezervari':review_viz})