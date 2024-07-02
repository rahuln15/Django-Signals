from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete

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

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("**********************************")
    print("Pre save signal...")
    print("sender:",sender)
    print("instance:",instance)
    print(f'kwargs: {kwargs}')
# withot decorator
# pre_save.connect(at_beginning_save,sender=User)


@receiver(post_save, sender=User)
def at_ending_save(sender, instance,created, **kwargs):
    if created:
        print("**********************************")
        print("Post save signal...")
        print("New Record")
        print("sender:",sender)
        print("instance:",instance)
        print("created:",created)
        print(f'kwargs: {kwargs}')
    else:
        print("**********************************")
        print("Post save signal...")
        print("Update")
        print("sender:",sender)
        print("instance:",instance)
        print("created:",created)
        print(f'kwargs: {kwargs}')
# withot decorator
# post_save.connect(at_ending_save,sender=User)



@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("**********************************")
    print("Pre Delete Signal")
    print("sender:",sender)
    print("instance:",instance)
    print(f'kwargs: {kwargs}')
# withot decorator
# pre_delete.connect(at_beginning_delete,sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("**********************************")
    print("Post Delete Signal")
    print("sender:",sender)
    print("instance:",instance)
    print(f'kwargs: {kwargs}')
# withot decorator
# post_delete.connect(at_ending_delete,sender=User)


@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("**********************************")
    print("Pre init Signal")
    print("sender:",sender)
    print(f'args:{args}')
    print(f'kwargs: {kwargs}')
# withot decorator
# pre_init.connect(at_beginning_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("**********************************")
    print("Post init signal")
    print("sender:",sender)
    print(f'args:{args}')
    print(f'kwargs: {kwargs}')
# withot decorator
# post_init.connect(at_ending_init, sender=User)