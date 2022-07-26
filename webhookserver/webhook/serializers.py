from rest_framework import serializers
from .models import WebhookUrl, WebhookRequest


class WebHookUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookUrl
        fields = (
            'url',
            'token',
            'status',
            'id'
        )


class WebHookRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookRequest
        fields = (
            'url',
            'payload',
            'status',
            'event_time',
            'response',
            'id'
        )