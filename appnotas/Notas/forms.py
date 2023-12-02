from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Nota

        fields = [
            'Titulo',
            'Nota',
            
        ]

        labels = {
            
            'Nota':'Numero',
            'Titulo':'titulo',
          
        }

        widgets = {
            'Nota':forms.TextInput(attrs={'class':'form-control'}),
            'Titulo':forms.TextInput(attrs={'class':'form-control'}),
            
        
        }
    
    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.fields['Titulo'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}