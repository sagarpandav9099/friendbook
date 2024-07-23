from django.urls import path
from .views import registration,email_varification,login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', registration.register, name='register'),

    # email urls
    path('emai_verification/<str:uidb64>/<str:token>', email_varification.email_varification, name='email-verification'),
    path('email_verification_sent', email_varification.email_varification_sent, name='email-verification-sent'),
    path('email_verification_success', email_varification.email_varification_success, name='email-verification-success'),
    path('email_verification_failed', email_varification.email_varification_failed, name='email-verification-failed'),

    # login urls
    path('', login.my_login, name='my-login'),

    # Reset Password
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"), name='password_reset_complete'),

]