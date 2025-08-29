from django.shortcuts import render, redirect
from .models import SimpleUser
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings

def generate_tokens(user):
    refresh = RefreshToken.for_user(user)
    refresh['user_id'] = user.id  # вручную добавляем user_id
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }

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

                # Генерация токена
                tokens = generate_tokens(user)
                response = redirect('accounts:profile')
                response.set_cookie('access_token', tokens['access'], httponly=True)
                return response
        else:
            message = 'Заполните все поля!'

    return render(request, 'registr.html', {'message': message})

def login_page(request):
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()

        user = SimpleUser.objects.filter(email=email, username=username).first()
        if user:
            tokens = generate_tokens(user)
            response = redirect('accounts:profile')
            response.set_cookie('access_token', tokens['access'], httponly=True)
            return response
        else:
            message = 'Неверный email или имя'

    return render(request, 'login.html', {'message': message})

def profile_page(request):
    token = request.COOKIES.get('access_token')
    if not token:
        return redirect('accounts:login')

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')
        user = SimpleUser.objects.get(id=user_id)
    except Exception:
        return redirect('accounts:login')

    return render(request, 'profile.html', {'user': user})

def logout_page(request):
    response = redirect('accounts:login')
    response.delete_cookie('access_token')
    return response

def simple_view(request):
    token = request.COOKIES.get('access_token')
    if token:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            SimpleUser.objects.get(id=user_id)
            return redirect('accounts:profile')  # токен валиден
        except Exception:
            pass  # токен невалидный или пользователь не найден

    return redirect('accounts:register')  # нет токена или ошибка
