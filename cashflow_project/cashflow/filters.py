import django_filters
from django import forms
from cashflow.models import CashFlowRecord


class CashFlowRecordFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(
        field_name='date',
        lookup_expr='gte',
        label='Дата от',
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'})
    )
    date_to = django_filters.DateFilter(
        field_name='date',
        lookup_expr='lte',
        label='Дата до',
        widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'})
    )

    class Meta:
        model = CashFlowRecord
        fields = {
            'status': ['exact'],
            'type': ['exact'],
            'category': ['exact'],
            'subcategory': ['exact'],
        }