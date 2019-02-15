from __future__ import absolute_import, print_function, division

from .core import SSHCluster

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
