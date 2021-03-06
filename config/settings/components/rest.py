REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'utils.authenticate.TokenAuthentication',
    # ),
    'DATETIME_FORMAT': '%Y/%m/%d %H:%M'
}