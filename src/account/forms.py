from account.models import User
from account.tasks import send_sign_up_email

from django import forms


class UserRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    def clean(self):
        cleaned_data: dict = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', 'User already exsist')
        return email

    def save(self, commit=True):
        instance: User = super().save(commit=False)
        instance.set_password(self.cleaned_data['password1'])
        instance.is_active = False
        instance.save()
        send_sign_up_email.apply_async(args=[instance.id], coutdown=30)
        return instance


class PasswordChangeForm(forms.ModelForm):

    current_password = forms.CharField(label=("Current_password"), widget=forms.PasswordInput())
    new_password = forms.CharField(label=("New password"), widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(label=("Confirm new password"), widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('current_password', 'new_password', 'confirm_new_password',)

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise forms.ValidationError('password is incorrect')
        return current_password

    def clean(self):
        cleaned_data: dict = super().clean()
        if not self.errors:
            if cleaned_data['new_password'] != cleaned_data['confirm_new_password']:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        instance: User = super().save(commit=False)
        instance.set_password(self.cleaned_data['new_password'])
        instance.save()
        return instance
