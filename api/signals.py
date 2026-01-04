from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Product, InventoryChange


@receiver(pre_save, sender=Product)
def capture_old_quantity(sender, instance, **kwargs):
    """Capture the old quantity before saving."""
    if instance.pk:
        try:
            old_instance = Product.objects.get(pk=instance.pk)
            instance._old_quantity = old_instance.quantity
        except Product.DoesNotExist:
            instance._old_quantity = None
    else:
        instance._old_quantity = None


@receiver(post_save, sender=Product)
def log_inventory_change(sender, instance, created, **kwargs):
    """Log any quantity changes to InventoryChange model."""
    if not created:
        old_quantity = getattr(instance, '_old_quantity', None)
        
        if old_quantity is not None and old_quantity != instance.quantity:
            InventoryChange.objects.create(
                product=instance,
                old_quantity=old_quantity,
                new_quantity=instance.quantity,
                changed_by=instance.updated_by,
            )
