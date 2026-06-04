"""Helper utilities used by :mod:`easy_exit_calls`."""

from .decorator import register_exit_handler
from .handler_list import HandlerList

__all__ = ["register_exit_handler", "HandlerList"]
