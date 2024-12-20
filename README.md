[![Python Application](https://github.com/anthonykgross/python-dependency-resolver/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/anthonykgross/python-dependency-resolver/actions/workflows/main.yml)
# python-dependency-resolver


## Install
**From PyPI**
```commandline
pip install python-dependency-resolver
```

**From source**
```commandline
rm build/ python_dependency_resolver.egg-info dist -Rf
python3 setup.py bdist_wheel
pip3 install -I dist/python_dependency_resolver-*-py3-none-any.whl
```

## How to use

***Use case 1***
```mermaid
flowchart TD
    B --> A

    C --> A
    C --> B

    D --> C
    D --> A

    E --> C
    E --> B

    F --> G
```
```python
from python_dependency_resolver import DependencyResolver
tree = {
    'A': [],
    'B': ['A'],
    'C': ['B', 'A'],
    'D': ['C', 'A'],
    'E': ['C', 'B'],
    'F': ['G'],
    'G': []
}

dependency_resolver = DependencyResolver()
dependency_resolver.resolve(tree)
# ['A', 'B', 'C', 'D', 'E', 'G', 'F']
```

***Use case 2***
```mermaid
flowchart TD
    B --> A
    A --> B
```
```python
from python_dependency_resolver import DependencyResolver
tree = {
    'A': ['B'],
    'B': ['A']
}

dependency_resolver = DependencyResolver()
dependency_resolver.resolve(tree)
# CircularReferenceException: Circular reference detected: B -> A
```

***Use case 3***
```mermaid
flowchart TD
    B --> A
    C --> A
```
```python
from python_dependency_resolver import DependencyResolver
tree = {
    'B': ['A'],
    'C': ['A'],
    #'A': ()
}

dependency_resolver = DependencyResolver()
dependency_resolver.resolve(tree)
# MissingReferenceException: Missing reference detected: A
```

**Documentation**
- <https://www.electricmonk.nl/log/2008/08/07/dependency-resolving-algorithm/>
- <http://mamchenkov.net/wordpress/2016/11/22/dependency-resolution-with-graphs-in-php/>

## Contributors
**Anthony K GROSS**
- <http://anthonykgross.fr>
- <https://twitter.com/anthonykgross>
- <https://github.com/anthonykgross>

**Joshua Behrens**
- <https://github.com/JoshuaBehrens>

## Copyright and license
Code and documentation copyright 2024. Code released under [the MIT license](https://github.com/anthonykgross/python-dependency-resolver/blob/main/LICENSE).
