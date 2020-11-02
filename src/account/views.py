from account.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('index')

    # def get_queryset(self):
    # queryset = super().get_queryset()
    # return queryset.filter(id=self.request.user.id)

    def get_object(self, queryset=None):
        return self.request.user
