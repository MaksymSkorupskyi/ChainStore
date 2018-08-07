import os
import time
from datetime import datetime
from django.conf import settings
from django.db import connection


class RequestsLogMiddleware:
    """
    Написать и подключить Middleware, который будет сохранять:
    - дату,
    - время,
    - метод запроса (GET, POST и т.д.),
    - URL (с доменом и GET-параметрами) запросов и
    - время генерации ответа с точностью до 0.0001 секунды
    в файл 'projectname/requests.log'.
    Каждый запрос в отдельную строку.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        self.requests_log_filename = os.path.join(settings.BASE_DIR, 'requests.log')

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        request_time = time.perf_counter_ns()

        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.
        datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response_time = round((time.perf_counter_ns() - request_time) * 1e-6, 2)

        # write Requests Log to file:
        with open(self.requests_log_filename, 'a') as f:
            f.write(f'{datetime_now} {request.method} {request.build_absolute_uri()} {response_time} ms\n')

        # print Requests Log to console
        print(f'{datetime_now} {request.method} {request.build_absolute_uri()} {response_time} ms')
        print(connection.queries, '\n')

        return response
