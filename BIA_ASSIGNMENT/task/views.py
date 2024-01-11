from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages


def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect('home')  # Superuser, redirect to the 'home' page
                else:
                    return redirect('home')  
                
            else:
                if username == '' or password == '':
                    messages.error(
                        request, message='Please Enter Username and Passowrd Correctly')
                else:
                    messages.error(
                        request, message='Username or Password not correct')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request,'home.html')

# TASK1
def hello(request):
    html_content = """
    <html>
    <head>
        <title>Hello, Django!</title>
    </head>
    <body style="background-color: #f4f4f4; text-align: center; padding: 50px;">
        <div style="width: 300px; margin: auto; background: linear-gradient(to right, #0575E6, #021B79); padding: 20px; border-radius: 10px;">
            <h1 style="color: #fff;">Hello, Django!</h1>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def movie(request):
    return render(request,'movie.html')