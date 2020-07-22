# coding=UTF-8
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        #'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'oraciones_2020_new',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'cloze',
        'PASSWORD': '23571113',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}



# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, './media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, './static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4ensr0^4%%f%s)bq&=@w&-oa8ehlkp8mv91o(cjuzb2m=!l4u4'

ADMIN_MEDIA_PREFIX = '/media/admin/'
