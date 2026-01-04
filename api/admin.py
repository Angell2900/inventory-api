from django.contrib import admin
from .models import Category, Product, InventoryChange


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price', 'updated_by', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at', 'updated_by')
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'quantity')
        }),
        ('Audit Information', {
            'fields': ('created_at', 'updated_at', 'updated_by'),
            'classes': ('collapse',)
        }),
    )


@admin.register(InventoryChange)
class InventoryChangeAdmin(admin.ModelAdmin):
    list_display = ('product', 'old_quantity', 'new_quantity', 'quantity_difference', 'changed_by', 'changed_at')
    list_filter = ('changed_at', 'product')
    search_fields = ('product__name',)
    readonly_fields = ('product', 'old_quantity', 'new_quantity', 'changed_by', 'changed_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

