from .hello_solution import hello
import pytest

def test_hello_function():
    assert hello("John") == "Hello, John!"
    assert hello("John") != "Hello, World!"