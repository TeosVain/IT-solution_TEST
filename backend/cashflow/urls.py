from django.urls import include, path

from cashflow.views import (
    CategoryCreateView, CategoryDeleteView, CategoryListView,
    CategoryUpdateView,
    RecordCreateView, RecordDeleteView, RecordListView, RecordUpdateView,
    StatusCreateView, StatusDeleteView, StatusListView, StatusUpdateView,
    SubcategoryCreateView, SubcategoryDeleteView, SubcategoryListView,
    SubcategoryUpdateView,
    TypeCreateView, TypeDeleteView, TypeListView, TypeUpdateView,
    load_categories, load_subcategories
)


app_name = 'cashflow'

record_patterns = [
    path('', RecordListView.as_view(), name='list'),
    path('create/', RecordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RecordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
]

status_patterns = [
    path('', StatusListView.as_view(), name='status_list'),
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('update/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
    path('delete/<int:pk>/', StatusDeleteView.as_view(), name='status_delete'),
]

type_patterns = [
    path('', TypeListView.as_view(), name='type_list'),
    path('create/', TypeCreateView.as_view(), name='type_create'),
    path('update/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
    path('delete/<int:pk>/', TypeDeleteView.as_view(), name='type_delete'),
]

category_patterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path(
        'update/<int:pk>/',
        CategoryUpdateView.as_view(), name='category_update'
    ),
    path(
        'delete/<int:pk>/',
        CategoryDeleteView.as_view(), name='category_delete'
    ),
]

subcategory_patterns = [
    path('', SubcategoryListView.as_view(), name='subcategory_list'),
    path(
        'create/', SubcategoryCreateView.as_view(), name='subcategory_create'
    ),
    path(
        'update/<int:pk>/',
        SubcategoryUpdateView.as_view(), name='subcategory_update'
    ),
    path(
        'delete/<int:pk>/',
        SubcategoryDeleteView.as_view(), name='subcategory_delete'
    ),
]

urlpatterns = [
    path('', include(record_patterns)),
    path('status/', include(status_patterns)),
    path('type/', include(type_patterns)),
    path('category/', include(category_patterns)),
    path('subcategory/', include(subcategory_patterns)),
    path(
        'ajax/load-subcategories/',
        load_subcategories, name='ajax_load_subcategories'
    ),
    path(
        'ajax/load-categories/',
        load_categories, name='ajax_load_categories'
    ),
]
