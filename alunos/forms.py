from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'curso', 'bio']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: Ana Souza'}),
            'curso': forms.TextInput(attrs={'placeholder': 'Ex: ADS, SI, Engenharia...'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Fale um pouco sobre você...', 'maxlength': 280, 'rows': 4}),
        }
