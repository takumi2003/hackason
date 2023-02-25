from rest_framework.views import exception_handler
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    # エラーをログに記録する
    logger.error('Exception: {}'.format(str(exc)), exc_info=True)

    # 例外に応じたレスポンスを生成する
    if isinstance(exc, ValidationError):
        response = Response({'detail': exc.message_dict}, status=status.HTTP_400_BAD_REQUEST)
    else:
        response = Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response