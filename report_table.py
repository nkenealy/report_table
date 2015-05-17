import string


def as_rest_table(data, title=False):
    """ nosetests --with-doctest --with-coverage report_table.py

    >>> from report_table import as_rest_table
    >>> data = [('what', 'how', 'who'),
    ...        ('lorem', 'that is a long value', 3.1415),
    ...        ('ipsum', 89798, 0.2)]

    >>> print as_rest_table(data)
    +-------+----------------------+--------+
    | what  | how                  | who    |
    | lorem | that is a long value | 3.1415 |
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+

    >>> print as_rest_table(data, title=True)
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +-------+----------------------+--------+
    | lorem | that is a long value | 3.1415 |
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+

    >>> print as_rest_table([])
    +---------+
    | No data |
    +---------+

    :param data: list of tuple of the same size
    :return: a ResT table representation
    """
    data = data if data else [['No data']]
    table = []
    # max size of each column
    sizes = map(max, zip(*[[len(str(elt)) for elt in member]
                           for member in data]))
    num_elts = len(sizes)

    start_of_line = '| '
    vertical_separator = ' | '
    end_of_line = ' |'
    meta_template = vertical_separator.join(['{{{{{0}:{{{0}}}}}}}'.format(i)
                                             for i in range(num_elts)])
    template = '{0}{1}{2}'.format(start_of_line,
                                  meta_template.format(*sizes),
                                  end_of_line)
    # determine top/bottom borders
    to_separator = string.maketrans('| ', '+-')
    start_of_line = start_of_line.translate(to_separator)
    vertical_separator = vertical_separator.translate(to_separator)
    end_of_line = end_of_line.translate(to_separator)
    separator = '{0}{1}{2}'.format(start_of_line,
                                   vertical_separator.join([x*'-' for x in sizes]),
                                   end_of_line)
    # prepare result
    table.append(separator)
    if title:
        titles = data.pop(0)
        table.append(template.format(*titles))
        table.append(separator)

    for d in data:
        table.append(template.format(*d))
    table.append(separator)
    return '\n'.join(table)

# data = [('what', 'how', 'who'),
#         ('lorem', 'that is a long value', 3.1415),
#         ('ipsum', 89798, 0.2)]
# # data = [('what', 'how', ), ('lorem', 'val111111111', ), ('ipsum', '89798', )]
#
# print as_rest_table(data)
# print as_rest_table(())
