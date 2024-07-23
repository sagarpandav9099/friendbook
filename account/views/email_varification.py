from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ..token import user_tokenizer_generate

def email_varification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(User, pk=unique_id)

    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('email-verification-success')
    else:
        return redirect('email-verification-failed')


def email_varification_sent(request):
    return render(request, 'registration/email_verification_sent.html')


def email_varification_success(request):
    return render(request, 'registration/email_verification_success.html')


def email_varification_failed(request):
    return render(request, 'registration/email_verification_failed.html')
 