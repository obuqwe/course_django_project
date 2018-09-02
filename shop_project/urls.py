"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop_app import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('products/new/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/order', views.OrderFormView.as_view(), name='product_order'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
]
