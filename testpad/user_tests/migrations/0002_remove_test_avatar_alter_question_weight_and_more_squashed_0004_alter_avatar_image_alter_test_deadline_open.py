# Generated by Django 4.2 on 2024-03-14 16:36

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    replaces = [
        (
            "user_tests",
            "0002_remove_test_avatar_alter_question_weight_and_more",
        ),
        ("user_tests", "0003_alter_avatar_test_alter_test_deadline_open"),
        ("user_tests", "0004_alter_avatar_image_alter_test_deadline_open"),
    ]

    dependencies = [
        ("user_tests", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="test",
            name="avatar",
        ),
        migrations.AlterField(
            model_name="question",
            name="weight",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="вес",
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="deadline_open",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    3,
                    14,
                    16,
                    16,
                    25,
                    75981,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="deadline_open",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    3,
                    14,
                    16,
                    18,
                    3,
                    369441,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
        migrations.CreateModel(
            name="Avatar",
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
                    "test",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image",
                        to="user_tests.test",
                        verbose_name="тест",
                    ),
                ),
            ],
            options={
                "verbose_name": "аватар",
                "verbose_name_plural": "аватары",
            },
        ),
        migrations.AlterField(
            model_name="test",
            name="deadline_open",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    3,
                    14,
                    16,
                    35,
                    22,
                    617621,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
    ]
