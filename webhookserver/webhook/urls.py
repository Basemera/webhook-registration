from django.urls import path
from .views import WebHookCreateListApiView, WebHookRequestCreateListApiView

urlpatterns = [
    path('', WebHookCreateListApiView.as_view()),
    path('test/', WebHookRequestCreateListApiView.as_view())

]