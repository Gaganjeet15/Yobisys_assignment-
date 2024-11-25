from django.contrib import admin
from django.urls import path
from tenants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:tenant_id>/', views.product_list, name='product_list'),
]
