import datetime
import jwt

import django.conf
import django.contrib.auth
import django.contrib.auth.decorators
import django.contrib.auth.mixins
import django.contrib.auth.models
import django.contrib.messages
import django.core.mail
import django.shortcuts
import django.urls
import django.utils.timezone
import django.views.generic

import core.utils
import users.forms
import users.models


class SignupFormView(django.views.generic.FormView):
    template_name = "users/signup.html"
    form_class = users.forms.SignUpForm

    def form_valid(self, form):
        user = form.save()
        user.save()

        if django.conf.settings.DEFAULT_USER_IS_ACTIVE:
            user.is_active = True
            user.save()

        expiration = django.utils.timezone.now() + datetime.timedelta(
            hours=django.conf.settings.LINK_EXPIRATION,
        )

        exp_timestamp = int(expiration.timestamp())

        token_context = {
            "username": user.username,
            "exp": exp_timestamp,
        }

        token = jwt.encode(
            token_context,
            django.conf.settings.SECRET_KEY,
            algorithm="HS256",
        )

        activation_link = self.request.build_absolute_uri(
            django.urls.reverse(
                "users:activate",
                kwargs={
                    "token": token,
                },
            ),
        )

        msg_text = (
            f"Вам необходимо активировать аккаунт в течение 12 часов "
            "после регистрации, перейдя по ссылке:\n"
            f"{activation_link}\n"
            "В противном случае возможности аккаунта будут ограничены."
        )

        django.core.mail.send_mail(
            "Активация аккунта PROTester",
            msg_text,
            django.conf.settings.EMAIL_ADDRESS,
            [user.email],
        )

        django.contrib.auth.login(self.request, user)

        return django.shortcuts.redirect(
            django.urls.reverse("homepage:home"),
        )
    

class ActivateUserView(django.views.generic.TemplateView):
    template_name = "users/activation_success"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        token = self.kwargs["token"]
        data, status_ok = core.utils.decode_token(token)

        if status_ok:
            try:
                user = users.models.CustomUser.objects.get(
                    username=data["username"],
                )
                user.is_active = True
                user.save()
                context["ok"] = status_ok
                context["info"] = data
            except users.models.CustomUser.DoesNotExist:
                context["ok"] = False
                context["info"] = "Пользователь не найден"
        else:
            context["ok"] = status_ok
            context["info"] = data
        
        return context
