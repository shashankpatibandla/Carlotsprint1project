from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def abc(request):
    return render(request, 'carlot/product/abc.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'registration/password_reset_complete.html', {'carlot': password_reset_complete})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def password_reset(request):
    return render(request, 'registration/password_reset_form.html',
    {'carlot': password_reset})


def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html',
    {'carlot': password_reset_confirm})

def password_reset_email(request):
    return render(request, 'registration/password_reset_email.html',
    {'carlot': password_reset_email})

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html',
    {'carlot': password_reset_complete})

@login_required()
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'carlot/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

@login_required()
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'carlot/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
