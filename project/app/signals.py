from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("**********************************")
    print("logged-in signal... Run Intro...")
    print("sender:",sender)
    print("request:", request)
    print("user:", user)
    print("password:", user.password)
    print(f'kwargs: {kwargs}')
# withot decorator
# user_logged_in.connect(login_success,sender=User)



@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("**********************************")
    print("logged-out signal... Run Outro...")
    print("sender:",sender)
    print("request:", request)
    print("user:", user)
    # print("password:", user.password)
    print(f'kwargs: {kwargs}')
# withot decorator
# user_logged_out.connect(log_out,sender=User)


@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print("**********************************")
    print("login failed signal...")
    print("sender:",sender)
    print("credentials:",credentials)
    print("request:", request)
    # print("password:", user.password)
    print(f'kwargs: {kwargs}')
# withot decorator
# user_loin_failed.connect(login_failed)