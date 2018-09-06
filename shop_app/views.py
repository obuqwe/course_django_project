from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .serializers import ProductSerializer
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

class OrderFormView(LoginRequiredMixin,generic.CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = '/'
    fields = ['customer_name', 'customer_phone']

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        form.instance.user = user
        form.instance.product = product
        return super().form_valid(form)

class SecretAdminView(UserPassesTestMixin, generic.TemplateView):
    template_name = 'memes.html'

    def test_func(self):
        return self.request.user.is_superuser

class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    #permission_classes = (permissions.IsAdminUser, )