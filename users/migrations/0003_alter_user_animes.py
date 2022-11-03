# Generated by Django 4.1.2 on 2022-11-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animes", "0001_initial"),
        ("users_animes", "0001_initial"),
        ("users", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="animes",
            field=models.ManyToManyField(
                related_name="users",
                through="users_animes.UserAnimes",
                to="animes.anime",
            ),
        ),
    ]
