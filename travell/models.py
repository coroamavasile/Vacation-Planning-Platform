from django.db import models

# Create your models here.
# clasele principale ale acestui proiect

# clasa pentru destinatiile de vacanta
class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)

# clasa pentru meniul de amintiri
class Amintiri(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

# clasa pentru meniul de rezervari
class Rezervari(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    nume_locatie = models.CharField(max_length=100)
    numar_persoane = models.IntegerField()
    data = models.DateTimeField()

# clasa pentru review-uri
class Review(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    nume_locatie = models.CharField(max_length=100)
    review = models.TextField()
    nr_stele = models.IntegerField()
