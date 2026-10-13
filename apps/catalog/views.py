from django.shortcuts import get_object_or_404, render

from apps.cart.forms import CartAddProductForm

from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # TODO: search, sorting and pagination - see TASKS.md (BE-2).

    return render(
        request,
        "catalog/product_list.html",
        {"category": category, "categories": categories, "products": products},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(
        request,
        "catalog/product_detail.html",
        {"product": product, "cart_product_form": CartAddProductForm()},
    )
