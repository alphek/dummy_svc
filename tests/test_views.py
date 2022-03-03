from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse


class TestDiscountCodeAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_discount_code_batch_create(self):
        url_params = {"brand_id": 1, "campaign_id": 1}
        url = reverse("discount_code_batch_create", kwargs=url_params)
        data = {
            "discount_type": "P",
            "discount_amount": 20.0,
            "expire_date": "2022-01-31 00:00:00",
            "code_count": 200
            }
        response = self.client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED
        # more conditions can be added

    # TODO populate test db so can Test this one properly
    def test_discount_code_retrieve_and_assign(self):
        url_params = {"customer_id": 1, "campaign_id": 1}
        url = reverse("discount_code_retrieve_and_assign", kwargs=url_params)
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        # more conditions can be added
