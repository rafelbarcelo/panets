from django imports forms

class Contacto(forms.Form)
    nombre=forms.CharField(label="Nombre", required=True)
    email= forms.EmailField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido"
    required=True, widget=forms.Textarea)