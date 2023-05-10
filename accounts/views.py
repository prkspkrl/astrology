from django.shortcuts import render
from .forms import UserForm
from .models import User

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/register.html', context)

