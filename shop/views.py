from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Under development")


def search(request):
    return HttpResponse("Under development")


def tracker(request):
    return HttpResponse("Under development")


def productView(request):
    return HttpResponse("Under development")


def checkout(request):
    return HttpResponse("Under development")
