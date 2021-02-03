from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View
from . import forms

def index():
    return render('authen/index.hml')

class RegisterView(View):

    def get(self, request):
        user_form = forms.UserForm()
        return render(request, 'authen/register.html', {
            'user_form': user_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            user_form.set_password(user.password)
            user.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('index')
        else:
            messages.error(request, _('Please correct the error below.'))
