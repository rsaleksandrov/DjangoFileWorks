from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Document(models.Model):
    description = models.CharField(
        max_length=100,
        verbose_name='Описание файла',
        blank=False,
        null=False,
    )
    document = models.FileField(
        upload_to='documents/',
        verbose_name='Файл документа',
    )
    uploaded_to = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
    )
    content_type = models.TextField(
        verbose_name='Тип документа',
        blank=False,
        null=False,
    )
    hash_code = models.CharField(
        max_length=256,
        verbose_name='Хэш код файла',
        blank=False,
        null=False,
        unique=True,
        db_index=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='documents',
        blank=False,
        null=False,
        verbose_name='Владелец файла',
    )
