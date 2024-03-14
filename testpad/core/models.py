import django.db.models


class AbstractImage(django.db.models.Model):
    image = django.db.models.ImageField(
        "изображение",
        upload_to="images/%Y/%m/%d/",
    )

    class Meta:
        abstract = True