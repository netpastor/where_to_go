from .base import *  # noqa
from .base import env

INSTALLED_APPS += ["django_extensions"]

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
