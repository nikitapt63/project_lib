# Generated by Django 5.0.6 on 2024-05-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_add_author_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=70, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "author",
                    models.ManyToManyField(to="book.author", verbose_name="Автор(ы)"),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
                "ordering": ["title"],
            },
        ),
    ]
