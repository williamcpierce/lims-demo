"""
Django settings for lims project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import json
import os

from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^z16o6g&-*kv%q8_tkt5@&iiketx&k@zzp^*89byj_!=s+h=a!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split()


# Application definition

INSTALLED_APPS = [
    "unfold.contrib.import_export",
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "import_export",
    "mptt",
    "auditlog",
    "registry",
    "inventory",
    "override",
]

MIDDLEWARE = [
    "lims.middleware.HealthCheckMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "auditlog.middleware.AuditlogMiddleware",
]

ROOT_URLCONF = "lims.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lims.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if "RDS_DB_NAME" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ["RDS_DB_NAME"],
            "USER": os.environ["RDS_USERNAME"],
            "PASSWORD": os.environ["RDS_PASSWORD"],
            "HOST": os.environ["RDS_HOSTNAME"],
            "PORT": os.environ["RDS_PORT"],
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/staticfiles/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Unfold settings

UNFOLD = {
    "SITE_TITLE": "LIMS Demo",
    "SITE_HEADER": "LIMS Demo",
    "SITE_URL": None,
    "SITE_SYMBOL": "Genetics",  # symbol from icon set
    "COLORS": {
        "primary": {
            "50": "0 216 164",
            "100": "0 216 164",
            "200": "0 216 164",
            "300": "0 216 164",
            "400": "0 216 164",
            "500": "0 216 164",
            "600": "0 216 164",
            "700": "0 216 164",
            "800": "0 216 164",
            "900": "0 216 164",
        }
    },
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Registry"),
                "separator": False,
                "items": [
                    {
                        "title": _("Samples"),
                        "icon": "genetics",
                        "link": reverse_lazy("admin:registry_sample_changelist"),
                    },
                    {
                        "title": _("Types"),
                        "icon": "settings",
                        "link": reverse_lazy("admin:registry_type_changelist"),
                    },
                ],
            },
            {
                "title": _("Inventory"),
                "separator": True,
                "items": [
                    {
                        "title": _("Containers"),
                        "icon": "labs",
                        "link": reverse_lazy("admin:inventory_container_changelist"),
                    },
                    {
                        "title": _("Locations"),
                        "icon": "location_on",
                        "link": reverse_lazy("admin:inventory_location_changelist"),
                    },
                ],
            },
            {
                "title": _("Audit Log"),
                "separator": True,
                "items": [
                    {
                        "title": _("Log Entries"),
                        "icon": "library_books",
                        "link": reverse_lazy("admin:auditlog_logentry_changelist"),
                    },
                ],
            },
            {
                "title": _("Auth"),
                "separator": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "groups",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}


# Import-Export settings

IMPORT_EXPORT_SKIP_ADMIN_CONFIRM = True


# CSRF

CSRF_TRUSTED_ORIGINS = ["https://williampierce.io", "https://www.williampierce.io"]
