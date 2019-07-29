from .models import Register
# from django.contrib.auth import get_user_model

class RegisterAuth(object):
    # Register = get_user_model()

    def authenticate(self, e_mail, password):
        try:
            user = Register.objects.get(e_mail = e_mail)
            if user.check_password(password):
                return user

        except Register.DoesNotExist():
            return None

    def get_user(self, user_id):

        try:
            user = Register.objects.get(pk= user_id)
            if user.is_active:
                return users
            return None
        except Register.DoesNotExist():
            return None
