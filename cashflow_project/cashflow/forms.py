from django import forms

from .models import CashFlowRecord, Category, Status, Subcategory, Type


class CashFlowForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
        label='Дата',
        required=False
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Комментарий'}),
        label='Комментарий',
        required=False
    )

    class Meta:
        model = CashFlowRecord
        exclude = ('author',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название категории'}),
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название подкатегории'}),
            'category': forms.Select(attrs={'placeholder': 'Выберите категорию'})
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