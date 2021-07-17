from django import forms
from .models import Art_Pieces


class Art_PiecesForm(forms.ModelForm):

    class Meta:
        model = Art_Pieces
        fields = '__all__'
