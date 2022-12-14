from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get("username")

        try:
            if User.objects.filter(username=email).exists():
                user = User.objects.get(username=email)
            else:
                user = User.objects.get(email=email)

            if user.check_password(password):
                user_backends = "%s,%s" % (self.__module__, self.__class__.__name__)
                return user

        except User.DoesNotExist:
            return None