import django.conf
import django.contrib
import django.contrib.auth
import django.core.exceptions
import django.core.validators
import django.db.models
import django.http
import django.utils.timezone
import sorl.thumbnail

import core.models
import user_tests.managers
import users.models


class Category(django.db.models.Model):
    objects = user_tests.managers.CategoryManager()

    name = django.db.models.CharField(
        "название категории",
        max_length=128,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


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
        default=django.utils.timezone.now,
    )

    deadline_close = django.db.models.DateTimeField(
        blank=True,
        null=True,
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

    def small_image_tmb(self):
        if self.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_image_x50().url}">',
            )
        return "изображения нет"

    def __str__(self):
        return f'Тест "{self.title}" от {self.created_on.strftime("%d.%m.%Y %H:%M")}'  # noqa

    image_tmb.short_description = "превью (300x300)"
    image_tmb.allow_tags = True

    small_image_tmb.short_description = "превью (50x50)"
    small_image_tmb.allow_tags = True

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"


class Question(django.db.models.Model):
    objects = user_tests.managers.QuestionManager()

    text = django.db.models.TextField(
        "условие вопроса",
    )

    weight = django.db.models.IntegerField(
        "вес",
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(5),
        ],
    )

    json_body = django.db.models.JSONField(
        "техническая характеристика вопроса",
        help_text="информация о типе вопроса и правильном ответе"
        " по определенной структуре",
    )

    test = django.db.models.ForeignKey(
        to=Test,
        on_delete=django.db.models.deletion.CASCADE,
        related_name="test",
        verbose_name="тест",
        help_text="тест, к которому относится этот вопрос",
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

    def small_image_tmb(self):
        if self.image:
            return django.utils.safestring.mark_safe(
                f'<img src="{self.get_image_x50().url}">',
            )
        return "изображения нет"

    image_tmb.short_description = "превью (300x300)"
    image_tmb.allow_tags = True

    small_image_tmb.short_description = "превью (50x50)"
    small_image_tmb.allow_tags = True

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        if len(self.text) < 30:
            return self.text
        return self.text[:30] + "..."


class QuestionAnswer(django.db.models.Model):
    objects = user_tests.managers.QuestionAnswerManager()

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
        help_text="меняет значение в зависимости от правильности"
        " введенных данных",
    )

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"


class TestAvatar(core.models.AbstractImage):
    test = django.db.models.OneToOneField(
        to=Test,
        verbose_name="тест",
        on_delete=django.db.models.deletion.CASCADE,
        related_name="image",
        null=True,
    )

    class Meta:
        verbose_name = "аватар"
        verbose_name_plural = "аватары"


class QuestionImage(core.models.AbstractImage):
    question = django.db.models.OneToOneField(
        to=Question,
        verbose_name="вопрос",
        on_delete=django.db.models.deletion.CASCADE,
        related_name="image",
        null=True,
    )

    class Meta:
        verbose_name = "картинка"
        verbose_name_plural = "картинки"


class TestResult(django.db.models.Model):
    objects = user_tests.managers.TestResultManager()

    user = django.db.models.ForeignKey(
        to=django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.deletion.CASCADE,
        verbose_name="пользователь",
    )

    test = django.db.models.ForeignKey(
        to=Test,
        verbose_name="тест",
        on_delete=django.db.models.deletion.CASCADE,
    )

    result = django.db.models.PositiveIntegerField(
        verbose_name="результат",
        default=0,
        help_text="сколько баллов пользователь набрал в этом тексте",
    )

    def set_result(self, user_id, test_id):
        try:
            weight_sum = (
                QuestionAnswer.objects.filter_by_tid_or_uid(test_id, user_id)
                .filter(is_correct=True)
                .aggregate(
                    total_sum=django.db.models.Sum("question__weight"),
                )["total_sum"]
            )
            TestResult.objects.create(
                test=Test.objects.get(id=test_id),
                user=users.models.CustomUser.get(id=user_id),
                result=weight_sum,
            )

            return django.http.JsonResponse(
                {
                    "status": 200,
                    "info": {
                        "value": weight_sum,
                    },
                },
            )

        except django.core.exceptions.ObjectDoesNotExist:
            return django.http.JsonResponse(
                {
                    "status": 404,
                    "info": {
                        "value": "Объект Test или User не существует",
                    },
                },
            )

        except Exception:
            return django.http.JsonResponse(
                {
                    "status": 404,
                    "info": {
                        "value": "Какая-то ошибка",
                    },
                },
            )

    class Meta:
        verbose_name = "результат теста"
        verbose_name_plural = "результаты тестов"
