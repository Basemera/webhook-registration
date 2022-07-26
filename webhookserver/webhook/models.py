from django.db import models


# Create your models here.
class WebhookUrl(models.Model):
    ACTIVE = 'ACTIVE'
    DEACTIVATED = 'DEACTIVATED'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (DEACTIVATED, 'Deactivated')
    ]
    
    url = models.URLField()
    token = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )


class WebhookRequest(models.Model):
    payload = models.JSONField(blank=True)
    url = models.ForeignKey(WebhookUrl, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)
    SUCCESSFUL = 'SUCCESS'
    FAILED = 'ERRORS'
    STATUS_CHOICES = [
        (SUCCESSFUL, 'Success'),
        (FAILED, 'Errors')
    ]
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES
    )
    response = models.TextField(blank=True)