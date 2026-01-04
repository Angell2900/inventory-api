from rest_framework import serializers
from .models import Category, Product, InventoryChange


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_name', 'quantity', 'price', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_quantity(self, value):
        """Ensure quantity is not negative."""
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

    def validate_price(self, value):
        """Ensure price is not negative."""
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value


class InventoryChangeSerializer(serializers.ModelSerializer):
    """
    Serializer for InventoryChange model.
    
    Shows the history of inventory changes with:
    - Product name
    - Previous and new quantities
    - Who made the change and when
    - Quantity difference
    """
    product_name = serializers.CharField(source='product.name', read_only=True)
    changed_by_username = serializers.CharField(source='changed_by.username', read_only=True, allow_null=True)
    quantity_difference = serializers.SerializerMethodField()

    class Meta:
        model = InventoryChange
        fields = [
            'id',
            'product',
            'product_name',
            'old_quantity',
            'new_quantity',
            'quantity_difference',
            'changed_by',
            'changed_by_username',
            'change_reason',
            'changed_at',
        ]
        read_only_fields = ['id', 'changed_at', 'product_name', 'changed_by_username']

    def get_quantity_difference(self, obj):
        """Calculate and return the quantity difference."""
        return obj.quantity_difference
