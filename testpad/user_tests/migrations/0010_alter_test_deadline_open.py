# Generated by Django 4.2 on 2024-03-28 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_tests", "0009_alter_test_deadline_open"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="deadline_open",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    3,
                    28,
                    15,
                    13,
                    32,
                    652738,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
    ]