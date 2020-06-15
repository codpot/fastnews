from django.shortcuts import render


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
    context = {}
    return render(request, 'login.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)


def myaccount(request):
    context = {}
    return render(request, 'myaccount.html', context)
