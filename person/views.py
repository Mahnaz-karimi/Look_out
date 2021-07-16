from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from person.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} has been createt!')  # f = format string
            return redirect('blog:blog-home')  # hvis formen er valid så vil redirect til url pattern for blogs
    else:
        form = UserRegisterForm()  # hvis der er indtastet forkert information viser register side stadig
    return render(request, 'person/register.html', {'form': form})


@login_required  # krævs at brugeren har logget ind for at vise profile side.
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # vil ha user name og email
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)  # vil ha users billede så derfor bruger request.FILES
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('person:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)  # instance gøre det at input er instance af en user
        p_form = ProfileUpdateForm(instance=request.user.profile)  # instance gøre det at input er instance af profile

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'person/profile.html', context)
