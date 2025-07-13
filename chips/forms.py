from  django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'category']
        widgets = {
            'type': forms.RadioSelect()
        }