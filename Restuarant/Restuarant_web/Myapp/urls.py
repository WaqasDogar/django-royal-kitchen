from django.urls import path
from Myapp import views

urlpatterns = [

    path('',views.temp,name='index'),

    path('customers',views.savecustomer,name='customer'),

    path('updatecustomer/<str:pk>',views.updatecustomer,name='updatecustomer'),

    path('deletecustomer/<str:pk>',views.deletecustomer,name='deletecustomer'),
]