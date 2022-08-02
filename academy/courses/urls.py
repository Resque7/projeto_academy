from django.urls import path

from academy.courses import views

urlpatterns =[
    path('index/', views.index, name='index'),
    #path('<int:pk>/', views.details, name='details'),
    path('<str:slug>/', views.details, name='details'),
    path('<str:slug>/inscrição/', views.enrollment, name='enrollment'),
    path('<str:slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment'),
    path('<str:slug>/anuncios/', views.announcements, name='announcements'),
    path('<str:slug>/anuncios/<int:pk>/', views.show_announcement, name='show_announcement'),
    path('<str:slug>/aulas/', views.lessons, name='lessons'),
    path('<str:slug>/aulas/<int:pk>/', views.lesson, name='lesson'),
    path('<str:slug>/materiais/<int:pk>/', views.material, name='material'),
]
