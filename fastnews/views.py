from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import Article, Comment, Debate, Settlement, User
from . import forms


def news_list(request, category):
    news = Article.objects.select_related('reporter')
    if category == 'politics':
        news = news.filter(category='PO')
    elif category == 'economy':
        news = news.filter(category='EC')
    elif category == 'social':
        news = news.filter(category='SO')
    elif category == 'life':
        news = news.filter(category='LI')
    elif category == 'world':
        news = news.filter(category='WO')
    elif category == 'it':
        news = news.filter(category='IT')
    news = news.order_by('-created_at')
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news_list.html', context)


def news_detail(request, id):
    news = Article.objects.select_related('reporter', 'debate').filter(id=id).first()
    if news is None:
        return render(request, 'alert.html', {'msg': '잘못된 뉴스입니다.'})
    news.views += 1
    news.save()
    if request.method == 'POST':
        form = forms.WriteComment(request.POST)
        if form.is_valid():
            if not 'user_id' in request.session:
                return render(request, 'alert.html', {'msg': '로그인이 필요합니다.'})
            Comment.objects.create(
                content=form.cleaned_data['content'],
                created_at=timezone.now(),
                debate_id=news.debate.id,
                user_id=request.session['user_id'],
            )
            news.debate.comment_cnt += 1
            news.debate.updated_at = timezone.now()
            news.debate.save()
    comments = Comment.objects.select_related('user').filter(debate_id=news.debate_id).order_by('-created_at')
    context = {
        'news': news,
        'debate': news.debate,
        'comments': comments,
    }
    return render(request, 'news_detail.html', context)


def debates_list(request):
    debate = Debate.objects.exclude(comment_cnt=0).order_by('-updated_at')
    if debate is None:
        return render(request, 'alert.html', {'msg': '잘못된 토론주제입니다.'})
    context = {
        'debates': debate
    }
    return render(request, 'debates_list.html', context)


def debates_recent(request):
    comments = Comment.objects.select_related('debate').select_related('user').order_by('-created_at')
    context = {
        'comments': comments,
    }
    return render(request, 'debates_recent.html', context)


def debates_detail(request, id):
    debate = Debate.objects.filter(id=id).first()
    if debate is None:
        return render(request, 'alert.html', {'msg': '잘못된 토론입니다.'})
    if request.method == 'POST':
        form = forms.WriteComment(request.POST)
        if form.is_valid():
            if not 'user_id' in request.session:
                return render(request, 'alert.html', {'msg': '로그인이 필요합니다.'})
            Comment.objects.create(
                content=form.cleaned_data['content'],
                created_at=timezone.now(),
                debate_id=id,
                user_id=request.session['user_id'],
            )
            debate.comment_cnt += 1
            debate.updated_at = timezone.now()
            debate.save()
    comments = Comment.objects.select_related('user').filter(debate_id=id).order_by('-created_at')
    context = {
        'debate': debate,
        'comments': comments
    }
    return render(request, 'debates_detail.html', context)


def write(request):
    if not 'user_id' in request.session:
        return render(request, 'alert.html', {'msg': '로그인이 필요합니다.', 'location': '/login/'})
    if request.method == 'POST':
        form = forms.WriteDebateForm(request.POST)
        if form.is_valid():
            is_exists = Debate.objects.filter(name=form.cleaned_data['debate_name'])
            if len(is_exists) != 0:
                return render(request, 'alert.html', {'msg': '이미 존재하는 주제입니다.'})
            Debate.objects.create(
                name=form.cleaned_data['debate_name'],
                comment_cnt=0,
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )
            return render(request, 'alert.html', {'msg': '토론 주제가 정상적으로 생성되었습니다.'})
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    debate = Debate.objects.all().order_by('-updated_at')
    context = {
        'debates': debate
    }
    return render(request, 'write.html', context)


def write_article(request, id):
    if not 'user_id' in request.session:
        return render(request, 'alert.html', {'msg': '로그인이 필요합니다.', 'location': '/login/'})
    debate = Debate.objects.filter(id=id).first()
    if debate is None:
        return render(request, 'alert.html', {'msg': '잘못된 토론주제입니다.'})
    if request.method == 'POST':
        form = forms.WriteArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.create(
                category=form.cleaned_data['category'],
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                views=0,
                created_at=timezone.now(),
                debate=debate,
                reporter_id=request.session['user_id'],
            )
            debate.updated_at = timezone.now()
            debate.save()
            return render(request, 'alert.html', {'msg': '기사가 작성되었습니다.', 'location': '/news/%s' % article.id})
        return render(request, 'alert.html', {'msg': '입력이 잘못되었습니다.'})
    context = {
        'debate_id': id,
    }
    return render(request, 'write_article.html', context)


def settlement(request):
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
    return render(request, 'settlement.html', context)


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
            if form.cleaned_data['password'] != form.cleaned_data['password_re']:
                return render(request, 'alert.html', {'msg': '비밀번호가 일치하지 않습니다.'})
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
