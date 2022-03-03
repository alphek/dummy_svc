from rest_framework import serializers
from dummy_svc.models import DiscountCode
from dummy_svc.constants import DISCOUNT_TYPES


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = '__all__'


class DiscountCodeCreateSerializer(serializers.Serializer):
    discount_type = serializers.ChoiceField(required=True, choices=DISCOUNT_TYPES)
    discount_amount = serializers.DecimalField(required=True, max_digits=6, decimal_places=2)
    expire_date = serializers.DateTimeField(required=True)
    code_count = serializers.IntegerField(required=True)
