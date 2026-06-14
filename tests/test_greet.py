import pytest
from tds_hello_kasim import greet, shout


def test_default():
    assert greet() == "Hello, world! — from tds-hello v0.2.0"


def test_custom_name():
    assert "Alice" in greet("Alice")


def test_invalid_type():
    with pytest.raises(TypeError):
        greet(42)  # type: ignore[arg-type]


def test_shout_default():
    assert shout() == greet("world").upper()


def test_shout_custom_name():
    result = shout("Alice")
    assert result == greet("Alice").upper()
    assert result.isupper()


def test_shout_invalid_type():
    with pytest.raises(TypeError):
        shout(42)  # type: ignore[arg-type]
