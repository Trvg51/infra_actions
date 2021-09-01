from django.http import HttpResponse


def index(request):
    return HttpResponse('А вот и новый билд подкатил =)')


def second_page(request):
    return HttpResponse('А это вторая страница!')
