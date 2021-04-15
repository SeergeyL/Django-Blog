from django.shortcuts import render, redirect
from .forms import CreationForm, UserProfileForm


def signup(request):
    """
    Renders the registration page with user CreationForm based on the User model and UserProfileForm based
    on the UserProfile model which extends the basic User model.
    If user is already authenticated redirects to main page.
    """

    if request.user.is_authenticated:
        return redirect('index')

    user_form = CreationForm(request.POST or None)
    user_profile_form = UserProfileForm(request.POST or None, files=request.FILES or None)

    if request.method == "POST":
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save(commit=False)
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user

            user_form.save()
            user_profile_form.save()

            return redirect('login')

    return render(request, 'signup.html', {"forms": [user_form, user_profile_form]})