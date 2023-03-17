from email.policy import default
from pyexpat import model
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class Todo(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name = '할 일'
    )
    description = models.TextField(
        verbose_name = '세부사항'
    )
    due_date = models.DateTimeField(
        null=True,
        verbose_name = '마감 기한',
        help_text = '마감 기한을 선택해 주세요.'
    )

    completed = models.BooleanField(
        default=False,
        verbose_name = '완료 여부'
    )

    def __str__(self):
        return self.title
