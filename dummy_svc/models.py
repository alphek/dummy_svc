from django.db import models
from dummy_svc.constants import DISCOUNT_TYPES, CODE_STATUS, AVAILABLE, USED


class DiscountCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=CODE_STATUS, default=AVAILABLE)
    # made BigAutoField because in past I had difficulties with integer run out
    # so if it's not a big cost I rather to use bigint for pk
    brand_id = models.IntegerField(null=False)
    # can be foreign key according to db structure
    customer_id = models.IntegerField(null=True)
    # can be foreign key according to db structure
    # will be assigned after get method called
    campaign_id = models.IntegerField(null=False)
    discount_type = models.CharField(max_length=1, choices=DISCOUNT_TYPES, null=False)
    # I used constant file to store discount_types but more dynamic approach can be used If they will change in time
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    expire_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # more indexes can be added if new apis need it
    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['campaign_id'])
        ]

    def assign_to_customer(self, customer_id):
        self.customer_id = customer_id
        self.status = USED
        self.save()


