from django.shortcuts import render
from django.views import View

from products.models import Category, Product


class HomeView(View):
    def get(self,request):
        categories= Category.objects.all()
        products= Product.objects.all()
        return render(request,'index.html',{
            'categories':categories,
            'products': products,
        })
