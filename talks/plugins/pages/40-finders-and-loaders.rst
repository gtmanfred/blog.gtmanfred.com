===================
Finders and Loaders
===================


Abstract Classes
================


Finders
=======

There are two basic Abstract Finder Classes in ``importlib``. They correspond
to the two types of import hooks.

``importlib.machinery.MetaPathFinder``
    For creating a ``sys.meta_path`` hook

``importlib.machinery.PathEntryFinder``
    For creating a ``sys.path_hooks`` hook


Loaders
=======

Once a finder has found a spec, it needs to be converted to a module, and then
loaded.

Loaders really have two functions ``create_module`` and ``exec_module``.

``create_module``
    Most loaders will not have a ``create_module`` method that does anything.
    If they do not need to do anything special, they can just return ``None``,
    and the default module creation from ``importlib.utils.module_from_spec``
    will be used.

``exec_module``
    This method excutes the module in its own namespace when a module is
    imported or reloaded.

There are 5 abstract Loaders in the ``importlib.machinery``:

Loader hierarchy::

     Loader
     +-- ResourceLoader --------+
     +-- InspectLoader          |
         +-- ExecutionLoader --+
             +-- FileLoader
             +-- SourceLoader

There are two that we are going to use.

``FileLoader``
    An abstract base class which inherits from ``ResourceLoader`` and
    ``ExecutionLoader``, providing concrete implementations of
    ``ResourceLoader.get_data()`` and ``ExecutionLoader.get_filename()``.

``SourceLoader``
    An abstract base class for implementing source (and optionally bytecode)
    file loading. The class inherits from both ``ResourceLoader`` and
    ``ExecutionLoader``, requiring the implementation of:

    - ``ResourceLoader.get_data``
    - ``ExecutionLoader.get_filename``

When these are used together they are a decent reference implementation that
can import modules.


.. code-block:: python

    from importlib.machinery import FileFinder, SOURCE_SUFFIXES, SourceFileLoader
    from importlib._bootstrap import _init_module_attrs
    from types import ModuleType
    import sys

    finder = FileFinder('/usr/lib/python3.7/', (SourceFileLoader, SOURCE_SUFFIXES))
    spec = finder.find_spec('os')

    module = None
    if spec.loader is not None and hasattr(spec.loader, 'create_module'):
        # It is assumed 'exec_module' will also be defined on the loader.
        module = spec.loader.create_module(spec)
    if module is None:
        module = ModuleType(spec.name)
    # The import-related module attributes get set here:
    _init_module_attrs(spec, module)

    if spec.loader is None:
        if spec.submodule_search_locations is not None:
            # namespace package
            sys.modules[spec.name] = module
        else:
            # unsupported
            raise ImportError
    elif not hasattr(spec.loader, 'exec_module'):
        module = spec.loader.load_module(spec.name)
        # Set __loader__ and __package__ if missing.
    else:
        sys.modules[spec.name] = module
        try:
            spec.loader.exec_module(module)
        except BaseException:
            try:
                del sys.modules[spec.name]
            except KeyError:
                pass
            raise
