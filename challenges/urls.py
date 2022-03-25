
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('<int:month>',views.m_int),
    path('<str:month>',views.m_challenges)
]