import secrets
import os
from django.conf import settings
from rest_framework import permissions
from dotenv import load_dotenv

load_dotenv()

class AuthorizedToken(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.headers)
        header_signature = request.headers.get('webhook-token')
        webhook_token = os.environ.get('WEBHOOK_TOKEN', '')
        if header_signature and secrets.compare_digest(webhook_token, header_signature):
            return True

    def has_object_permission(self, request, view, obj):
        header_signature = request.headers.get('webhook-token')
        if header_signature and secrets.compare_digest(settings.WEBHOOK_KEY, header_signature):
            return True