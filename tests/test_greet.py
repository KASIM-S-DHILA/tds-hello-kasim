import pytest
from tds_hello_kasim import greet


def test_default():
    assert greet() == "Hello, world! — from tds-hello v0.1.0"


def test_custom_name():
    assert "Alice" in greet("Alice")


def test_invalid_type():
    with pytest.raises(TypeError):
        greet(42)  # type: ignore[arg-type]
