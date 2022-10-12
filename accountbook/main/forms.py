from django import forms
from .models import Consume

class Consumeform(forms.ModelForm):

    class Meta:
        model = Consume
        fields = '__all__'
        # exclude = ('title',)
