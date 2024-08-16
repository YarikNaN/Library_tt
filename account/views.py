from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, SvRegistrationForm
from django.core.cache import cache
from django.contrib.auth.models import Group
from .models import Reader

def custom_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    # Проверяем, состоит ли пользователь в группе Librarians
                    if user.groups.filter(name='Librarians').exists():
                        return redirect('debt')  # Редирект на debt для Librarians
                    elif user.groups.filter(name='Readers').exists():
                        return redirect('books')  # Редирект на books
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save()  # Тут false было когда в представлении обрабатывал, теперь в форме обрабатывается
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            readers_group = Group.objects.get(name='Readers')
            readers_group.user_set.add(new_user)
            # new_user.save() в форме сохранение теперь

            # Now create a Reader instance linked to the new User
            # Reader.objects.create(
            #     user=new_user,
            #     name=user_form.cleaned_data['name'],
            #     surname=user_form.cleaned_data['surname'],
            #     address=user_form.cleaned_data['address']
            # )

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})



def svregister(request):
    if request.method == 'POST':
        user_form = SvRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save()  # Тут false было когда в представлении обрабатывал, теперь в форме обрабатывается
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            librarians_group = Group.objects.get(name='Librarians')
            librarians_group.user_set.add(new_user)
            # new_user.save() в форме сохранение теперь

            # Now create a Reader instance linked to the new User
            # Reader.objects.create(
            #     user=new_user,
            #     name=user_form.cleaned_data['name'],
            #     surname=user_form.cleaned_data['surname'],
            #     address=user_form.cleaned_data['address']
            # )

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = SvRegistrationForm()
    return render(request, 'account/svregister.html', {'user_form': user_form})



def dashboard(request):
    return render(request, 'account/dashboard.html')





