from account.forms import UserRegistrationForm, PasswordChangeForm
from account.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View, FormView, TemplateView

from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters



class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('index')

    # def get_queryset(self):
    # queryset = super().get_queryset()
    # return queryset.filter(id=self.request.user.id)

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')


class ActivateUser(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        user.is_active = True
        user.save(update_fields=('is_active', ))
        return redirect('index')


class PasswordChangeView(PasswordContextMixin, UpdateView):
    model = User
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password-change-done')
    template_name = 'registration/password_change_form.html'
    title = ('Password change')

