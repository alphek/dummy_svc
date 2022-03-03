import logging

from dummy_svc.models import DiscountCode
from dummy_svc.constants import AVAILABLE
from dummy_svc.util import generate_codes


def create_discount_codes(brand_id, campaign_id, data):
    # I used bulk create ORM function for this one
    # and according to source code the function itself uses transaction atomic.So I don't put transaction block
    # I assume there should be another microservice to manage campaigns
    # or any cache can be used to hold campaigns
    # but for the sake of simplicity I will use auto increment
    codes = generate_codes(brand_id, campaign_id, data["code_count"])
    objs = [DiscountCode(brand_id=brand_id,
                         code=code,
                         campaign_id=campaign_id,
                         discount_type=data["discount_type"],
                         discount_amount=data["discount_amount"],
                         expire_date=data["expire_date"]) for code in codes]
    DiscountCode.objects.bulk_create(objs)
    return {"status": "success", "data": {"brand_id": brand_id,
                                          "campaign_id": campaign_id,
                                          "created_code_number": data["code_count"]}}


def retrieve_and_assign_code(customer_id, campaign_id):
    # TODO need to check customer id for auth
    # Can implement cache here later
    # I did not use first or last to avoid unnecessary use of order by
    qs = DiscountCode.objects.filter(campaign_id=campaign_id, status=AVAILABLE)[:1]
    if len(qs) == 1:
        code_obj = qs[0]
        code_obj.assign_to_customer(customer_id)
        return {"status": "success", "data": {"code": code_obj.code, "expire_date": code_obj.expire_date}}
    else:
        print(len(qs))
        # can be implemeted diffirent responses for run out of code or campaign is not valid
        return None
