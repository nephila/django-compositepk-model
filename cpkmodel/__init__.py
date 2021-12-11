"""
Package for the application library(Mulit-Column Primary Keys)
"""
__version__ = "2.0.0.dev1"
from .cpkmodel import CPkModel
from .cpkquery import (
    CPkQuery,
    CPkDeleteQuery,
    CPkUpdateQuery,
    CPkQuerySet,
)

__all__ = [
    'CPkModel','CPkQuery','CPkDeleteQuery','CPkUpdateQuery','CPkQuerySet'
]
