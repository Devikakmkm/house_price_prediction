# Compatibility layer for Python 3.12
import collections.abc
import sys

# Patch collections to include Container and other moved members for Python 3.12+
if sys.version_info >= (3, 12):
    # Add the missing members to collections
    import collections
    collections.Container = collections.abc.Container
    collections.Iterable = collections.abc.Iterable
    collections.MutableSet = collections.abc.MutableSet
    collections.MutableMapping = collections.abc.MutableMapping
    
    # Also patch the collections module to include these in __all__
    if not hasattr(collections, '__all__'):
        collections.__all__ = []
    
    # Add any missing members that might be needed
    for name in ['Container', 'Iterable', 'MutableSet', 'MutableMapping']:
        if name not in collections.__all__:
            collections.__all__.append(name)
