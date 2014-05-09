# -*- coding: utf-8 -*-

import us

from limelight.types import Map

tracking = Map(
    offer_id='C1',
    affiliate_id='AFID',
    affiliate_sub_id='SID',
    affiliate_sub_id2='AID'
)

credit_card = Map(
    first_name='billing_first_name',
    last_name='billing_last_name',
    type=('credit_card_type', lambda v: v.lower()),
    number='credit_card_number',
    expires=('expiration_date', lambda v: v.strftime("%m%y")),
    ccv='CVV'
)

address = Map(
    first_name='first_name',
    last_name='last_name',
    street='address1',
    city='city',
    state=('state', lambda v: us.states.lookup(v).abbr),
    _state=('state', lambda v: us.states.lookup(v).abbr),
    postal_code='zip',
    country='country'
)

customer = Map(
    first_name='first_name',
    last_name='last_name',
    phone_number='phone',
    email_address='email',
    ip_address='ip_address'
)


