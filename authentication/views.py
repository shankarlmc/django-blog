from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from post.models import Blog_Post
from .forms import updateUserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if username and email and password:
                if password == password2:
                    user = User.objects.create(
                        email=email,
                        username=username,
                        password=password,
                    )
                    user.save()
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "The two password fields didn'/t match.")
                    return HttpResponseRedirect('/register')
            else:
                messages.error(request, "All fields are required.")
                return HttpResponseRedirect('/register')
        return render(request, 'authentication/register.html')


def loginUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Username or password is incorrect.')
        return render(request, 'authentication/login.html')

@login_required(login_url="/login")
def userProfile(request):
    post_count = Blog_Post.objects.all().filter(author=request.user).count()
    user_posts = Blog_Post.objects.all().filter(author=request.user)

    if request.method == "POST":
        user_form = updateUserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully.')
            return HttpResponseRedirect('/profile')
    else:
        user_form = updateUserProfileForm(instance=request.user)
        
    context = {
        "post_count":post_count,
        "user_form":user_form,
        "user_posts":user_posts,
    }
    return render(request, 'authentication/profile.html', context)


@login_required(login_url="/login")
def logoutUser(request):
    logout(request)
    return redirect('/')