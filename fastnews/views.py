from django.http import HttpResponse


def news_list(request, category):
    return HttpResponse('News')


def news_detail(request, id):
    return HttpResponse('News')


def debates_list(request):
    return HttpResponse('Debates')


def debates_detail(request, id):
    return HttpResponse('Debates')


def notifications_list(request):
    return HttpResponse('Notifications')


def notifications_detail(request, id):
    return HttpResponse('Notifications')


def likes_list(request):
    return HttpResponse('Likes')


def likes_detail(request, id):
    return HttpResponse('Likes')


def write(request):
    return HttpResponse('Write')


def settlement_list(request):
    return HttpResponse('Settlement')


def settlement_detail(request, id):
    return HttpResponse('Settlement')


def login(request):
    return HttpResponse('Login')


def register(request):
    return HttpResponse('Register')


def myaccount(request):
    return HttpResponse('My Account')
