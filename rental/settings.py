#settings.py


import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ix_n_xy)1x4k@v7meaiw97t@4=6(%hvfx3l!qoj4=&9=+p2f5("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    'social_django',
    'rentalapp',  # ควรมี rentalapp อยู่ในนี้
    
]
 
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # ค่า Default

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'rental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'rentalapp/templates'],  # หรือ BASE_DIR / 'templates'
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]



WSGI_APPLICATION = "rental.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fashion_db',          # ชื่อของฐานข้อมูล
        'USER': 'fashion_user',        # ชื่อผู้ใช้ของฐานข้อมูล
        'PASSWORD': 'fashion_pass',    # รหัสผ่านของฐานข้อมูล
        'HOST': 'db',                  # ชื่อโฮสต์ของฐานข้อมูลใน Docker Compose
        'PORT': '5432',                # พอร์ตของฐานข้อมูล
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # ใช้ SMTP ของ Gmail หรือผู้ให้บริการอื่น ๆ
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'thawaporn.t@gmail.com'
EMAIL_HOST_PASSWORD = 'Tt20122004'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.google.GoogleOAuth2',

]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '69226887281-821ta93itabg2he4gakjsn5q3hcekana.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile'] # ตัวอย่าง Scope
# ระบุ URL ที่ใช้สำหรับการเชื่อมต่อ
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000/auth/complete/google-oauth2/'
LOGIN_REDIRECT_URL = '/'  # หรือเส้นทางที่คุณต้องการให้ผู้ใช้ไปหลังจากล็อกอินสำเร็จ


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'rentalapp/static',  # พาธหลักที่เก็บไฟล์ Static (รวมพาธ rental/image)
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
# settings.py
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
