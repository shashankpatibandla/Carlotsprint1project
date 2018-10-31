from django.urls import path
from . import views as core_views
from django.conf.urls import url
from . import views

app_name = 'carlot'

urlpatterns = [
    path('',views.abc, name='abc'),
    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    url(r'^/password/$', views.change_password, name='change_password'),
]