from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class MarqueForm(ModelForm):
    class Meta:
        model = models.Marque
        fields = ('nom_Marque', 'pays_Marque', 'date_parution_Marque','description')
        labels = {
            'nom_Marque' : _('Nom de la marque'),
            'pays_Marque' : _('Pays de la marque') ,
            'date_parution_Marque' : _('Date de parution de la marque'),
            'description' : _('Description')
        }

class ModeleForm(ModelForm):
    class Meta:
        model = models.Modele
        fields = ('nom_modele', 'date_creation_modele', 'nombre_modele','description', 'marque')
        labels = {
            'nom_modele': _('Nom du modèle'),
            'date_creation_modele': _('Date de creation du modèle'),
            'nombre_modele': _('Nombre de modele créer'),
            'description': _('description'),
            'Marque' : _("Marque:")
        }