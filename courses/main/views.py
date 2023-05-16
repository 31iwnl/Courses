import time

from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm, ProductForm, UpdateUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Basket, Role, Product, Receipt
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect("create_basket")
            return redirect("profile")
    else:
        form = LoginForm()
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/login.html", {"form": form})


def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    session_user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'main/edit_user.html', {'form': form, 'user': user, 'session_user': session_user})


@login_required
def user_logout(request):
    logout(request)
    return redirect('products')


def products(request):
    all_products = Product.objects.all().order_by('price')
    if request.user.is_authenticated:
        basket = Basket.objects.get(basket_id=request.user)
        context = {'all_products': all_products, 'basket': basket}
    else:
        context = {'all_products': all_products}
    return render(request, 'main/products.html', context)


def product_page(request, pk):
    product = Product.objects.get(id=pk)
    if request.user.is_authenticated:
        basket = Basket.objects.get(basket_id=request.user)
        context = {'product': product, 'basket': basket}
    else:
        context = {'product': product}
    return render(request, "main/product_page.html", context)


def create_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

        else:
            error = 'Check the data for correct input'

    form = ProductForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create_product.html', data)


def delete_product(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('products')
    else:
        return redirect('products')


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'main/update_product.html'
    fields = ['id', 'product_name', 'description', 'link', 'price']
    success_url = reverse_lazy("products")


def create_receipt(request):
    # basket = Basket.objects.get(basket_id=request.user)[0]
    basket = Basket.objects.get(basket_id=request.user)
    tot_price = basket.get_total_price()
    user_receipt = Receipt.objects.get_or_create(user_username=request.user, date=time.ctime(), total_price=tot_price)[0]
    product = Product.objects.all()
    check = basket.products_id.all()
    for pr in product:
        if pr in check:
            user_receipt.basket_products.add(pr)
    for pr in product:
        if pr in check:
            basket.products_id.remove(pr)
    return redirect('profile')


def profile(request):
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        receipts = Receipt.objects.all().order_by('-id')
        users = User.objects.all()
        user = User.objects.get(id=request.user.id)
        data = {'user': user, 'users': users, 'receipts': receipts}
        return render(request, 'main/profile.html', data)
    else:
        return redirect("login")


def add_to_basket(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user
    basket = Basket.objects.get_or_create(basket_id=user)[0]
    basket.products_id.add(product)
    basket.save()
    return redirect("products")


def remove_from_basket(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    basket = Basket.objects.get(basket_id=user)
    basket.products_id.remove(product)
    basket.save()
    return redirect("basket")


def remove_from_basket_products(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    basket = Basket.objects.get(basket_id=user)
    basket.products_id.remove(product)
    basket.save()
    return redirect("products")


def basket_view(request):
    if request.user.is_authenticated:
        basket_check = Basket.objects.all()
        flag = 0
        for bas in basket_check:
            if bas.basket_id == request.user:
                flag = 1
        if flag == 0:
            basket = 'Your cart is empty'
        else:
            basket = Basket.objects.get(basket_id=request.user)
        return render(request, "main/user_basket.html", {"basket": basket})
    else:
        return redirect("login")