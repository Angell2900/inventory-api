from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, InventoryChangeViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'inventory-changes', InventoryChangeViewSet, basename='inventory-change')

urlpatterns = [
    path('', include(router.urls)),
]

