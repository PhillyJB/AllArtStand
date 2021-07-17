from django import forms
from .models import Art_Pieces


class Art_PiecesForm(forms.ModelForm):

    class Meta:
        model = Art_Pieces
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
