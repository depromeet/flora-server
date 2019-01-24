import datetime

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365),
}