from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
def leo(request):
    return HttpResponse('LIGY')

# Create your views here.
def index(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']
        location = request.POST['location']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists.'})
        
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Create UserProfile object and set additional fields
        profile = UserProfile.objects.create(user=user, mobile=mobile, location=location)
        
        login(request, user)
    
        return redirect('user_login')
    return render(request, 'signup.html')
from .models import  UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product')  # Replace 'home' with your desired redirect URL
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'login.html')

def product(request):
    return render(request, 'shop.html')


from django.contrib.auth import logout
def user_logout(request):
    logout(request)
    return redirect('index')

def about(request):
    return render(request, 'about.html')


from .forms import ProductForm

from .models import Product


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=form.instance.pk)
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def contact(request):
    return render(request,"contact.html")