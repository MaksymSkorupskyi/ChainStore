# class MyMiddleware:
#     def process_request(self, request):
#         print('process_request')
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('process_view')
#
#     def process_template_response(self, request, response):
#         print('process_template_response')
#         return response
#
#     def process_response(self, request, response):
#         print('process_response')
#         return response
#
#     def process_exception(self, request, exception):
#         print('process_exception')