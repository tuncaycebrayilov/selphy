from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
from django.contrib.auth.views import(
                        PasswordChangeDoneView,
                        PasswordResetView,
                        PasswordResetConfirmView,
                        LoginView)
from .tokens import account_activation_token
from .forms import UserRegisterForm, UserLoginForm
from .models import User



def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        messages.error(request, 'Your session is expired')
        return redirect('/')
    

class RegisterView(CreateView):
    form_class = UserRegisterForm
    succes_url = reverse_lazy('login')
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.is_active = False
        form.instance.save()

        subject = 'Active Your Account'
        current_site = get_current_site(self.request)
        message = render_to_string('email/confirmation_email.html', {
            'user': form.instance,
            'domain': current_site.domain, 
            'uid': urlsafe_base64_encode(force_bytes(form.instance.pk)),
            'token': account_activation_token.make_token(form.instance),
            })
        from_email = EMAIL_HOST_USER
        to_email = self.request.POST['email']
        send_mail(
            subject,
            message,
            from_email,
            [to_email]
        )
        messages.success(self.request, ('Please confirm your email to complate registration.'))
        return redirect('login')
    

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'my-account.html'
    authentication_form = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/core/index')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)