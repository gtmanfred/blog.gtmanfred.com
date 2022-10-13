============
Introduction
============

Who am I
========

`Twitter -> gtmanfred <https://twitter.com/gtmanfred>`_

`Github -> gtmanfred <https://github.com/gtmanfred>`_

Previous Work:
  - Rackspace
  - SaltStack

Currently: Autodesk - Senior Principal Engineer

What is the goal of this talk?
==============================

Goals for talk:
  - Have a better idea of how ``import`` inside of python works
  - Be able to describe how to augment the import structure in python
  - Use importlib and some other fun python stuff to build a framework for building simple app handlers.

Make this work:

``app/handlers/ping.py``

.. code-block::

    class Ping:

        uri = '/ping'

        def get(self):
            return {"response": True}
