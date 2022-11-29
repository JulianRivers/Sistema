from django import forms

class registrarAspirante(forms.Form):
    nombre = forms.CharField(label='Nombres', required=True, widget=forms.TextInput(attrs={"autofocus": True}))
    apellido = forms.CharField(label='Apellidos', required=True)
    numero_documento = forms.CharField(label='Documento', max_length=15, required=True)
    tipo_documento = forms.CharField("Tipo documento", max_length=5, required=True)
    profesion = forms.CharField("profesion", max_length=10, required=True)
    edad = forms.IntegerField("edad", required=True)
    ciudad = forms.CharField("ciudad", max_length=20, required=True)