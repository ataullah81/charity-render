from django.urls import path

from charityfinderapp import views


urlpatterns = [
    path('charity', views.charity_func, name='charity'),
    path('index', views.index_func, name='index'),
    path('about', views.about_func, name='about'),
    path('donate', views.donate_func, name='donate'),
    path('search_charity', views.search_charity_func, name='search_charity'),
    path('contact', views.contact_func, name='contact'),
]
