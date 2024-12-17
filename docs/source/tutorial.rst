=============
Tutorial
=============

This tutorial introduces **python-dependency-resolver** by means of example - we will walk through how to
create a simple ordered todo list.

Getting started
===============

Before we start, we have to install **python-dependency-resolver**.

.. code-block::

    $ python -m pip install python-dependency-resolver

We have to create a ``main.py`` file and import **python-dependency-resolver**.

.. note:: You can see our examples on `Github <https://github.com/anthonykgross/python-dependency-resolver/tree/main/examples/>`_

What do we have to do
=====================

My todo list is :

- Buying food
- Cooking
- Feeding kitties
- Feeding my self
- Doing the dishes
- Learning a new recipe
- Buying a cookbook

.. code-block:: python

    # main.py
    from python_dependency_resolver import DependencyResolver

    # [
    #   my task: [requirements]
    # ]
    tree = {
        'Buying food': ['Learning a new recipe'],
        'Cooking': ['Buying food', 'Learning a new recipe'],
        'Feeding kitties': [],
        'Feeding my self': ['Cooking'],
        'Doing the dishes': ['Feeding my self', 'Feeding kitties'],
        'Learning a new recipe': ['Buying a cookbook'],
        'Buying a cookbook': []
    }

    dependency_resolver = DependencyResolver()
    result, unsolved = dependency_resolver.resolve(tree)
    # [['Buying a cookbook', 'Learning a new recipe', 'Buying food', 'Cooking', 'Feeding kitties', 'Feeding my self', 'Doing the dishes'], []]

