from django.urls import path
from dummy_svc.views import DiscountCodeBrandViewSet, DiscountCodeCustomerViewSet

urlpatterns = [
    path('brand/<int:brand_id>/<int:campaign_id>/', DiscountCodeBrandViewSet.as_view({
        'post': 'batch_create'
    }), name="discount_code_batch_create"),
    path('customer/<int:customer_id>/<int:campaign_id>/', DiscountCodeCustomerViewSet.as_view({
        'get': 'retrieve_and_assign'
    }), name="discount_code_retrieve_and_assign")
]
