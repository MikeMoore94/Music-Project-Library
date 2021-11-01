


SECRET_KEY = 'django-insecure-wy9m)-5qrg3n9^36j1abj=%)@gbz$7oc%p1w_r1xgf71)v90xj'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'Music_library_database',
        'USER': 'root',
        'PASSWORD': 'Moore210',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True 
        }
    }
}
