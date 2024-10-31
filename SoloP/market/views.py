from django.shortcuts import render, HttpResponse, redirect
from .models import MarketProduct
from .models import User
from django.contrib.auth.hashers import make_password
from django.views import View

# Create your views here.
def home(request):
  return render(request, 'market/index.html')

def market(request):
  products = MarketProduct.objects.all()
  context = {
    'products': products
  }
  return render(request, 'Market/market.html', context)

def cart(request):
  return render(request, 'Market/cart.html')

def about(request):
  return render(request, 'Market/about.html')

def login(request):
  return render(request, 'Market/login.html')

def signup(request):
  return render(request, 'Market/signup.html')





# View for listing all users
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})

# View for creating a new user
class UserCreateView(View):
    def get(self, request):
        return render(request, 'user_create.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Create and save a new user with hashed password
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=make_password(password),
            role=role
        )
        user.save()

        return redirect('login')

