from django.shortcuts import render
from django.views import generic
from .models import Product, Category, Order

class ProductListView(generic.ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product

class CategoryList(generic.ListView):
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    model = Category

class CategoryDetail(generic.DetailView):
    template_name = 'category_detail.html'
    model = Category

class ProductCreate(generic.CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'

class OrderFormView(generic.CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = '/'
    fields = ['customer_name', 'customer_phone']

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)