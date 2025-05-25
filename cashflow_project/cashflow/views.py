from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView
)
from django.urls import reverse

from cashflow.forms import CashFlowForm
from cashflow.models import CashFlowRecord

class CashFlowListView(ListView):
    model = CashFlowRecord


class CashFlowCreateView(CreateView):
    model = CashFlowRecord
    form_class = CashFlowForm


class CashFlowUpdateView(UpdateView):
    model = CashFlowRecord
    form_class = CashFlowForm


class CashFlowDeleteView(DeleteView):
    model = CashFlowRecord
