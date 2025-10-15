class MyFilter:
    def __init__(self, function, iterable):
        self.function = function if function else bool
        self.iterable = iter(iterable)

    def __iter__(self):
        self.iterable = iter([element for element in self.iterable
                              if self.function(element)])
        return self.iterable


def ft_filter(function, iterable):
    '''
 ft_filter(function or None, iterable) --> ft_filter.MyFilter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
'''

    return MyFilter(function, iterable)
