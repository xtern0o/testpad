import django.conf
import django.core.validators
import django.db.models
import django.utils.timezone
import sorl.thumbnail

import users.models


class Category(django.db.models.Model):
    name = django.db.models.CharField(
        "название категории",
        max_length=128,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Question(django.db.models.Model):
    text = django.db.models.TextField(
        "условие вопроса",
    )

    weight = django.db.models.IntegerField(
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(5),
            ]
    )

    json_body = django.db.models.JSONField(
        "техническая характеристика вопроса",
        help_text="информация о типе вопроса и правильном ответе по определенной структуре",
    )

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"


class QuestionAnswer(django.db.models.Model):
    user = django.db.models.ForeignKey(
        to=django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.deletion.CASCADE,
    )

    question = django.db.models.ForeignKey(
        to=Question,
        on_delete=django.db.models.deletion.CASCADE,
    )

    answer = django.db.models.CharField(
        "ответ",
        help_text="ответ, данный пользователем",
        max_length=64,
        blank=True,
        null=True,
    )

    is_correct = django.db.models.BooleanField(
        "правильность ответа",
        help_text="меняет значение в зависимости от правильности введенных данных",
    )

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"


class Test(django.db.models.Model):
    title = django.db.models.CharField(
        "название теста",
        help_text="название теста",
        max_length=128,
    )

    description = django.db.models.TextField(
        "описание теста",
        help_text="краткая информация о тесте (опционально)",
    )

    author = django.db.models.ForeignKey(
        to=django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.deletion.CASCADE,
        help_text="создатель теста",
        verbose_name="автор теста",
        related_name="author",
    )

    avatar = django.db.models.ImageField(
        upload_to="user_tests/%Y/%m/%d/",
        help_text="аватарка теста",
        verbose_name="аватар",
        null=True,
        blank=True,
    )

    category = django.db.models.ForeignKey(
        to=Category,
        null=False,
        on_delete=django.db.models.deletion.CASCADE,
        help_text="категория этого теста (может быть только одна!)",
        verbose_name="категория",
        related_name="category",
    )

    created_on = django.db.models.DateTimeField(
        auto_now_add=True,
        help_text="время создания теста",
        verbose_name="время создания теста",
    )

    deadline_open = django.db.models.DateTimeField(
        default=django.utils.timezone.now(),
    )

    deadline_close = django.db.models.DateTimeField(
        blank=True,
        null=True,
    )

    questions = django.db.models.ManyToManyField(
        to=Question,
        verbose_name="вопросы",
        help_text="список вопросов в этом тесте",
    )

    def get_image_x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def get_image_x50(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "50x50",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_image_x300().url}">',
            )
        return "изображения нет"

    def __str__(self):
        return f'Тест "{self.title}" от {self.created_on.strftime("%d.%m.%Y %H:%M")}'

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"
