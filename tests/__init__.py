import unittest
from python_dependency_resolver import DependencyResolver
from python_dependency_resolver.exceptions import CircularReferenceException, MissingReferenceException


class DependencyResolverTestCase(unittest.TestCase):
    """
        v ----------------|
        A <-- B <-- C <-- D
              ^     ^
              |--E--|
    """

    def test_resolve(self):
        tree = {
            'A': (),
            'B': ('A'),
            'C': ('B', 'A'),
            'D': ('C', 'A'),
            'E': ('C', 'B'),
            'F': ('G'),
            'G': ()
        }

        dependency_resolver = DependencyResolver()
        r = dependency_resolver.resolve(tree)
        self.assertEqual(r[0], ['A', 'B', 'C', 'D', 'E', 'G', 'F'])
        self.assertEqual(r[1], [])

    """
                <-- A  
        D <-- C
                <-- B
    """
    def test_resolve_graph(self):
        tree = {
            'A': ('C'),
            'B': ('C'),
            'C': ('D'),
            'D': (),
        }

        dependency_resolver = DependencyResolver()
        r = dependency_resolver.resolve(tree)
        self.assertEqual(r[0], ['D', 'C', 'A', 'B'])

    def test_missing_dependency(self):
        tree = {
            'A': (),
            'B': ('A'),
            'C': ('B', 'A'),
            'D': ('C', 'A'),
            'E': ('C', 'B'),
            'F': ('G'),
            # 'G': ()
        }

        dependency_resolver = DependencyResolver()
        with self.assertRaises(MissingReferenceException) as e:
            r = dependency_resolver.resolve(tree)
        self.assertEqual(str(e.exception), 'Missing reference detected: G')

        dependency_resolver = DependencyResolver(raise_errors=False)
        r = dependency_resolver.resolve(tree)
        self.assertEqual(r[0], ['A', 'B', 'C', 'D', 'E', 'F'])
        self.assertEqual(r[1], ['G'])

    """
         < ------|
        A        B
        |------ >
    """
    def test_circular_dependency(self):
        tree = {
            'A': ('B'),
            'B': ('A'),
        }

        dependency_resolver = DependencyResolver()
        with self.assertRaises(CircularReferenceException) as e:
            r = dependency_resolver.resolve(tree)
        self.assertEqual(str(e.exception), 'Circular reference detected: B -> A')

        dependency_resolver = DependencyResolver(raise_errors=False)
        r = dependency_resolver.resolve(tree)
        self.assertEqual(r[0], ['A', 'B'])
        self.assertEqual(r[1], ['B'])
