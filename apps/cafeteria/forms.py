from django import forms 
from apps.cafeteria.models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta: #Faz referência aos meta dados da classe de Produto
        model = Produto
        exclude = ['publicada',]
        labels = {
            'denominacao': 'Denominação',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
            'data_criacao': 'Data de Criação',
            'usuario': 'Usuário',
        }

        widgets = {
            'denominacao': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'imagem': forms.FileInput(attrs={'class':'form-control'}),
            'data_criacao': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),            
            'usuario': forms.Select(attrs={'class':'form-control'}),
                                     
        }
