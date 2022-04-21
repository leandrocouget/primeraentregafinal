from django import forms


class registroformulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.CharField()
    ciudad = forms.CharField()
    email = forms.EmailField()

class registroArticulos(forms.Form):
    nombre = forms.CharField()
    precio = forms.CharField()
    cantidad = forms.CharField()
   