===========
Other Stuff
===========

Useful Modules
==============

* `Flake8-pytest <https://pypi.org/project/flake8-pytest/>`_
* `Pytest-Random-Order <https://github.com/jbasko/pytest-random-order>`_
* `Pytest-Replay <https://github.com/ESSS/pytest-replay>`_
* `Pytest-Cov <https://pypi.org/project/pytest-cov/>`_
* `Pytest-Xdist <https://pypi.org/project/pytest-xdist/>`_
* `MonkeyPatch <https://docs.pytest.org/en/latest/monkeypatch.html>`_

Useful Info
===========

If you are using `nosetests <https://nose.readthedocs.io/en/latest/>`_ It
hasn't been maintained since 2016. You need to switch before python 3.9.
This version of python will break nose by moving collection.abc stuff.

If you choose not to switch to Pytest, here are some options:

* `Nose2 <https://github.com/nose-devs/nose2>`_
* `Ward <https://github.com/darrenburns/ward>`_
* `PTR <https://github.com/facebookincubator/ptr>`_
* `UnitTest <https://docs.python.org/3/library/unittest.html#test-discovery>`_
* `StestR <https://pypi.org/project/stestr/>`_ * used by OpenStack

Catch warnings as errors in test suite
======================================

``-Werror`` will should cause any tests that have warning errors for
deprecation messages to cause the test suite to error

.. code-block:: python

    # content of test_show_warnings.py
    import warnings

    def api_v1():
        warnings.warn(UserWarning("api v1, should use functions from v2"))
        return 1

    def test_one():
        assert api_v1() == 1


.. code-block:: shell

    bash-5.0$ pytest -k warnings -Werror| cat
    ============================= test session starts ==============================
    platform darwin -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dwallace/workspace/blog.gtmanfred.com/talks/pytest
    collected 8 items / 7 deselected / 1 selected

    test/test_warnings.py F                                                  [100%]

    =================================== FAILURES ===================================
    ___________________________________ test_one ___________________________________

        def test_one():
    >       assert api_v1() == 1

    test/test_warnings.py:11:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

        def api_v1():
    >       warnings.warn(UserWarning("api v1, should use functions from v2"))
    E       UserWarning: api v1, should use functions from v2

    test/test_warnings.py:6: UserWarning
    ======================= 1 failed, 7 deselected in 0.19s ========================

This can also be configured with the ``filterwarnings`` option in the
pytest config.
