from django.shortcuts import render, HttpResponse
from .models import Product
from math import ceil


def index(request):

    # products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}

    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def productView(request):
    return render(request, 'shop/prodView.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
