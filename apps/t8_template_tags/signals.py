from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.t8_template_tags.models import ModelSignal


@receiver(post_save)
def save_signal(sender, created, **kwargs):
    class_name = sender.__name__
    if class_name == 'ModelSignal':
        return
    action = 'create' if created else 'edit'
    ModelSignal.objects.create(model=class_name, action=action).save()


@receiver(post_delete)
def delete_signal(sender, **kwargs):
    class_name = sender.__name__
    ModelSignal.objects.create(model=class_name, action='delete').save()
