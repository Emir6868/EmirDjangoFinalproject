
from django.db import models


class Marque(models.Model): #déclare la classe Livre héritant de la classe Model, classede base des modèles
    nom_Marque = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    pays_Marque = models.CharField(max_length = 100)
    date_parution_Marque = models.DateField(blank = True, null = True) # champs de type date,pouvant être null ou ne pas être rempli
    description = models.TextField(null = True, blank = True) # champs de type text long

    def __str__(self):
        chaine = f"{self.nom_Marque}"
        return chaine

class Modele(models.Model):
    nom_modele = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    date_creation_modele = models.DateField(blank=True, null=True)  # champs de type date,pouvant être null ou ne pas être rempli
    nombre_modele = models.IntegerField(blank=False)  # champs de type entier devant être obligatoirement rempli
    description = models.TextField(null=True, blank=True)  # champs de type text long
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE,default= None, null=True)

    def __str__(self):
        chaine = f"{self.nom_Marque} est une marque de voiture du pays {self.pays_modele} et cette marque a été créer en"
        return chaine