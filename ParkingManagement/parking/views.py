from django.shortcuts import render, redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
from .models import Category
from .models import AddVehicle

from .forms import CategoryForm
from .forms import AddVehicleForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("User Name Exists! Try Another Username")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print("Email is already taken, Try another One")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('login')
        else:
            print('Password did not Matched----!')
            return redirect('register')
    else:
        return render(request, 'login.html')

def login(request):
    if request.method == 'POST':  #(POST == POST)True
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("Login Successfully")
            return redirect('dashboard')
        else:
            print("You provide Invalid Details")
            return redirect('login')
    else:
        return render(request, 'login.html')
@login_required(login_url='login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("logged out from Website")
        return redirect('login')
@login_required(login_url='login')
def DisplayItems(request):
    display = Category.objects.all()

    page_num = request.GET.get("page")  # Total number of pages required
    paginator = Paginator(display, 5)

    try:
        display = paginator.page(page_num)  # Total 5-+ Products load --> each page 3 =>2 pages(1,2)

    except PageNotAnInteger:
        display = paginator.page(1)  # its show first page only which is 127.0.0.1:8000

    except EmptyPage:  # If the page is empty (there is no product this except block will execute)
        display = paginator.page(paginator.num_pages)

    context = {'display': display}

    return render(request, 'Category.html', context)
@login_required(login_url='login')
def ManageVehicle(request):
    display1 = AddVehicle.objects.all()

    page_num = request.GET.get("page")  # Total number of pages required
    paginator = Paginator(display1, 5)

    try:
        display1 = paginator.page(page_num)  # Total 5-+ Products load --> each page 3 =>2 pages(1,2)

    except PageNotAnInteger:
        display1 = paginator.page(1)  # its show first page only which is 127.0.0.1:8000

    except EmptyPage:  # If the page is empty (there is no product this except block will execute)
        display1 = paginator.page(paginator.num_pages)


    context = {'display1': display1}

    return render(request, 'manage.html', context)
@login_required(login_url='login')
def addCategory(request):
    form = CategoryForm()

    if request.method == "POST":        # post == Post ==> True
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Display')

    context = {'form': form}
    return render(request, 'forms.html', context)

@login_required(login_url='login')
def Vehicleadd(request):
    form = AddVehicleForm()

    if request.method == "POST":        # post == Post ==> True
        form = AddVehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Manage')

    context = {'form': form}
    return render(request, 'forms.html', context)


def delete(request, pk):
    displey = Category.objects.get(id=pk)
    displey.delete()

    return redirect('Display')

def update(request, pk):
    displey1 = Category.objects.get(id=pk)
    form = CategoryForm(instance=displey1)

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=displey1)
        if form.is_valid():
            form.save()

            return redirect('Display')

    context = {'form': form}

    return render(request, 'form1.html', context)

def deactive(req,pk):
    category = Category.objects.get(id=pk)
    category.status = False
    category.save()
    return redirect('Display')

def active(req,pk):
    category = Category.objects.get(id=pk)
    category.status = True
    category.save()
    return redirect('Display')

def leaved(req,pk):
    category1 = AddVehicle.objects.get(id=pk)
    category1.status = False
    category1.save()
    return redirect('Manage')

def parked(req,pk):
    category1 = AddVehicle.objects.get(id=pk)
    category1.status = True
    category1.save()
    return redirect('Manage')

@login_required(login_url='login')
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query: # condition is true
            display1 = AddVehicle.objects.filter(vehicle_no__contains = query)
            return render(request, 'search.html',{'display1':display1})
        else:
             print("No information show based on the search")
             return render(request, 'search.html',{})

def manageSearch(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query: # condition is true
            display1 = AddVehicle.objects.filter(vehicle_no__contains = query)
            return render(request, 'manage.html',{'display1':display1})
        else:
            print("No information show based on the search")
            return render(request, 'manage.html',{})

def categorySearch(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query: # condition is true
            display = Category.objects.filter(parking_area_no__contains = query)
            return render(request, 'category.html',{'display': display})
        else:
            print("No information show based on the search")
            return render(request, 'category.html',{})

@login_required(login_url='login')
def dashboard(request):

    parked_count = AddVehicle.objects.filter(status=True).count()
    departed_count = AddVehicle.objects.filter(status=False).count()
    category_count = Category.objects.filter(status=True).count()
    records_count = AddVehicle.objects.all().count()
    total_earnings = AddVehicle.objects.filter(status=True).aggregate(Sum('parking_charge'))["parking_charge__sum"]


    context = {'parked_count': parked_count,
               'departed_count': departed_count,
               'category_count': category_count,
               'records_count': records_count,
               'total_earnings': total_earnings,
               }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def reports(request):
    return render(request, 'reports.html')

@login_required(login_url='login')
def accountsettings(request):
    return render(request, 'accountsettings.html')

