from python_dependency_resolver.exceptions import CircularReferenceException


class DependencyResolver:
    def __init__(self, *args, **kwargs):
        self.raise_errors = kwargs.get('raise_errors', True)

    """
        :param node : {
            'A': (),
            'B': ('A'),
            'C': ('B'),
            'D': ('C', 'A'),
            'E': ('C', 'B'),
        }
    """
    def resolve(self, node, resolved=None, unresolved=None):
        if resolved is None:
            resolved = []

        if unresolved is None:
            unresolved = []

        for n in node.keys():
            self.resolver(n, node, resolved, unresolved)
        return [resolved, unresolved]

    def resolver(self, n, node, resolved=None, unresolved=None):
        unresolved.append(n)
        for e in node[n]:
            if e not in resolved:
                if e in unresolved:
                    if self.raise_errors:
                        raise CircularReferenceException(n, e)
                    # avoid infinite loop
                    return
                self.resolver(e, node, resolved, unresolved)

        if n not in resolved:
            resolved.append(n)
        unresolved.remove(n)
