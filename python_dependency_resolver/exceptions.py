class CircularReferenceException(Exception):
    def __init__(self, n, e):
        self.node = n
        self.edge = e
        message = 'Circular reference detected: %s -> %s' % (n, e)
        super().__init__(message)