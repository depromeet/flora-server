from utils.setting import get_app_list
# 장고 고유 앱 추가
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# Third-Party 전용 앱 추가
THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]
# apps 디렉토리에 있는 모든 Application 조회 및 추가
PROJECT_APPS = [
    'apps.{}'.format(app) for app in get_app_list()
]

INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS
