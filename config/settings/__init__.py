import os
import glob
from split_settings.tools import include

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = os.environ.get('SECRET_KEY')

# 구동 환경 체크
ENV = os.environ.get('PROJECT_ENV') or 'development'
print('****Running on %s settings****' % ENV)

# 설정 파일 분기
COMPONENT_DIR = os.path.join(BASE_DIR, 'config', 'settings', 'components')
COMPONENTS = [
    'components/{}'.format(os.path.basename(component)) for component
    in glob.glob(os.path.join(COMPONENT_DIR, '*.py'))
]
SETTINGS = [
    'environments/%s.py' % ENV,
] + COMPONENTS
include(*SETTINGS)
