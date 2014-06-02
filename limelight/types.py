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
        for k, v in kwargs.items():
            self.__map[k] = v if isinstance(v, tuple) else (v, lambda x: x)

    def keys(self):
        for k in self.__map.keys():
            yield k

    def __getitem__(self, item):
        if isinstance(item, slice):
            key, value = item.start, item.stop
            try:
                return self.__map[key][0], self.__map[key][1](value)  # TODO something more sensible
            except:
                return key, value
        elif item in self.__map:
            return self.__map[item][0]
        else:
            return item