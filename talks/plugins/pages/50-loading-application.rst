========
Examples
========


Importing Programatically
==========================

.. code-block:: python

    import importlib

    itertools = importlib.import_module('itertools')

Checking if a module is importable
==================================

.. code-block:: python

    import importlib.util
    import sys

    # For illustrative purposes.
    name = 'itertools'

    if name in sys.modules:
        print(f"{name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(name)) is not None:
        # If you chose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        print(f"{name!r} has been imported")
    else:
        print(f"can't find the {name!r} module")


Import a source file directly
=============================

.. code-block:: python

    import importlib.util
    import sys

    # For illustrative purposes.
    import tokenize
    file_path = tokenize.__file__
    module_name = tokenize.__name__

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


Approximate ``importlib.import_module``
=======================================

.. code-block:: python

    import importlib.util
    import sys

    def import_module(name, package=None):
        """An approximate implementation of import."""
        absolute_name = importlib.util.resolve_name(name, package)
        try:
            return sys.modules[absolute_name]
        except KeyError:
            pass

        path = None
        if '.' in absolute_name:
            parent_name, _, child_name = absolute_name.rpartition('.')
            parent_module = import_module(parent_name)
            path = parent_module.__spec__.submodule_search_locations
        for finder in sys.meta_path:
            spec = finder.find_spec(absolute_name, path)
            if spec is not None:
                break
        else:
            msg = f'No module named {absolute_name!r}'
            raise ModuleNotFoundError(msg, name=absolute_name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[absolute_name] = module
        spec.loader.exec_module(module)
        if path is not None:
            setattr(parent_module, child_name, module)
        return module

Other Examples
==============

* `strip-hints <https://github.com/abarker/strip-hints/blob/master/src/strip_hints/import_hooks_py3.py>`_
