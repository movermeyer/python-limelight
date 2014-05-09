# -*- coding: utf-8 -*-


class Map(object):
    """
    A weird object that maps local field names to lime light field name, also supports
    value conversions.
    """
    def __init__(self, **kwargs):
        self.__map = {}
        for k, v in kwargs.iteritems():
            self.__map[k] = v if isinstance(v, tuple) else (v, lambda x: x)

    def keys(self):
        for k in self.__map.iterkeys():
            yield k

    def __call__(self, *args):
        map_tuple = self.__map[args[0]]
        if len(args) == 2:
            return map_tuple[0], map_tuple[1](args[1])
        else:
            return map_tuple[0]


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
    state='state',
    _state='state',
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


