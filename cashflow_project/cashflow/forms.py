from django import forms

from cashflow.models import CashFlowRecord, Category, Status, Subcategory, Type
from cashflow_project.constants import ROWS


class CashFlowForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
        label='Дата',
        required=False
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': ROWS, 'placeholder': 'Комментарий'}
        ),
        label='Комментарий',
        required=False
    )

    class Meta:
        model = CashFlowRecord
        fields = [
            'date', 'status', 'type', 'category',
            'subcategory', 'amount', 'comment'
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Название категории'}
            ),
        }


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Название подкатегории'}
            ),
            'category': forms.Select(
                attrs={'placeholder': 'Выберите категорию'}
            ),
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название статуса'})
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название типа'})
        }
