from django.shortcuts import render, HttpResponse
from .models import Product
from math import ceil


def index(request):

    products = Product.objects.all()

    n = len(products)

    num_of_slide = ceil(n/4)

    params = {'num_of_slide': num_of_slide, 'range': range(1,num_of_slide), 'product': products}

    return render(request, 'shop/index.html', params)


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
