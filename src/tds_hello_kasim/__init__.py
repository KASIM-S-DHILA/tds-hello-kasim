"""tds-hello — a tiny greeter from the TDS 2026 course."""

from importlib.metadata import version as _v

__version__ = _v("tds-hello-kasim")


def greet(name: str = "world") -> str:
    """Return a friendly greeting with the package version."""
    if not isinstance(name, str):
        raise TypeError("name must be a str")
    return f"Hello, {name}! — from tds-hello v{__version__}"


def shout(name: str = "world") -> str:
    return greet(name).upper()
