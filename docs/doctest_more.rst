.. _doctest_more:

What to do when output varies
=============================


Order of dictionaries can vary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

use ``sorted`` in the test::

    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0

instead of::

    dice_counts([1,1,2,2,2]).items()
    [(1, 2), (2, 3), (3, 0), (4, 0), (5, 0), (6, 0)]

use::

  sorted(dice_counts([1,1,2,2,2]).items())
    [(1, 2), (2, 3), (3, 0), (4, 0), (5, 0), (6, 0)]


use round to give a predictable number of decimal places
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

instead of::

    >>>  1.0/7
    0.142857

use::

    >>> round ( 1.0/7 , 6)
    0.142857
