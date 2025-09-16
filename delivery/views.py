from django.shortcuts import render
from django.http import HttpResponse
from . models import Customer

# Create your views here.
def home(request):
    return render(request, 'index.html')

def open_signin(request):
    return render(request, 'sign_in.html')

def open_signup(request):
    return render(request, 'sign_up.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
    try:
        Customer.objects.get(username = username, password = password)
        if username == "Admin":
            return render(request, 'admin_home.html')
        else:
            return render(request, 'customer_home.html')
    except Customer.DoesNotExist:
        return render(request, 'fail.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

    try:
        Customer.objects.get(username = username)
        return HttpResponse("Duplicate Usernames are not allowed")
    except:
        Customer.objects.create(username = username,
                                password = password,
                                email = email,
                                contact = contact,
                                address = address)
        return render(request, 'sign_in.html')
    
def add_restro_page(request):
    return render(request, 'add_restro.html')