# -*- coding: utf-8 -*-


class Map(object):
    """
    An object that maps field names to each other, also supports value conversions.

    :param str or tuple(str, function) kwargs: Keyword arguments that define values to map to, and
                                               an optional conversion function.
    """
    __slots__ = ['__map']

    def __init__(self, **kwargs):
        self.__map = {}
        for k, v in kwargs.iteritems():
            self.__map[k] = v if isinstance(v, tuple) else (v, lambda x: x)

    def keys(self):
        for k in self.__map.iterkeys():
            yield k

    def __getitem__(self, item):
        if isinstance(item, slice):
            try:
                key, value = item.start, item.stop
                return self.__map[key][0], self.__map[key][1](value)
            except:
                return key, value
        elif item in self.__map:
            return self.__map[item][0]
        else:
            return item