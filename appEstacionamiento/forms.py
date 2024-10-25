from django import forms
from appEstacionamiento.models import ClienteEst

class FormCliente(forms.ModelForm):
    class Meta:
        model = ClienteEst
        fields = '__all__'