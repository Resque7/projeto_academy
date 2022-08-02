from django.urls import path

from academy.courses import views

urlpatterns =[
    path('index/', views.index, name='index'),
    #path('<int:pk>/', views.details, name='details'),
    path('<str:slug>/', views.details, name='details'),
    path('<str:slug>/inscrição/', views.enrollment, name='enrollment'),
    path('<str:slug>/anuncios/', views.enrollment, name='announcements'),

]
