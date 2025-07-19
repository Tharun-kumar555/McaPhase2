from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

def home(request):
    return render(request, 'shop/home.html')

def category_view(request, cat):
    items = Item.objects.filter(category=cat)
    
    # Convert slug to readable label
    category_labels = dict(Item._meta.get_field('category').choices)
    cat_label = category_labels.get(cat, cat)
    return render(request, 'shop/category.html', {
        'items': items,
        'cat': cat,
        'cat_label': cat_label
    })

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'shop/item_detail.html', {'item': item})

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for id_str, qty in cart.items():
        item = get_object_or_404(Item, id=int(id_str))
        items.append({'item': item, 'qty': qty, 'subtotal': item.price * qty})
        total += item.price * qty
    return render(request, 'shop/cart.html', {'items': items, 'total': total})

def checkout(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for id_str, qty in cart.items():
        item = get_object_or_404(Item, id=int(id_str))
        items.append({'item': item, 'qty': qty, 'subtotal': item.price * qty})
        total += item.price * qty

    if request.method == 'POST':
        # Simulate payment success and clear cart
        request.session['cart'] = {}
        return render(request, 'shop/success.html', {'total': total})

    return render(request, 'shop/checkout.html', {'items': items, 'total': total})
