import django.contrib.admin

import user_tests.models


class AvatarInline(django.contrib.admin.TabularInline):
    model = user_tests.models.Avatar
    
    fields = [
        "small_image_preview",
        "image",
    ]

    readonly_fields = [
        "small_image_preview",
    ]

    def small_image_preview(self, obj):
        return obj.small_image_tmb()
    
    small_image_preview.short_description = "Превью 50x50"
    small_image_preview.allow_tags = True


class QuestionImageInline(django.contrib.admin.TabularInline):
    model = user_tests.models.QuestionImage

    fields = [
        "small_image_preview",
        "image",
    ]
    
    readonly_fields = [
        "small_image_preview",
    ]

    def small_image_preview(self, obj):
        return obj.small_image_tmb()
    
    small_image_preview.short_description = "Превью 50x50"
    small_image_preview.allow_tags = True


@django.contrib.admin.register(user_tests.models.Category)
class CategoryAdmin(django.contrib.admin.ModelAdmin):
    list_display = [
        user_tests.models.Category.name.field.name,
    ]

    search_fields = [
        user_tests.models.Category.name.field.name,
    ]


@django.contrib.admin.register(user_tests.models.Question)
class QuestionAdmin(django.contrib.admin.ModelAdmin):
    list_display = [
        user_tests.models.Question.text.field.name,
        user_tests.models.Question.weight.field.name,
        user_tests.models.Question.json_body.field.name,
        user_tests.models.Question.small_image_tmb,
    ]

    search_fields = [
        user_tests.models.Question.text.field.name,
    ]

    inlines = [
        QuestionImageInline,
    ]


@django.contrib.admin.register(user_tests.models.Test)
class TestAdmin(django.contrib.admin.ModelAdmin):
    list_display = [
        user_tests.models.Test.title.field.name,
        user_tests.models.Test.description.field.name,
        user_tests.models.Test.author.field.name,
        user_tests.models.Test.created_on.field.name,
        user_tests.models.Test.deadline_open.field.name,
        user_tests.models.Test.deadline_close.field.name,
        user_tests.models.Test.small_image_tmb,
    ]

    filter_horizontal = [
        user_tests.models.Test.questions.field.name,
    ]

    readonly_fields = [
        user_tests.models.Test.created_on.field.name,
        user_tests.models.Test.author.field.name,
    ]

    inlines = [
        AvatarInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        super().save_model(request, obj, form, change)



    
