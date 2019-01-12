from re import compile

from rest_framework.status import is_client_error


class ResponseFormattingMiddleware:
    # API 전용 응답 포멧팅 미들웨어
    METHODS = (
        'GET', 'POST', 'DELETE', 'PUT', 'PATCH'
    )
    API_URLS = [compile(r'^api/')]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info.lstrip('/')
        response = self.get_response(request)

        if request.method in self.METHODS and \
            any(m.match(path) for m in self.API_URLS):
            # 서버 500 에러 이외의 에러 메세지 처리를 위한 로직
            if is_client_error(response.status_code) and \
                hasattr(response, 'data') and \
                getattr(response, 'data') is not None:
                data = response.data
                message = None

                if isinstance(data, list):
                    # 에러 메세지가 리스트인 경우
                    # 여러 필드에서 에러가 발생한 경우
                    message = data[0]
                elif 'detail' in data:
                    message = data.get('detail')
            
            response_format = {
                'message': message,
                'success': False
            }

            response.data = response_format
            response.content = response.render().rendered_content

        return response