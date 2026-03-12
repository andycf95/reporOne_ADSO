from django import forms
from .models import solicitudFalla

class solicitudFallaForm(forms.ModelForm):
    
    CRITICIDAD_CHOICES = [
            (1, '1 - Muy baja'),
            (2, '2 - Baja'),
            (3, '3 - Media'),
            (4, '4 - Alta'),
            (5, '5 - Crítica'),
        ]
        
    ESTADO_CHOICES = [
            ('Pendiente', 'Pendiente'),
            ('En proceso', 'En proceso'),
            ('Resuelto', 'Resuelto'),
            ('Cerrado', 'Cerrado'),
        ]

    criticidad = forms.ChoiceField(
            choices=CRITICIDAD_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    estado = forms.ChoiceField(
            choices=ESTADO_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control'})
        )
    
    class Meta:
        model = solicitudFalla
        fields = '__all__'

        widgets = {
            'nombre_activo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el nombre del activo'
            }),
            
            'sistema_afectado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el sistema afectado'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe la descripción de la falla'
            }),
            'accion_requerrida': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe la acción requerida'
            }),
            
        }
        
        CRITICIDAD_CHOICES = [
            (1, '1 - Muy baja'),
            (2, '2 - Baja'),
            (3, '3 - Media'),
            (4, '4 - Alta'),
            (5, '5 - Crítica'),
        ]
        
        ESTADO_CHOICES = [
            ('Pendiente', 'Pendiente'),
            ('En proceso', 'En proceso'),
            ('Resuelto', 'Resuelto'),
            ('Cerrado', 'Cerrado'),
        ]

        criticidad = forms.ChoiceField(
            choices=CRITICIDAD_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

        estado = forms.ChoiceField(
            choices=ESTADO_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control'})
        )
    