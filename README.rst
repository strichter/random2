========
Random 2
========

.. image:: https://github.com/strichter/random2/actions/workflows/test.yml/badge.svg
   :target: https://github.com/strichter/random2/actions

.. image:: https://img.shields.io/pypi/v/random2.svg
   :target: https://pypi.python.org/pypi/random2

.. image:: https://img.shields.io/pypi/pyversions/random2.svg
   :target: https://pypi.python.org/pypi/random2/

This package provides a Python 3 ported version of Python 2.7's ``random``
module. It has also been back-ported to work in Python 2.6.

In Python 3, the implementation of ``randrange()`` was changed, so that even
with the same seed you get different sequences in Python 2 and 3. Note that
several high-level functions such as ``randint()`` and ``choice()`` use
``randrange()``.

In my testing code I heavily rely on stable random generator results and it
makes porting code to Python 3 a lot harder, if all those tests have to be
adjusted. This package fixes that.
