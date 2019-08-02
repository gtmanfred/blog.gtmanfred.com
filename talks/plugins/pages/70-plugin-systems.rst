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
        url='https://github.com/.../...',
        packages=['test',],
        entry_points='''
            [test.loader]
            test.plugins = test.handlers
        ''',
    )

Once you have an entry point to iterate over, instead of having to hard code a
path, just use the path of your entry point.

.. code-block:: python

    import pkg_resources

    for handler_dir in pkg_resources.iter_entry_points('test.plugins'):
        path = os.path.dirname(handler_dir.__file__)
        ...

``stevedore``
=============

stevedore_ is another
entry_points plugin loader that can be used to iterate and is slightly faster
than pkg_resources and has some extra stuff that it can keep track of.

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
