from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.cache import cache
from dummy_svc.serializers import DiscountCodeCreateSerializer
from dummy_svc.discount_code import create_discount_codes, retrieve_and_assign_code


class DiscountCodeBrandViewSet(viewsets.ViewSet):
    def batch_create(self, request, brand_id, campaign_id):
        serializer = DiscountCodeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_body = create_discount_codes(brand_id, campaign_id, serializer.data)
        cache.set(str(campaign_id), response_body["data"]["created_code_number"])
        return Response(response_body, status=status.HTTP_201_CREATED)


class DiscountCodeCustomerViewSet(viewsets.ViewSet):
    def retrieve_and_assign(self, request, customer_id, campaign_id):
        remain_code_count = cache.get(str(campaign_id))
        if not remain_code_count or int(remain_code_count) < 1:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(remain_code_count)
        response_body = retrieve_and_assign_code(customer_id, campaign_id)
        if response_body:
            cache.set(str(campaign_id), str(int(remain_code_count) - 1))
            return Response(response_body, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
