====================
What is in Importlib
====================

Documentation
=============

`Docs <https://docs.python.org/3/library/importlib.html>`_

What do I need to know to get started
=====================================

Basic functions
---------------

``importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)``
    Reference implementation of the built-in ``__import__``

``importlib.import_module(name, package=None)``
    Import a module.
      - package is the ``from`` portion if it is required.
      - Simple wrapper around ``importlib.__import__``

The above functions import modules and put them in ``sys.modules``.

``importlib.reload(module)``
    Replacement for the ``reload`` built-in for python2.
    Allows for reimporting a module that may have been saved, without having to
    exit an intepreter.

``importlib.utils.module_from_spec``
    The default module creation
      - Load module and apply ``type(sys)(spec)`` to it
      - Set all the required module attributes

Words to know
-------------

spec

    A specification for a module’s import-system-related state.  This
    includes stuff such as:

        * name (__name__)
        * loader (__loader__)
        * origin (__file__)
        * submodule_search_locations (__path__)
        * parent (__package__)

    Reference implementation `importlib.machinery.ModuleSpec`

module

    A usable object that has been imported into the python namespace.
    A spec loader is used to instantiate (exec) a module object.
