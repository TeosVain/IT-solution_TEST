from django import forms

from .models import CashFlowRecord


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }