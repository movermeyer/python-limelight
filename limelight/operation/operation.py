# -*- coding: utf-8 -*-


class Operation(object):
    def order_update:
        urllib2.urlopen(
            tx.endpoint + '/admin/membership.php',
            urllib.urlencode({
                'username': tx.username,
                'password': tx.password,
                'method': 'order_update',
                'order_ids': int(response.order_id),
                'actions': 'notes',
                'values': '"%s, %s"' % (buyer.company, buyer.coaching_number), }),
            timeout=12).read()