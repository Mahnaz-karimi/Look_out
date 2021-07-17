from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from person.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):  # register en bruger
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} has been createt!')  # f = format string
            return redirect('blog:blog-home')  # Hvis formen er valid så vil redirect til den url pattern for blogs
    else:
        form = UserRegisterForm()  # Hvis der er indtastet forkert information viser register side stadig
    return render(request, 'person/register.html', {'form': form})


@login_required  # krævs at brugeren har logget ind for at vise profile side.
def profile(request):  # se og opdatere profile
    if request.method == 'POST':  # Når der nogle data er blevet send for at gemmes
        u_form = UserUpdateForm(request.POST, instance=request.user)  # For at ændre users data som er navn og email
        # og som default vil stå navn for user ind i feltet
        p_form = ProfileUpdateForm(request.POST,  # For at ændre profiles billede
                                   request.FILES,  # Profile billede vil også stå på skærmen og man kan se billedes navn
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():  # Hvis formerne for (user og profile) er valid, gemmes ændringer
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('person:profile')

    else:  # hvis data ikke er blevet send
        u_form = UserUpdateForm(instance=request.user)  # instance gøre det at input er instance af en user
        p_form = ProfileUpdateForm(instance=request.user.profile)  # instance gøre det at input er instance af profile

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'person/profile.html', context)

