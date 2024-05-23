from django.db import models
from .mixins import DateTimeMixin


class Author(DateTimeMixin, models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.pk} - {self.first_name.capitalize()[0]}.{self.last_name.capitalize()} {self.birth_date}"

    def __repr__(self):
        return f"{self.pk} - {self.first_name.capitalize()[0]}.{self.last_name.capitalize()}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['birth_date']


class Book(DateTimeMixin, models.Model):
    title = models.CharField(max_length=70, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    author = models.ManyToManyField(Author, verbose_name="Автор(ы)")

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def __repr__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']
