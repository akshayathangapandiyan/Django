from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import student_signals

@receiver(post_save, sender= student_signals)
def Student_created(sender ,instance ,created,**kwargs):
    if created:
        print(f'student created:{instance.name}')