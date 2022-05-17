from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MarqueForm
from .forms import ModeleForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = MarqueForm(request)
        if form.is_valid():
            Marque = form.save()
            return HttpResponseRedirect("/Voiture/")
        else:
            return render(request,"Voiture/ajout.html",{"form": form})
    else :
        form = MarqueForm()
        return render(request,"Voiture/ajout.html",{"form" : form})

def ajout2(request):
    if request.method == "POST":
        form = ModeleForm(request)
        if form.is_valid():
            Modele = form.save()
            return HttpResponseRedirect("/Voiture/")
        else:
            return render(request,"Voiture/ajout2.html",{"form": form})
    else :
        form = ModeleForm()
        return render(request,"Voiture/ajout2.html",{"form" : form})

def traitement(request):
    form = MarqueForm(request.POST)
    if form.is_valid():
        marque = form.save()
        return HttpResponseRedirect("/Voiture/")
    else:
        return render(request,"Voiture/ajout.html",{"form": form})

def traitement2(request):
    mform = ModeleForm(request.POST)
    if mform.is_valid():
        Modele = mform.save()
        return HttpResponseRedirect("/Voiture/")
    else:
        return render(request,"Voiture/ajout2.html",{"form": mform})

def main(request):
    marque = list(models.Marque.objects.all())
    return render(request, 'Voiture/home.html', {'liste': marque})


def affiche(request, id):
    marque = models.Marque.objects.get(pk=id)
    modele = models.Modele.objects.filter(marque_id=id)
    return render(request,"Voiture/affiche.html",{"marque": marque,"modele": modele})

def delete(request, id):
    marque = models.Marque.objects.get(pk=id)
    marque.delete()
    return HttpResponseRedirect("/Voiture/")

def delete2(request, id):
    Modele = models.Modele.objects.get(pk=id)
    Modele.delete()
    return HttpResponseRedirect("/Voiture/")

def update(request, id):
    cform = MarqueForm(request.POST)
    if cform.is_valid():
        Marque = cform.save()
        return HttpResponseRedirect("/Voiture/")
    else:
        return render(request, "Voiture/update.html", {"form": cform, 'id': id})

def update2(request, id):
    jform = ModeleForm(request.POST)
    if jform.is_valid():
        Modele = jform.save()
        return HttpResponseRedirect("/Voiture/")
    else:
        return render(request, "Voiture/update2.html", {"form": jform, 'id': id})

def traitementupdate(request, id):
    cform = MarqueForm(request.POST)
    if cform.is_valid():
        Marque = cform.save(commit=False)
        Marque .id = id
        Marque.save()
        return HttpResponseRedirect("/Voiture")
    else:
        return render(request, "Voiture/update.html", {"form": cform, "id": id})

def traitementupdate2(request, id):
    jform = ModeleForm(request.POST)
    if jform.is_valid():
        Modele = jform.save(commit=False)
        Modele.id = id
        Modele.save()
        return HttpResponseRedirect("/Voiture")
    else:
        return render(request, "Voiture/update2.html", {"form": jform, "id": id})