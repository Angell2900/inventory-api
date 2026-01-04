from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import Category, Product, InventoryChange
from .serializers import CategorySerializer, ProductSerializer, InventoryChangeSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'quantity', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Product.objects.all()
        
        # Filter by low stock
        low_stock = self.request.query_params.get('low_stock', None)
        if low_stock is not None:
            low_stock_threshold = int(low_stock)
            queryset = queryset.filter(quantity__lt=low_stock_threshold)
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        
        if min_price is not None:
            queryset = queryset.filter(price__gte=float(min_price))
        if max_price is not None:
            queryset = queryset.filter(price__lte=float(max_price))
        
        return queryset

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class InventoryChangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryChange.objects.all()
    serializer_class = InventoryChangeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['product']
    ordering = ['-changed_at']

