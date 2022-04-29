# users/urls.py
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/',
         LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('password_change_form/',
         PasswordChangeView.
         as_view(template_name='users/password_change_form.html'),
         name='password_change_form'),
    path('password_change_done/',
         PasswordChangeDoneView.
         as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password_reset_form/',
         PasswordResetView.
         as_view(template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.
         as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.
         as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_comfirm'),
    path('reset/done/',
         PasswordResetCompleteView.
         as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]