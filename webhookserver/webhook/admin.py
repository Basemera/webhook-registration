from django.contrib import admin

from .models import WebhookRequest, WebhookUrl

# Register your models here.
admin.site.register(WebhookUrl)
admin.site.register(WebhookRequest)