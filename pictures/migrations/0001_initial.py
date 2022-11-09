# Generated by Django 4.1.3 on 2022-11-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CatPicture",
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
                ("title", models.CharField(blank=True, max_length=128)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(upload_to="CatPictures")),
            ],
        ),
    ]