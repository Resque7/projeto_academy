import django.contrib.auth.views
from django.urls import path

import academy
from academy.accounts import views
from academy.accounts.views import do_login, do_logout

urlpatterns =[
    path('', academy.accounts.views.dashboard, name='dashboard'),
    path('entrar/', views.login_screen, name='login'),
    path('do_login', do_login, name="do_login"),
    path('do_logout', do_logout, name="do_logout"),
    path('cadastre-se/', academy.accounts.views.register, name='register'),
    path('nova-senha/', academy.accounts.views.password_reset, name='password_reset'),
    path('confirmar-nova-senha/(str:<key>)/', academy.accounts.views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', academy.accounts.views.edit, name='edit'),
    path('editar-senha/', academy.accounts.views.edit_password, name='edit_password'),
]
