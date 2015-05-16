import string


def as_rest_table(data, title=False):

    data = data if data else [['No Data']]
    table = []
    # max size of each column
    sizes = map(max, zip(*[[len(str(elt)) for elt in member]
                           for member in data]))
    num_elts = len(sizes)

    sol = '| '
    vs = ' | '
    eol = ' |'
    meta_tmpl = vs.join(['{{{{{0}:{{{0}}}}}}}'.format(i)
                                             for i in range(num_elts)])
    tmpl = '{0}{1}{2}'.format(sol,
                                  meta_tmpl.format(*sizes),
                                  eol)
    # determine top/bottom borders
    to_sep = string.maketrans('| ', '+-')
    sol = sol.translate(to_sep)
    vs = vs.translate(to_sep)
    eol = eol.translate(to_sep)
    sep = '{0}{1}{2}'.format(sol,
                                   vs.join([x*'-' for x in sizes]),
                                   eol)
    # prepare result
    table.append(sep)
    if title:
        titles = data.pop(0)
        table.append(tmpl.format(*titles))
        table.append(sep)

    for d in data:
        table.append(tmpl.format(*d))
    table.append(sep)
    return '\n'.join(table)

# data = [('what', 'how', 'who'),
#         ('lorem', 'that is a long value', 3.1415),
#         ('ipsum', 89798, 0.2)]
# # data = [('what', 'how', ), ('lorem', 'val111111111', ), ('ipsum', '89798', )]
#
# print as_rest_table(data)
# print as_rest_table(())
