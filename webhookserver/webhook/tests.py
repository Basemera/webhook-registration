import pytest
from rest_framework.test import APITestCase
import json

# Create your tests here.
pytest.mark.django_db()
class WebHookUrlCreateListApiViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def test_create_webhook_url_successfully(self):
        response = self.client.post(
            '/api/webhook/',
            {
                "url": "http://0.0.0.0:3000/reporting",
                "status": "ACTIVE",
                "token":"foo"
            },
            
            HTTP_Webhook_Token= '45a9eef987caa53c07a433c2daf58728',
            format='json'
        )
        self.assertEqual(response.data, {
            "url": "http://0.0.0.0:3000/reporting",
            "token": "foo",
            "status": "ACTIVE",
            "id": 2
        })

    def test_create_webhook_url_unsuccessfully_with_no_token(self):
        response = self.client.post(
            '/api/webhook/',
            {
                "url": "http://0.0.0.0:3000/reporting",
                "status": "ACTIVE",
                "token":"foo"
            },
            HTTP_Webhook_Token= 'wrong string',          
            format='json'
        )
        res = response.content.decode('utf-8')
        dict_res = json.loads(res)
        self.assertEqual(dict_res, {"detail":"Authentication credentials were not provided."})

    
    def test_create_webhook_url_unsuccessfully_with_wrong_token(self):
        response = self.client.post(
            '/api/webhook/',
            {
                "url": "http://0.0.0.0:3000/reporting",
                "status": "ACTIVE",
                "token":"foo"
            },            
            format='json'
        )
        res = response.content.decode('utf-8')
        dict_res = json.loads(res)
        self.assertEqual(dict_res, {"detail":"Authentication credentials were not provided."})

pytest.mark.django_db()
class WebHookRequestCreateListApiViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()

    def test_make_webhook_request_successfully(self):
        response = self.client.post(
            '/api/webhook/test/',
            {
                "payload": ["any", {"valid":"json"}]
            },
            HTTP_Webhook_Token= '45a9eef987caa53c07a433c2daf58728',
            format='json'
        )
        res = dict(response.data[0]['data'][0])
        self.assertEqual(res['url'], 1)
        self.assertEqual(res['payload'], [
					"any",
					{
						"valid": "json"
					}
				])