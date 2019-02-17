"""Some helpful functions for EECS 230."""

from typing import Optional
import attr


def record(*args, **kwargs):
    if 'auto_attribs' in kwargs:
        return attr.s(*args, **kwargs)
    else:
        return attr.s(*args, auto_attribs=True, **kwargs)


Factory = attr.Factory


def putstr(s: str) -> None:
    """Prints a string without a terminating newline.

    >>> putstr('hello, world')
    hello, world
    >>> putstr('hello, world\\n')
    hello, world
    """
    print(s, end='')


def read_float(prompt: str = '') -> Optional[float]:
    """Attempts to read a float from the standard input.
    Prompts and tries again if the input cannot be parsed.
    Returns `None` on EOF.
    """
    while True:
        try:
            return float(input(prompt))
        except EOFError:
            return None
        except ValueError as e:
            print("Parse error:", e)


def read_int(prompt: str = '') -> Optional[int]:
    """Attempts to read a int from the standard input.
    Prompts and tries again if the input cannot be parsed.
    Returns `None` on EOF.
    """
    while True:
        try:
            return int(input(prompt))
        except EOFError:
            return None
        except ValueError as e:
            print("Parse error:", e)

