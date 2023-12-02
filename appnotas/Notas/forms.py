from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de notas.
    """

    class Meta: 
        model = Nota

        fields = [
            'Titulo',
            'Nota',
            'fecha',  # Agrega el campo fecha al formulario
        ]

        labels = {
            'Nota': 'Numero',
            'Titulo': 'titulo',
            'fecha': 'Fecha de Creación',  # Ajusta la etiqueta según tus necesidades
        }

        widgets = {
            'Nota': forms.TextInput(attrs={'class': 'form-control'}),
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields['Titulo'].error_messages = {'required': 'custom required message'}

        # Asegúrate de que el campo fecha esté incluido en la lista de campos
        for field in self.fields.values():
            field.error_messages = {'required': f'El campo {field.label} es obligatorio'}