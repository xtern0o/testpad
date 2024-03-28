import django.conf
import django.core.validators
import django.db.models
import django.utils.timezone
import sorl.thumbnail

import core.models


class Category(django.db.models.Model):
    name = django.db.models.CharField(
        "название категории",
        max_length=128,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Question(django.db.models.Model):
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


class Avatar(core.models.AbstractImage):
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
