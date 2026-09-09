"""
Defines the :class:`OpaqueKey` class, to be used as the base-class for
implementing pluggable OpaqueKeys.

These keys are designed to provide a limited, forward-evolveable interface to
an application, while concealing the particulars of the serialization
formats, and allowing new serialization formats to be installed transparently.
"""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from functools import total_ordering
from typing import Self

from importlib.metadata import version

from stevedore.enabled import EnabledExtensionManager

__version__ = version("edx-opaque-keys")
