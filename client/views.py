from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from client.models import FoodItems, Images, Clients

###########################################
# HOMEPAGE AND CLIENT SIDE VIEWS
def home(request):
    data = ""
    return render(request, 'index.html', {'data': data})

def food(request):
    all_foods = FoodItems.objects.all()
    if request.session.get('user'):
        print(request.session.get('user'))
        return render(request, 'foods.html', {'data': all_foods, 'user': request.session.get('user')})
    else:
        user = "USER"
        return render(request, 'foods.html', {'data': all_foods, 'user': user})
    
def contact(request):
    data = ""
    return render(request, 'contact.html', {'data': data})

def checkout(request):
    data = ""
    return render(request, 'checkout.html', {'data': data})

# HOMEPAGE AND CLIENT SIDEW VIWES DONE
###########################################

###########################################
# AUTHENTICATION VIEWS HERE
def login(request):
    data = ""
    return render(request, 'login.html', {'data': data})

def verifylogin(request):
    post_data = request.POST
    print(post_data)
    if 'user' and 'pass' in post_data:
        user = authenticate(
            request,
            username=post_data['user'],
            password=post_data['pass']
        ) 
        if user is None:
            return redirect('login')
        elif user.is_superuser:
            auth_login(request, user)
            request.session['user'] = post_data['user']
            request.session['type'] = "admin"
            return redirect('addfood')
        else:
            auth_login(request, user)
            request.session['user'] = post_data['user']
            request.session['type'] = "client"
            return redirect('food')
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('home')

def register(request):
    data = ""
    print(request.POST)
    return render(request, 'register.html', {'data': data})

def saveuser(request):
    print(request.POST)
    post_data = request.POST
    if post_data['password'] == post_data['conf_pass']:
        user = User.objects.create_user(post_data['phone'], post_data['email'], post_data['password'])
        client = Clients(
            user = user,
            phone = post_data['phone'],
            name = post_data['name']
        )
        client.save()    
        return redirect('home')
    else:
        return redirect('register')

# AUTHENTICATION VIEWS DONE
###########################################

###########################################
# ALL ADMIN SIDE VIEWS
@login_required(login_url='/login/')
def addFood(request):
    if request.session.get('type'):
        user_type = request.session.get('type')
        print(user_type)
        if user_type == "admin":
            data = ""
            return render(request, 'addfood.html', {'data': data})
        else:
            return redirect('home')


def savefood(request):
    print(request.POST)
    print(request.FILES)

    post_data = request.POST
    img_data = request.FILES

    item = FoodItems(
        name = post_data['name'],
        price = post_data['price'],
        qty = post_data['qty'],
        description = post_data['description'],
        time = post_data['time'],
        status = post_data['status']
    )
    item.save() 

    if 'img' in img_data:
        for f in img_data.getlist('img'):
            img = Images(
                food = item,
                images = f
            )
            img.save()
    
    return redirect('foodlist')

@login_required(login_url="/login/")
def orders(request):
    if request.session.get('type'):
        user_type = request.session.get('type')
        if user_type == "admin":
            data = ""
            return render(request, 'order.html', {'data': data})
        else:
            return redirect('home')
    

@login_required(login_url="/login/")
def foodlist(request):
    if request.session.get('type'):
        user_type = request.session.get('type')
        if user_type == "admin":
            all_foods = FoodItems.objects.all()
            print(all_foods)
            return render(request, 'foodlist.html', {'data': all_foods})
        else:
            return redirect('home')
    

@login_required(login_url="/login/")
def users(request):
    if request.session.get('type'):
        user_type = request.session.get('type')
        if user_type == "admin":
            all_users = Clients.objects.all()
            print(all_users)
            return render(request, 'users.html', {'data': all_users})
        else:
            return redirect('home')

# ADMIN VIEWS DONE
###########################################


###########################################
# helper and misc functions
def checkadmin(name):
    if name == "admin":
        return "admin"
    else:
        return "client"


###########################################