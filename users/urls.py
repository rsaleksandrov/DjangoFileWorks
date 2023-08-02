from django.urls import include, path

from users.views import SignUp

urlpatterns = [
    path('singup/', SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
