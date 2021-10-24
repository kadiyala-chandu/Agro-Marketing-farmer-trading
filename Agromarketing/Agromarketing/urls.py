"""Agromarketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from . import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.base_view),
    path('home/',views.home_view),
    path('about/',views.about_view),
    path('service/',views.service_view),
    path('logout/',views.logout_view),
    path('registration/',views.profile_reg,name='reg'),
    path('retailer/',views.retailer_reg,name='regs'),
    path('services/',views.service_view,name='ser'),
    path('register/',views.index,name='index'),
    path('products/',views.ProductView),
    path('accounts/',include('django.contrib.auth.urls')),
    path('allproducts/',views.AllProductsView),
    path("product/<slug:slug>/",views.ProductDetailView,name="productdetail"),
    path("add-to-cart-<int:pro_id>/",views.AddToCartView,name="addtocart")

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
