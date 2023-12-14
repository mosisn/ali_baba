from django.http.response import HttpResponse, JsonResponse


def greeting(request):
    return HttpResponse('welcome to my website!')


def about(request):
    return HttpResponse('here is about page!')


def contact(request):
    return HttpResponse('contact mostafa.saneisn@gmail.com')

