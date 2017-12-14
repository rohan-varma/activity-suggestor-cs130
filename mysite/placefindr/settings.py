
# django.core.mail

class settings:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    INSTALLED_APPS = [
    'placefindr.apps.PlacefindrConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


    # custom parameters


    TWILIO_ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        # Your Auth Token from twilio.com/console
    TWILIO_AUTH_TOKEN  = "your_auth_token"

    GOOGLE_API_KEY = "AIzaSyBmE6FRGoLwIDxQ8MJc0egc_ZH7xfQZNAU"
