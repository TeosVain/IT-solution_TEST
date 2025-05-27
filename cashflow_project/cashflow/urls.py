from django.urls import path

from cashflow.views import (
    CashFlowCreateView, CashFlowDeleteView,
    CashFlowListView, CashFlowUpdateView, CategoryCreateView
)

app_name = 'cashflow'

urlpatterns = [
    path('', CashFlowListView.as_view(), name='list'),
    path('create/', CashFlowCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CashFlowUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CashFlowDeleteView.as_view(), name='delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
