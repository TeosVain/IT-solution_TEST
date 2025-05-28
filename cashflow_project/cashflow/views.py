from django_filters.views import FilterView
from django.http import JsonResponse
from django.views.generic import (
    CreateView, DeleteView, ListView, UpdateView
)
from django.urls import reverse
from django.utils import timezone

from cashflow.filters import CashFlowRecordFilter
from cashflow.forms import (
    CashFlowForm, CategoryForm,
    StatusForm, SubcategoryForm, TypeForm
)
from cashflow.models import CashFlowRecord, Category, Status, Subcategory, Type


class RecordFormMixin:
    form_class = CashFlowForm
    template_name = 'cashflow/record/form.html'

    def get_success_url(self):
        return reverse('cashflow:list')


class StatusFormMixin:
    form_class = StatusForm
    template_name = 'cashflow/status/form.html'

    def get_success_url(self):
        return reverse('cashflow:status_list')


class CategoryFormMixin:
    form_class = CategoryForm
    template_name = 'cashflow/category/form.html'

    def get_success_url(self):
        return reverse('cashflow:category_list')


class SubcategoryFormMixin:
    form_class = SubcategoryForm
    template_name = 'cashflow/subcategory/form.html'

    def get_success_url(self):
        return reverse('cashflow:subcategory_list')


class TypeFormMixin:
    form_class = TypeForm
    template_name = 'cashflow/type/form.html'

    def get_success_url(self):
        return reverse('cashflow:type_list')


class RecordListView(FilterView):
    model = CashFlowRecord
    template_name = 'cashflow/record/list.html'
    paginate_by = 10
    filterset_class = CashFlowRecordFilter


class RecordCreateView(RecordFormMixin, CreateView):
    model = CashFlowRecord

    def form_valid(self, form):
        if not form.cleaned_data.get('date'):
            form.instance.date = timezone.now()
        return super().form_valid(form)


class RecordUpdateView(RecordFormMixin, UpdateView):
    model = CashFlowRecord

    def form_valid(self, form):
        if not form.cleaned_data.get('date'):
            form.instance.date = timezone.now()
        return super().form_valid(form)


class RecordDeleteView(DeleteView):
    model = CashFlowRecord
    template_name = 'cashflow/record/form.html'

    def get_success_url(self):
        return reverse('cashflow:list')


class StatusListView(ListView):
    model = Status
    paginate_by = 10
    template_name = 'cashflow/status/list.html'
    ordering = ['name']


class StatusCreateView(StatusFormMixin, CreateView):
    model = Status


class StatusUpdateView(StatusFormMixin, UpdateView):
    model = Status


class StatusDeleteView(StatusFormMixin, DeleteView):
    model = Status


class CategoryListView(ListView):
    model = Category
    paginate_by = 10
    template_name = 'cashflow/category/list.html'
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        type_id = self.request.GET.get('type')
        if type_id:
            qs = qs.filter(type_id=type_id)
        return qs
    

class CategoryCreateView(CategoryFormMixin, CreateView):
    model = Category


class CategoryUpdateView(CategoryFormMixin, UpdateView):
    model = Category


class CategoryDeleteView(CategoryFormMixin, DeleteView):
    model = Category


class SubcategoryListView(ListView):
    model = Subcategory
    paginate_by = 10
    template_name = 'cashflow/subcategory/list.html'
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs


class SubcategoryCreateView(SubcategoryFormMixin, CreateView):
    model = Subcategory


class SubcategoryUpdateView(SubcategoryFormMixin, UpdateView):
    model = Subcategory


class SubcategoryDeleteView(SubcategoryFormMixin, DeleteView):
    model = Subcategory


class TypeListView(ListView):
    model = Type
    paginate_by = 10
    template_name = 'cashflow/type/list.html'
    ordering = ['name']


class TypeCreateView(TypeFormMixin, CreateView):
    model = Type


class TypeUpdateView(TypeFormMixin, UpdateView):
    model = Type


class TypeDeleteView(TypeFormMixin, DeleteView):
    model = Type


def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)


def load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)
