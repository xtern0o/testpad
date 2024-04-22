import django.db.models

import user_tests.models


class CategoryManager(django.db.models.Manager):
    def filter_by_substring(self, substring):
        return self.get_queryset().filter(name__icontains=substring)


class QuestionManager(django.db.models.Manager):
    def filter_by_test_id(self, test_id):
        return (
            self.get_queryset()
            .filter(test__id=test_id)
            .order_by(user_tests.models.Question.weight.field.name)
        )


class QuestionAnswerManager(django.db.models.Manager):
    def filter_by_tid_or_uid(self, test_id=None, user_id=None):
        if test_id and user_id:
            return self.get_queryset().filter(
                question__test__id=test_id,
                user__id=user_id,
            )
        if test_id:
            return self.get_queryset().filter(question__test__id=test_id)
        if user_id:
            return self.get_queryset().filter(user__id=user_id)
        return self.get_queryset()
