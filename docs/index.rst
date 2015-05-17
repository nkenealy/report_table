.. Tech_talks documentation master file, created by
   sphinx-quickstart on Sun May 17 16:02:56 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

storyboard for doctest and nose demo
====================================
`Bloomberg Polarlake <http://www.polarlake.com>`_.

The demo shows good practice for documenting testing and refactoring with a real-life example


Contents:

.. toctree::
   :maxdepth: 2

   doctest_more
   sphinx_more

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


For more information on doctest, see the :ref:`sphinx_more`

The code **without test or docstring** has been sitting there for a while.
New ticket is opened and assigned to you, it prints ‘No Data’ for None values, but we want spaces instead.
What's the best way to handle a change to the code when you don't really understand how the code works?

Type this from the command line to get the inital version of the code::

    git branch report_table - variables bad and no docstring


To check the code and see how much coverage, use the code from the command line::

    nosetests --with-doctest --with-coverage report_table.py

To find out the best commands to put in the docstring, use this from the python REPL::

    from report_table import as_rest_table
    data = [('what', 'how', 'who'),
            ('lorem', 'that is a long value', 3.1415),
            ('ipsum', 89798, 0.2)]

    print as_rest_table(data)
    print as_rest_table(data, title=True)
    print as_rest_table([])

From Command Line::

    git branch docstring_bad_variable

-Copy/paste into the docstring
-Run nose to show test passing and  now getting full coverage::

  git branch master

Refactor variables to sensible names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-Refactor, renaming variables to sensible names
-Tests still pass

Perform the change requested in JIRA in the docstring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-Change docstring from No Data to 7 spaces
-Tests fail


Change the code
~~~~~~~~~~~~~~~
-Update code from No Data to 7 spaces
-Test pass


For more information on doctest, see the :ref:`doctest_more`






