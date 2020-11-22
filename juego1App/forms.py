from django import forms

class FormComprar(forms.Form):
    nombre_completo = forms.CharField(max_length=55, label='Nombre Completo')
    contacto = forms.CharField(empty_value='No', max_length=55, widget=forms.TextInput(attrs={'placeholder': 'correo o teléfono'})) #puede ser correo o numero de telefono
    cont_super_usuario = forms.CharField(max_length=15, label='contrasenia', widget=forms.TextInput(attrs={'placeholder':'Identificate!'}))


class FormRegistrar(forms.Form):
    ACCIONES = [(0, '--Seleccione--'), (1, 'Desplazar arriba'), (2, 'Desplazar abajo'), (3, 'intercambiar arriba'), (4, 'intercambiar abajo')]
    codigo = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder':'Código de participación'}))
    accion = forms.ChoiceField(required=True, choices=ACCIONES, label='acción'   )
    num_accion = forms.IntegerField(max_value=5, min_value=1, initial=1, label='posiciones para tu acción')