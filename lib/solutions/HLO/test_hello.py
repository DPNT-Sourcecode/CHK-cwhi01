from .hello_solution import hello
import pytest

def test_hello_function():
    assert hello("World") == "Hello, World!"