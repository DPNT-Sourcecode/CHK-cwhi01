from .checkout_solution import checkout

def test_checkout():
    assert checkout("") == 0
    assert checkout("A") == 50
    assert checkout(76) == -1
    assert checkout("ATYEBC") == -1