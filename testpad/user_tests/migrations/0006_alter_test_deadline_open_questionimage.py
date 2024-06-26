# Generated by Django 4.2 on 2024-03-14 17:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user_tests", "0005_alter_test_deadline_open"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="deadline_open",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    3,
                    14,
                    17,
                    6,
                    41,
                    412083,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.CreateModel(
            name="QuestionImage",
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
                (
                    "image",
                    models.ImageField(
                        upload_to="images/%Y/%m/%d/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "question",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image",
                        to="user_tests.question",
                        verbose_name="вопрос",
                    ),
                ),
            ],
            options={
                "verbose_name": "картинка",
                "verbose_name_plural": "картинки",
            },
        ),
    ]
