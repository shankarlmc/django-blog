from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from post.models import Blog_Post
from .forms import updateUserProfileForm

# Create your views here.
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

def userProfile(request):
    post_count = Blog_Post.objects.all().filter(author=request.user).count()
    if request.method == "POST":
        user_form = updateUserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully.')
            return redirect('/profile')
    else:
        user_form = updateUserProfileForm(instance=request.user)
        
    context = {
        "post_count":post_count,
        "user_form":user_form,
    }
    return render(request, 'authentication/profile.html', context)



def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')