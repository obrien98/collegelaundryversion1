from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from .models import Profile



def home(request):
    return HttpResponse('Welcome')


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm


def home(request):
    if request.user.profile.role == 'WORKER':
        users_with_same_university_as_worker = Profile.objects.filter(university=request.user.profile.university, role = "CUSTOMER")
        #above line gets all customers who share the same university as the worker viewing the page


        return render(request, 'core/home.html', {'user': request.user, 'customers': users_with_same_university_as_worker})
        #abovee passes the current users infor as 'user' and a list of users who want their laundry done as 'customers' to the template

    else:
        render(request, 'core/home.html', {'user': request.user})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.university = form.cleaned_data.get('university')
            user.profile.role = form.cleaned_data.get('role')
            user.save()  # explicitly save custom fields not in User model
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)  # login user after signup
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


from django.shortcuts import render

# Create your views here.
