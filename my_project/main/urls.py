from django.urls import path
from . import views

urlpatterns = [
  path("", views.customer_list, name="customer_list"),
  path("customerform", views.add_customer, name="customer_form"),
  path("delete/<int:pk>", views.delete_customer, name="delete_customer"),
  path("search", views.search, name="search"),
]
