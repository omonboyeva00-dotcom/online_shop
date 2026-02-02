from django.urls import path

# from config.urls import urlpatterns

from . import views


urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('products', views.ProductView.as_view(), name='products'),
    path('product/<int:id>/detail',views.ProductDetailView.as_view(),name='product_detail')
]