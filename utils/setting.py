# Config 설정과 관련된 기능 제공
import os
import glob

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_app_list():
    # 프로젝트 앱 이름을 리스트로 반환
    try:
        app_list = [
            os.path.basename(app) for app in glob.glob(
                os.path.join(BASE_DIR, 'apps', '*')) 
            if not os.path.basename(app).startswith('__pycache__') and
            not os.path.basename(app).startswith('__init__')
        ]
    except ModuleNotFoundError:
        raise ImproperlyConfigured(
            "프로젝트 앱 디렉토리를 조회하는 과정에서 문제가 발생했습니다."
        )
    return app_list
