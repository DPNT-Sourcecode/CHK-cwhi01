from .checkout_solution import checkout

def test_checkout():
    assert checkout("") == 0
    assert checkout("A") == 50
    assert checkout(76) == -1
    assert checkout("ATYEBC") == -1
    assert checkout("AB") == 80
    assert checkout("BBBB") == 90    
    assert checkout("AAAAAA") == 260
    assert checkout("AAAABBCD") == 260    