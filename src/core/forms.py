from django import froms

from .pqrsf import PQRSF_CHOICES

class ContactForm(forms.Form):
#crear campos
    email = forms.EmailField(label="Correo Electronico", widget=forms.EmailInput(attrs={'class':'form-control'}), required = True)
    tipom = forms.ChoiceField(choices = PQRSF_CHOICES,label="Tipo de Atencion Requerida",initial='',widget=forms.Select(attrs=
    {'class':'form-control'}),required = True)
    nombre = forms.CharField(label="Nombre",required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    msj=forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}),required=True)