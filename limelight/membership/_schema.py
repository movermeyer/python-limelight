# -*- coding: utf-8 -*-

import six

from voluptuous import All, Length, Any

from .. import validate


condition_for = {'order_ids': [int],                       # order_update
                 'actions': [six.u],
                 'values': [Any(six.u, int)],
                 'campaign_id': [int],                     # order_find
                 'start_date': validate.date('%m/%d/%Y'),
                 'end_date': validate.date('%m/%d/%Y'), }