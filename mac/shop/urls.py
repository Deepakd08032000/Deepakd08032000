
from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name="ShopHome"),
path("about/", views.about,name="AboutUs"),
path("contact/", views.contact, name="contactUs"),
path("tracker/", views.tracker, name="tracker"),
path("products/<int:myid>", views.productView, name="product"),
path("checkout/", views.checkout, name="checkout")
]
