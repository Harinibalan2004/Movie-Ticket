from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'Tickets/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrderForm()
    return render(request, 'Tickets/add_order.html', {'form': form})
