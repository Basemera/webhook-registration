import secrets
import requests
from hashlib import sha1
from urllib import response

from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from rest_framework import status
from logging import getLogger

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes

from .permissions import AuthorizedToken

from .models import WebhookRequest, WebhookUrl

from .serializers import WebHookUrlSerializer, WebHookRequestSerializer

logger = getLogger(__name__)


# Create your views here.
class WebHookCreateListApiView(ListCreateAPIView):
    serializer_class = WebHookUrlSerializer
    permission_classes = [AuthorizedToken]
    queryset = WebhookUrl.objects.all()


class WebHookRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = WebHookUrlSerializer
    permission_classes = [AuthorizedToken]
    queryset = WebhookUrl.objects.all()


class WebHookRequestCreateListApiView(ListCreateAPIView):
    serializer_class = WebHookRequestSerializer
    queryset = WebhookRequest.objects.all()
    def create(self, request, *args, **kwargs):
        urls = WebhookUrl.objects.all()
        res_list = []

        for url in urls:
            try:
                response = requests.post(
                    'http://0.0.0.0:9876/api/webhook/',
                    {
                        'token':url.token,
                        'payload': request.data.get('payload')
                    }
                )
                data = [{
                'payload': request.data.get('payload'),
                'url': url.id,
                'status': 'SUCCESS' if response.status_code == 200 else 'ERRORS',
                'token': url.token
                }]
            except Exception as exc:
                data = [{
                    'payload': request.data.get('payload'),
                    'url': url.id,
                    'status': 'ERRORS',
                    'response': str(exc),
                    'token': url.token
                }]
                logger.error(str(exc))
                logger.debug("I errored")
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            res_list.append(
                {
                    'data': serializer.data,
                    'status':status.HTTP_201_CREATED,
                    'headers': headers
                }
            )
        return Response(
            res_list,
            status=status.HTTP_201_CREATED,
            )
