from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView

from accounts.forms import RegisterForm, ProfileEditForm


# Create your views here.
class RegisterFormView(FormView):
    template_name = "registeration.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],
                                 email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'],
                                 last_name = form.cleaned_data['last_name'])
        return super().form_valid(form)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'login.html')

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy("profile_view"))
        else:
            error = 'Username or password invalid'
            return TemplateResponse(request, 'login.html', context={'error': error})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("login"))

def profile_view(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse('401 UNAUTHORIZED', status=401)
    return JsonResponse({"id": user.id, "username": user.username, "email": user.email,
                         "first_name": user.first_name, "last_name": user.last_name})


class ProfileEditFormView(FormView):
    template_name = "profile_edit.html"
    success_url = reverse_lazy("profile_view")
    form_class = ProfileEditForm

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('401 UNAUTHORIZED', status=401)
        return FormView.render_to_response(self, context, **response_kwargs)

    def get_initial(self):
        initial = super(ProfileEditFormView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'email': self.request.user.email})
            initial.update({'first_name': self.request.user.first_name})
            initial.update({'last_name': self.request.user.last_name})
        return initial

    def form_valid(self, form):
        user = self.request.user
        if not user.is_authenticated:
            return HttpResponse('401 UNAUTHORIZED', status=401)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        if form.cleaned_data['password1'] is "":
            print("password not changed")
        else:
            print(f"password=>{form.cleaned_data['password1']}")
            user.set_password(form.cleaned_data['password1'])
            update_session_auth_hash(self.request, user)
        user.save()
        return super().form_valid(form)


