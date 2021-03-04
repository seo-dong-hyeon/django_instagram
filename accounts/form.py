from django.contrib.auth.models import User
from django import forms


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    Repeat_password = forms.CharField(label='Repeat_password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'Repeat_password', ]

        def clean_repeat_password(self):
            cleaned_data = self.cleaned_data
            if cleaned_data['password'] != cleaned_data['Repeat_password']:
                raise forms.ValidationError('비밀번호가 일치하지 않습니다')
            return cleaned_data['Repeat_password']