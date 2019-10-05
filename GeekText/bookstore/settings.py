# Django settings for django_bookstore project.
import os
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': 'Bookstore_website_project',
        'USER':'postgres',
        'PASSWORD':'Nicole13',
        'PORT':'5432',
        'HOST': 'localhost',
    }
}
