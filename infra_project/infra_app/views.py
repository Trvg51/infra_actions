from django.http import HttpResponse


def index(request):
    return HttpResponse('Добавили месседжи в телегу!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
