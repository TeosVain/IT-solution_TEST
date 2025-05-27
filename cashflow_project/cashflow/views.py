from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView
)
from django.urls import reverse

from cashflow.forms import CashFlowForm, CategoryForm
from cashflow.models import CashFlowRecord, Category


class RedirectMixin:
    def get_success_url(self):
        return reverse('cashflow:list')


class CashFlowListView(ListView):
    model = CashFlowRecord
    paginate_by = 10


class CashFlowCreateView(RedirectMixin, CreateView):
    model = CashFlowRecord
    form_class = CashFlowForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CashFlowUpdateView(RedirectMixin, UpdateView):
    model = CashFlowRecord
    form_class = CashFlowForm


class CashFlowDeleteView(RedirectMixin, DeleteView):
    model = CashFlowRecord
    template_name = 'cashflow/cashflowrecord_form.html'


class CategoryCreateView(RedirectMixin, CreateView):
    model = Category
    form_class = CategoryForm

    def form_valid(self, form):
        return super().form_valid(form)
