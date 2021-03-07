from django.shortcuts import render
from django.contrib.auth.models import User
from .form import SignUpForm


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            user_instance = signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request, 'accounts/sign_up_complete.html')
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': signup_form.as_p})

''' 
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        return render(request, 'accounts/sign_up_complete.html')
    else:
        context_value = {'form': 'this is form'}
        return render(request, 'accounts/sign_up.html', context_value)'''