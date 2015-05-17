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
    | No Data |
    +---------+

    :param data: list of tuple of the same size
    :return: a ResT table representation
    """
    data = data if data else [['No Data']]
    table = []
    # max size of each column
    sizes = map(max, zip(*[[len(str(elt)) for elt in member]
                           for member in data]))
    num_elts = len(sizes)

    sol = '| '
    vs = ' | '
    eol = ' |'
    meta_template = vs.join(['{{{{{0}:{{{0}}}}}}}'.format(i)
                                             for i in range(num_elts)])
    template = '{0}{1}{2}'.format(sol,
                                  meta_template.format(*sizes),
                                  eol)
    # determine top/bottom borders
    to_separator = string.maketrans('| ', '+-')
    sol = sol.translate(to_separator)
    vs = vs.translate(to_separator)
    eol = eol.translate(to_separator)
    separator = '{0}{1}{2}'.format(sol,
                                   vs.join([x*'-' for x in sizes]),
                                   eol)
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
