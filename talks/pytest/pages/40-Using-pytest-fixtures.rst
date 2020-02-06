=====================
Using Pytest Fixtures
=====================

Lots of projects now provide their own pytest fixtures for testing applications
that use their libraries. Here are some that I use often:

* `Pytest-Flask <https://pypi.org/project/pytest-flask/>`_
* `Pytest-Django <https://pypi.org/project/pytest-django/>`_
* `Celery <https://docs.celeryproject.org/en/stable/userguide/testing.html>`_
* `Redis <https://pypi.org/project/pytest-redis/>`_
* `Moto <https://pypi.org/project/pytest-moto/>`_
* `Pytest-Docker <https://pypi.org/project/pytest-docker/>`_

Pytest fixtures can provide commonly used objects or push app contexts.


Scope of Fixtures
=================

Session
-------

Lives for the entire session.

Can depend on:

* Session

Module
------

Lives for the module

Can depend on:

* Module
* Session

Function
--------

This is the default.

Recreated for every function.

Can Depend on:

* Function
* Module
* Session

Basic Fixtures
==============

Writing a fixture for an http client
------------------------------------

.. code-block:: python

    import json
    import pytest
    import urllib3

    @pytest.fixture(scope='session')
    def http():
        return urllib3.PoolManager()

    def test_petstore_inventory(http):
        url = 'https://petstore.swagger.io/v2/store/inventory'
        ret = http.request('GET', url)
        assert json.loads(ret.data)[' not available'] == 1


Using yield fixtures to replace setup/teardown
----------------------------------------------

.. code-block::

    import docker
    import pytest

    @pytest.fixture(scope='session')
    def docker_client():
        return docker.from_env()

    @pytest.fixture(scope='session')
    def postgres(docker_client):
        container = docker_client.containers.run("postgres:9.6", detach=True)
        yield container
        container.stop()
        container.remove()

    def test_db(postgres):
        assert 'postgres:9.6' in postgres.image.tags
