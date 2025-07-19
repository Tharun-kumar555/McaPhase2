from django.shortcuts import render, get_object_or_404,redirect
from .models import CanteenModel,Category,Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
import random
import qrcode
from io import BytesIO
import base64

def home(request):
    return render(request,'home.html')
    
def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    products = CanteenModel.objects.all()
    if category_id:
        products = CanteenModel.objects.filter(category_id=category_id)
    if query:
        products = products.filter(name__icontains=query)
        
    categories = Category.objects.all()
    context = {'products':products,'categories':categories}
    return render(request,'product_list.html',context)


def product_detail(request, pk):
    ob_product = get_object_or_404(CanteenModel, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def add_to_cart(request, pk):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    pk_str = str(pk)
    if pk_str in cart:
        cart[pk_str] += quantity
    else:
        cart[pk_str] = quantity
    request.session['cart'] = cart
    return redirect('product_list')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = CanteenModel.objects.filter(pk__in=product_ids)

    cart_items = []
    total_price = 0
    for product in products:
        quantity = cart.get(str(product.pk), 1)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    # Add this QR generation block
    upi_id = "srikarts@ybl"  # Replace with your real UPI ID
    upi_url = f"upi://pay?pa={upi_id}&pn=MotherTheresaCanteen&am={total_price}&cu=INR"

    qr = qrcode.make(upi_url)
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_base64 = base64.b64encode(qr_io.getvalue()).decode()

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'qr_code': qr_base64,
    })

@login_required
def place_order(request):
    cart = request.session.get('cart',[])
    if cart:
        order = Order.objects.create(user=request.user)
        order.products.set(cart)
        order.save()
        request.session['cart']=[]
        return redirect('order_history')
    return redirect('product_list')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html',{'orders':orders})

@csrf_exempt
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    pk_str = str(pk)
    if pk_str in cart:
        del cart[pk_str]
    request.session['cart'] = cart
    return redirect('view_cart')


@require_POST
def update_cart_quantity(request, pk):
    new_quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    pk_str = str(pk)

    if pk_str in cart:
        if new_quantity < 1:
            # Remove the item if they set quantity to 0
            del cart[pk_str]
        else:
            cart[pk_str] = new_quantity

    request.session['cart'] = cart
    return redirect('view_cart')

def download_bill_pdf(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for pk_str, quantity in cart.items():
        product = CanteenModel.objects.get(pk=pk_str)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    bill_number = f"MTIC-{random.randint(1000, 9999)}"

    # GENERATE QR Code for UPI
    upi_id = "srikarts@ybl"  # Replace this with your real UPI ID
    upi_url = f"upi://pay?pa={upi_id}&pn=MotherTheresaCanteen&am={total_price}&cu=INR"

    qr = qrcode.make(upi_url)
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_base64 = base64.b64encode(qr_io.getvalue()).decode()

    template_path = 'bill_pdf.html'
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'user': request.user,
        'bill_number': bill_number,
        'qr_code': qr_base64,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response
