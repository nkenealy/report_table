>>> from report_table.report_table import as_rest_table
>>> data = [('what', 'how', 'who'),
            ('lorem', 'that is a long value', 3.1415),
            ('ipsum', 89798, 0.2)]


storyboard for a demo on usin doctests for docuementing testing and refactoring

------git branch report_table - variables bad and no docstring


The code (without test or docstring) has been sitting there for a while
New ticket is opened, it prints ‘None’ for None values, but we want spaces instead

How to handle a change/refactor ?

Use the code from the command line

   nosetests --with-doctest --with-coverage report_table.py

    from report_table import as_rest_table
    data = [('what', 'how', 'who'),
            ('lorem', 'that is a long value', 3.1415),
            ('ipsum', 89798, 0.2)]

    print as_rest_table(data)

    print as_rest_table(data, title=True)

    print as_rest_table([])


------git branch docstring_bad_variable
Copy/paste into the docstring
Run nose to show test passing and  now getting full coverage


------git branch master
Refactor, renaming variables to sensible names
Tests still pass


Change docstring from No Data to 7 spaces
Tests fail

Update code from No Data to 7 spaces
Test pass



>>> data = [('what', 'how', 'who'),
            ('lorem', 'that is a long value', 3.1415),
            ('ipsum', 89798, 0.2)]


storyboard for a demo on usin doctests for docuementing testing and refactoring

------git branch report_table - variables bad and no docstring


The code (without test or docstring) has been sitting there for a while
New ticket is opened, it prints ‘None’ for None values, but we want spaces instead

How to handle a change/refactor ?

Use the code from the command line

   nosetests --with-doctest --with-coverage report_table.py

    from report_table import as_rest_table
    data = [('what', 'how', 'who'),
            ('lorem', 'that is a long value', 3.1415),
            ('ipsum', 89798, 0.2)]

    print as_rest_table(data)

    print as_rest_table(data, title=True)

    print as_rest_table([])


------git branch docstring_bad_variable
Copy/paste into the docstring
Run nose to show test passing and  now getting full coverage


------git branch master
Refactor, renaming variables to sensible names
Tests still pass


Change docstring from No Data to 7 spaces
Tests fail

Update code from No Data to 7 spaces
Test pass


**Some things to Note**

order of dictionaries can vary so used sorted in the test
 if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0

instead of
  >>> dice_counts([1,1,2,2,2]).items()
    [(1, 2), (2, 3), (3, 0), (4, 0), (5, 0), (6, 0)]

    use
  >>> sorted(dice_counts([1,1,2,2,2]).items())
    [(1, 2), (2, 3), (3, 0), (4, 0), (5, 0), (6, 0)]


output from floats will vary so use round to give a predictable number of decimal places

instead of
>>>  1.0/7
0.142857


>>> round ( 1.0/7 , 6)
0.142857



