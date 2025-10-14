from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
{%- if cookiecutter.use_djstripe == 'y' -%}
import stripe
from django.conf import settings
from djstripe.models import Product, Price, Customer
from django.http import JsonResponse
{%- endif -%}

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

{%- if cookiecutter.use_djstripe == 'y' -%}
@login_required
def subscription_view(request):
    # Get active products
    products = Product.objects.filter(active=True)
    customer, created = Customer.objects.get_or_create(subscriber=request.user)
    subscriptions = customer.subscriptions.filter(status='active')
    return render(request, 'subscription.html', {
        'products': products,
        'subscriptions': subscriptions,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })

@login_required
def create_checkout_session(request, price_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        price = Price.objects.get(id=price_id)
        customer, created = Customer.objects.get_or_create(subscriber=request.user)
        checkout_session = stripe.checkout.Session.create(
            customer=customer.id,
            payment_method_types=['card'],
            line_items=[{
                'price': price.id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=request.build_absolute_uri('/profile/'),
            cancel_url=request.build_absolute_uri('/subscription/'),
        )
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
{%- endif -%}

# Create your views here.
