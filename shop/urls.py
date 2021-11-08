from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("prodView/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]