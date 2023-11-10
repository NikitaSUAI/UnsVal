import uuid
from django.db import models


class Dialogs(models.Model):
    dialog_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    user_id = models.UUIDField()

    question = models.CharField(max_length=4000)
    answer = models.CharField(max_length=4000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()

    def __str__(self):
        return f'{self.question} {self.answer}'


class StopThemes(models.Model):
    theme_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    theme = models.CharField(max_length=4000)
    embed = models.BinaryField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()

    def __str__(self):
        return f'{self.theme}'
