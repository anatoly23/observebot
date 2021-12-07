from django.db import models

# Create your models here.


class Link(models.Model):
    link = models.TextField(
        verbose_name="ссылка"
    )
    word = models.ForeignKey('Word', on_delete=models.CASCADE)


class Word(models.Model):
    word = models.TextField(
        verbose_name="слово для поиска"
    )
