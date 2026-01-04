from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, DecimalValidator


class Category(models.Model):
    """Category model for grouping products."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model with inventory tracking."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.quantity} in stock)"


class InventoryChange(models.Model):
    """Model to track all inventory changes."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_changes')
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    changed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    change_reason = models.CharField(max_length=200, blank=True, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-changed_at']

    def __str__(self):
        return f"{self.product.name}: {self.old_quantity} -> {self.new_quantity}"

    @property
    def quantity_difference(self):
        return self.new_quantity - self.old_quantity

