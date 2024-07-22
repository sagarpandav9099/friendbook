from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



# Registration form
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Your Full Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Email Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Your Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-0',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # Mark email as required
        self.fields['email'].required = True

    # Email validation

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already exists')

        # len function updated ###
        if len(email) >= 60:
            raise forms.ValidationError("Your email is too long")

        return email
    