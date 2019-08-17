=================
The Import System
=================

Import Hooks
============

The Meta Path
-------------

There are 3 Meta Path finders by default

* Built-ins
* Frozen
* Path Entry

These are defined in `sys.meta_path`

Each Finder has a `find_spec` method that finds a spec for loading the modules
that it finds.

.. code-block:: python

    import importlib.machinery
    import sys

    # For illustrative purposes only.
    SpamMetaPathFinder = importlib.machinery.PathFinder
    sys.meta_path.append(SpamMetaPathFinder)


``find_spec``
~~~~~~~~~~~~~

The ``find_spec`` method returns a module spec, which defines information
about the module that will be loaded.

.. code-block:: python

     def find_spec(fullname, path, target=None):
        return None

If a spec is not found, it should return ``None``.

    .. code-block:: python

        # import [fullname]
        import spam.eggs

        # from [package] import [fullname]
        from bacon import spam.eggs

``fullname``
    The full name of the module that is being imported

``path``
    The value of ``__path__`` to look in.  If looking for a top level module,
    path will be ``None``

``target``
    A module object that the finder may use to make a more educated guess about
    what spec to return.


Path Entry Hooks
----------------

Path Finders are called Finders in the same sense as MetaFinders, but they rely
entirely on the Path Entry Finder to be in ``sys.meta_hooks`` for them to be
accessed.

Path finders also have a ``find_spec`` method.

.. code-block:: python

    import importlib.machinery
    import sys

    SpamPathEntryFinder = importlib.machinery.FileFinder
    loader_details = (importlib.machinery.SourceFileLoader,
                      importlib.machinery.SOURCE_SUFFIXES)

    sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))


``find_spec``
~~~~~~~~~~~~~

The find spec for Path Entry Finders is slightly different, because the
PathFinder class defines a path at instantiation, a path is not needed by
``find_spec``

.. code-block:: python

     def find_spec(fullname, target=None):
        return None

If a spec is not found, it should return ``None``.

``fullname``
    The full name of the module that is being imported

``target``
    A module object that the finder may use to make a more educated guess about
    what spec to return.
