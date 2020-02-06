=============================
How to write tests for pytest
=============================

While you can use the ``unittest.TestCase`` class for writing tests for pytest,
I strongly recommend using functions as they are widely considered to be more
pythonic.

From the docs:

    The Python unit testing framework, sometimes referred to as “PyUnit,”
    is a Python language version of JUnit, by Kent Beck and Erich Gamma.
    JUnit is, in turn, a Java version of Kent’s Smalltalk testing framework.
    Each is the de facto standard unit testing framework for its respective
    language.

Be more pythonic, not like java.

Pytest and the Assert Statement
===============================

Pytest allows you to use the standard python assert for verifying expectations
and values in Python tests.

Simple Test Case
----------------

.. code-block:: python

    def test_addition():
        assert 1 + 1 == 2


Test Function Output
--------------------

.. code-block:: python

    def f():
        return 4

    def test_f():
        assert f() == 4


Test an API
-----------

.. code-block:: python

    import json
    import urllib3

    def test_petstore_inventory():
        http = urllib3.PoolManager()
        url = 'https://petstore.swagger.io/v2/store/inventory'
        ret = http.request('GET', url)
        assert json.loads(ret.data)[' not available'] == 1


Test Exceptions
---------------

.. code-block:: python

    import pytest

    def raise_exception():
        raise ConnectionError('failed to connect')

    def test_for_connection_failure():
        with pytest.raises(ConnectionError) as excinfo:
            raise_exception()
        assert 'failed to connect' in str(excinfo)
