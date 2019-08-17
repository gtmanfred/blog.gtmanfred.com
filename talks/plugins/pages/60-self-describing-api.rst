============================
Time to build an application
============================


Application Loader
==================

``app/__init__.py``

.. code-block:: python

    import collections
    import importlib.machinery
    import importlib.util
    import inspect
    import os
    import pathlib

    import flask
    import flask_restful

    Handler = collections.namedtuple('Handler', ['name', 'klass'])


    class HandlerLoader(importlib.abc.SourceLoader):

        def __init__(self, fullname, path):
            """Cache the module name and the path to the file found by the
            finder."""
            self.name = fullname
            self.path = path

        def get_filename(self, fullname):
            return self.path

        def get_data(self, path):
            with open(path, 'rb') as codefile:
                return codefile.read()

        @staticmethod
        def create_resource(blueprint):
            setattr(
                blueprint,
                'methods',
                list(map(
                    lambda item: next(iter(item)).upper(),
                    inspect.getmembers(blueprint, inspect.isfunction)
                ))
            )
            return type(blueprint.__name__, (blueprint, flask_restful.Resource), {})

        def exec_module(self, module):
            super().exec_module(module)
            version = getattr(module, '__version__', 1)
            app = flask.Blueprint(module.__name__, module.__name__)
            api = flask_restful.Api(app)

            for obj in inspect.getmembers(module, lambda x: inspect.isclass(x) and hasattr(x, 'uri')):
                blueprint = Handler(*obj)
                api.add_resource(self.create_resource(blueprint.klass), f'/api/v{version}{blueprint.klass.uri}')
            return app

    def create_app():
        app = flask.Flask('test')
        loader_details = [
            (HandlerLoader, importlib.machinery.SOURCE_SUFFIXES),
        ]

        handler_dir = f'{os.path.dirname(__file__)}/handlers/'
        finder = importlib.machinery.FileFinder(handler_dir, *loader_details)

        for entry in pathlib.Path(handler_dir).iterdir():
            if entry.name in ('__init__.py', ):
                continue

            # use the FileFinder to find the spec for `entry` module in `path`
            modname, _ = os.path.splitext(entry.name)
            spec = finder.find_spec(modname)
            if not spec.loader:
                continue
            module = importlib.util.module_from_spec(spec)
            app.register_blueprint(spec.loader.exec_module(module))

        return app


Handler
=======

``app/handlers/ping.py``

.. code-block::

    class Ping:

        uri = '/ping'

        def get(self):
            return {"response": True}
