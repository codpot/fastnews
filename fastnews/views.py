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
    if not 'user_id' in request.session:
        return render(request, 'alert.html', {'msg': '로그인이 필요합니다.', 'location': '/login/'})
    if request.method == 'POST':
        form = forms.SettlementForm(request.POST)
        if form.is_valid():
            Settlement.objects.filter(user__id=request.session['user_id'], received_at__isnull=True) \
                .update(bank_code=form.cleaned_data['bank_code'],
                        account_number=form.cleaned_data['account_number'],
                        real_name=form.cleaned_data['real_name'])
            return render(request, 'alert.html', {'msg': '수취인 정보가 정상적으로 등록되었습니다.'})
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    settlement = Settlement.objects.filter(user__id=request.session['user_id']).order_by('-id')
    context = {
        'settlement': settlement
    }
    return render(request, 'settlement_list.html', context)


def myaccount(request):
    if not 'user_id' in request.session:
        return render(request, 'alert.html', {'msg': '로그인이 필요합니다.', 'location': '/login/'})
    if request.method == 'POST':
        form = forms.MyAccountForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session['user_id'])
            if check_password(form.cleaned_data['now_password'], user.password) is False:
                return render(request, 'alert.html', {'msg': '현재 비밀번호가 올바르지 않습니다.'})
            if form.cleaned_data['new_password'] != '':
                user.password = make_password(form.cleaned_data['new_password'])
            user.nickname = form.cleaned_data['nickname']
            user.save()
            request.session['user_nickname'] = form.cleaned_data['nickname']
            return render(request, 'alert.html', {'msg': '성공적으로 수정되었습니다.'})
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    context = {
        'nickname': request.session['user_nickname']
    }
    return render(request, 'myaccount.html', context)


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
            request.session['user_nickname'] = user[0].nickname
            return HttpResponseRedirect('/')
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    return render(request, 'login.html')


def logout(request):
    del request.session['user_id']
    del request.session['user_nickname']
    return HttpResponseRedirect('/')


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
