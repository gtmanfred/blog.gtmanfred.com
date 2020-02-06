=================
How to run pytest
=================

Install pytest
==============

.. code-block:: shell

    bash-5.0$ pip install pytest
    Looking in indexes: https://daniel.wallace%40plangrid.com:****@plangrid.artifactoryonline.com/plangrid/api/pypi/pypi/simple
    Collecting pytest
    Downloading https://plangrid.artifactoryonline.com/plangrid/api/pypi/pypi/packages/packages/a5/c0/34033b2df7718b91c667bd259d5ce632ec3720198b7068c0ba6f6104ff89/pytest-5.3.5-py3-none-any.whl (235kB)
        |████████████████████████████████| 235kB 987kB/s
    Requirement already satisfied: attrs>=17.4.0 in /Users/dwallace/.pyenv/versions/3.8.1/lib/python3.8/site-packages (from pytest) (19.3.0)
    Requirement already satisfied: packaging in /Users/dwallace/.pyenv/versions/3.8.1/lib/python3.8/site-packages (from pytest) (20.1)
    Collecting more-itertools>=4.0.0 (from pytest)
    Using cached https://plangrid.artifactoryonline.com/plangrid/api/pypi/pypi/packages/packages/72/96/4297306cc270eef1e3461da034a3bebe7c84eff052326b130824e98fc3fb/more_itertools-8.2.0-py3-none-any.whl
    Collecting py>=1.5.0 (from pytest)
    Using cached https://plangrid.artifactoryonline.com/plangrid/api/pypi/pypi/packages/packages/99/8d/21e1767c009211a62a8e3067280bfce76e89c9f876180308515942304d2d/py-1.8.1-py2.py3-none-any.whl
    Collecting wcwidth (from pytest)
    Using cached https://plangrid.artifactoryonline.com/plangrid/api/pypi/pypi/packages/packages/58/b4/4850a0ccc6f567cc0ebe7060d20ffd4258b8210efadc259da62dc6ed9c65/wcwidth-0.1.8-py2.py3-none-any.whl
    Collecting pluggy<1.0,>=0.12 (from pytest)
    Using cached https://plangrid.artifactoryonline.com/plangrid/api/pypi/pypi/packages/packages/a0/28/85c7aa31b80d150b772fbe4a229487bc6644da9ccb7e427dd8cc60cb8a62/pluggy-0.13.1-py2.py3-none-any.whl
    Requirement already satisfied: pyparsing>=2.0.2 in /Users/dwallace/.pyenv/versions/3.8.1/lib/python3.8/site-packages (from packaging->pytest) (2.4.6)
    Requirement already satisfied: six in /Users/dwallace/.pyenv/versions/3.8.1/lib/python3.8/site-packages (from packaging->pytest) (1.13.0)
    Installing collected packages: more-itertools, py, wcwidth, pluggy, pytest
    Successfully installed more-itertools-8.2.0 pluggy-0.13.1 py-1.8.1 pytest-5.3.5 wcwidth-0.1.8
    WARNING: You are using pip version 19.2.3, however version 20.0.2 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.

Running pytest
==============

Pytest looks for files that meet the format ``test_*.py`` or ``*_test.py``.
Then it looks for any function in that file that starts with ``test*``, and any
method that starts with ``test*`` on a class that starts with ``Test``. This
allows pytest to also run UnitTest style test classes.

.. code-block:: shell

    bash-5.0$ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dwallace/workspace/blog.gtmanfred.com/talks/pytest/test
    collected 5 items

    test_api.py .                                                            [ 20%]
    test_basicmath.py ....                                                   [100%]

    ============================== 5 passed in 0.01s ===============================


Specify certain tests to run
----------------------------

.. code-block:: shell

    bash-5.0$ tail -c +0 test_*.py
    ==> test_api.py <==
    def test_google_com():
        assert True

    ==> test_basicmath.py <==
    def test_addition():
        assert 1 + 1 == 2


    def test_subtraction():
        assert 1 - 1 == 0


    def test_multiplication():
        assert  2 * 3 == 6


    def test_division():
        assert 7 / 2 == 3.5
        assert 7 // 2 == 3
    bash-5.0$ pytest -k basicmath
    ============================= test session starts ==============================
    platform darwin -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dwallace/workspace/blog.gtmanfred.com/talks/pytest/test
    collected 5 items / 1 deselected / 4 selected

    test_basicmath.py ....                                                   [100%]

    ======================= 4 passed, 1 deselected in 0.01s ========================
    bash-5.0$ pytest -k subtraction
    ============================= test session starts ==============================
    platform darwin -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dwallace/workspace/blog.gtmanfred.com/talks/pytest/test
    collected 5 items / 4 deselected / 1 selected

    test_basicmath.py .                                                      [100%]

    ======================= 1 passed, 4 deselected in 0.01s ========================
