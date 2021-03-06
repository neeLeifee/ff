from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, LoginForm, ChangeProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('base')
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', 'base')
                return redirect(redirect_url)
            else:
                messages.error(request, "Username Or Password is incorrect!!",
                               extra_tags='alert alert-warning alert-dismissible fade show')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required
def show_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


def change_profile(request):
    if request.method == "POST":
        form = ChangeProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('../profile')
        else:
            form = ChangeProfileForm(instance=request.user)
            args = {'form': form}
            return render(request, 'change_profile.html', args)
    else:
        form = ChangeProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'change_profile.html', args)