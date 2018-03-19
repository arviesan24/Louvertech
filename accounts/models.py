from django.contrib.auth.models import User
from django.db.models.signals import pre_save

def pre_save_user_receiver(instance, *args, **kwargs):
    '''
    :param instance: accounts_signup function in views
    check if new registration occurs, change the is_active to False so admin needs to confirm the registration
    '''
    if instance.is_active:
        instance.is_active = False

pre_save.connect(pre_save_user_receiver, sender=User)