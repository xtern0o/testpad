# Generated by Django 4.2 on 2024-04-18 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user_tests", "0012_alter_test_deadline_open_alter_test_questions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="test",
            name="questions",
        ),
        migrations.AddField(
            model_name="question",
            name="test",
            field=models.ForeignKey(
                default=1,
                help_text="тест, к которому относится этот вопрос",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test",
                to="user_tests.test",
                verbose_name="тест",
            ),
            preserve_default=False,
        ),
    ]