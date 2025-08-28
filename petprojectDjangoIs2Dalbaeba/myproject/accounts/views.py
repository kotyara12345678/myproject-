from django.shortcuts import render, redirect
from .models import SimpleUser

def registr_page(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username and email:
            if SimpleUser.objects.filter(email=email).exists():
                message = 'Такой email уже зарегистрирован!'
            else:
                user = SimpleUser(username=username, email=email)
                user.save()

                request.session['user_id'] = user.id
                return redirect('accounts:profile')
        else:
            message = 'Заполните все поля!'

    return render(request, 'registr.html', {'message': message})


def login_page(request):
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')

        try:
            user = SimpleUser.objects.get(email=email, username=username)
            request.session['user_id'] = user.id
            return redirect('accounts:profile')
        except SimpleUser.DoesNotExist:
            message = 'Неверный email или имя'

    return render(request, 'login.html', {'message': message})


def profile_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('accounts:login')
    user = SimpleUser.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})


def logout_page(request):
    request.session.flush()
    return redirect('accounts:login')