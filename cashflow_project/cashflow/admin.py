from django.contrib import admin

from cashflow.models import CashFlowRecord, Category, Status, Subcategory, Type


@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', 'author')
    list_filter = ('status', 'type', 'category', 'subcategory')
    search_fields = ('comment',)
    date_hierarchy = 'date'
    ordering = ('-date',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name',)
    list_filter = ('type',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
