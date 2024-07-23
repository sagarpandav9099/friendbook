from django.urls import path
from .views import registration,email_varification

urlpatterns = [
    path('register/', registration.register, name='register'),

    # email urls
    path('emai-verification/<str:uidb64>/<str:token>', email_varification.email_varification, name='email-verification'),
    path('email_verification_sent', email_varification.email_varification_sent, name='email-verification-sent'),
    path('email_verification_success', email_varification.email_varification_success, name='email-verification-success'),
    path('email_verification_failed', email_varification.email_varification_failed, name='email-verification-failed'),


]