
from django import forms
from .models import Information


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['date','trade_code', 'high', 'low', 'open', 'close', 'volume']
