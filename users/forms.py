from django.contrib.auth.forms import UserCreationForm

from main.models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # type: ignore
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
