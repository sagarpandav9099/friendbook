from django.shortcuts import render, redirect
from ..forms.registretion import CreateUserForm

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from ..token import user_tokenizer_generate
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Account Verification'
            message = render_to_string('registration/email_verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })

            user.email_user(subject=subject, message=message)

            return redirect('email-verification-sent')
        
    context = {'form': form}

    return render(request, 'registration/register.html', context=context)