from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


def do_logout(request):
    logout(request)
    return redirect('login')


def login_screen(request):
    if request.user.is_authenticated:
        do_logout(request)
    return render(request, "accounts/login.html")


def do_login(request):
    if request.user.is_authenticated:
        return redirect('login')
    if len(request.POST) > 0:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return redirect('login')


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['sucess'] = True
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['sucess'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    form = EditAccountForm()
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['sucess'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['sucess'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


#A MENSAGEM DE DISPARAR O EMAIL NAO APARECE, ELA RELOGA A PÁGINA (ULTIMA AULA VISTA) def password_reset