from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import Article, ArticleLike, Attachment, \
    Comment, CommentLike, Debate, Notification, Settlement, User, UserSubscribe
from . import forms


def news_list(request, category):
    context = {}
    return render(request, 'news_list.html', context)


def news_detail(request, id):
    context = {}
    return render(request, 'news_detail.html', context)


def search(request):
    context = {}
    return render(request, 'search.html', context)


def debates_list(request):
    context = {}
    return render(request, 'debates_list.html', context)


def debates_detail(request, id):
    context = {}
    return render(request, 'debates_list.html', context)


def notifications_list(request):
    context = {}
    return render(request, 'notifications_list.html', context)


def notifications_detail(request, id):
    context = {}
    return render(request, 'notifications_detail.html', context)


def likes_list(request):
    context = {}
    return render(request, 'likes_list.html', context)


def write(request):
    context = {}
    return render(request, 'write.html', context)


def settlement_list(request):
    context = {}
    return render(request, 'settlement_list.html', context)


def settlement_detail(request, id):
    context = {}
    return render(request, 'settlement_detail.html', context)


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email'])
            if len(user) != 1:
                return render(request, 'alert.html', {'msg': '이메일 주소 혹은 비밀번호가 일치하지 않습니다.'})
            if check_password(form.cleaned_data['password'], user[0].password) is False:
                return render(request, 'alert.html', {'msg': '이메일 주소 혹은 비밀번호가 일치하지 않습니다.'})
            request.session['user_id'] = user[0].id
            return HttpResponseRedirect('/')
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            is_exists = User.objects.filter(email=form.cleaned_data['email'])
            if len(is_exists) != 0:
                return render(request, 'alert.html', {'msg': '이미 사용중인 이메일 주소 입니다.'})
            User.objects.create(
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),
                nickname=form.cleaned_data['nickname'],
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )
            return render(request, 'alert.html', {'msg': '성공적으로 가입되었습니다.', 'location': '/login/'})
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    return render(request, 'register.html')


def myaccount(request):
    context = {}
    return render(request, 'myaccount.html', context)
