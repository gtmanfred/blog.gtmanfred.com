==============
Plugin Systems
==============

Now that we can load modules and attach them to our application singletons we
just need to be able to figure out where those handlers/tasks are.

``pkg_resources`` entry points
==============================

Entry Points are defined in the setup.py file.

They point to modules that will be loaded.

.. code-block:: python

    setuptools.setup(
        name='test',
        summary='test plugin',
        version='0.0.1a',
        long_description='short',
        author='Daniel Wallace',
        author_email='daniel@gtmanfred.com',
        url='https://github.com/gtmanfred/...',
        packages=['test',],
        entry_points='''
            [test.loader]
            test.dirs = test.handlers
        ''',
    )

Once you have an entry point to iterate over, instead of having to hard code a
path, just use the path of your entry point.

Before python 3.8

.. code-block:: python

    import pkg_resources

    for entry in pkg_resources.iter_entry_points('test.loader', name='test.dirs':
        directory = entry.load()
        if not directory.__file__:
            # namespace package
            path = directory.__path__._path[0]
        else:
            path = directory.__file__
        ...


After python 3.8

.. code-block:: python

   from importlib.metadata import entry_points

   for entry in entry_points(group='test.loader', name='test.dirs'):
        directory = entry.load()
        if not directory.__file__:
            # namespace package
            path = directory.__path__._path[0]
        else:
            path = directory.__file__
        ...


``stevedore``
=============

stevedore_ is another entry_points plugin loader that can be used to iterate
and is slightly faster than pkg_resources and has some extra stuff that it can
keep track of.

Config Management
=================

If you want some fun importlib stuff to look at, SaltStack_ and Ansible_ both
do some fun stuff with importlib.

``pop``
=======

SaltStack is also manages a new opensource loader system with a hub, which is
really interesting.  It is called pop_

.. _stevedore: https://docs.openstack.org/stevedore/latest/
.. _SaltStack: https://github.com/saltstack/salt/tree/develop/salt/loader.py
.. _Ansible: https://github.com/ansible/ansible/blob/devel/lib/ansible/executor/module_common.py
