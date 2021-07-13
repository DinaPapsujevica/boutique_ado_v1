from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 
        'pk_test_51J9wNlJAfoHqVtfAXRA8Cqj05RLpaWjbFmdUlA2BsKRVNxGmK6OSnisP6sZlU4daaeDQI7gbpKss2p4cbJVaJNib00nvys1Ziw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)