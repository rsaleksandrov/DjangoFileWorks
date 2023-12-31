# Generated by Django 4.2 on 2023-04-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'description',
                    models.CharField(
                        max_length=100, verbose_name='Описание файла'
                    ),
                ),
                (
                    'document',
                    models.FileField(
                        upload_to='documents/', verbose_name='Файл документа'
                    ),
                ),
                (
                    'uploaded_to',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата добавления'
                    ),
                ),
                (
                    'content_type',
                    models.TextField(verbose_name='Тип документа'),
                ),
                (
                    'hash_code',
                    models.CharField(
                        db_index=True,
                        max_length=256,
                        unique=True,
                        verbose_name='Хэш код файла',
                    ),
                ),
            ],
        ),
    ]
