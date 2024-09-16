from .checkout_solution import checkout

def test_checkout():
    assert checkout("") == 0
    assert checkout("A") == 50
    assert checkout(76) == -1
    assert checkout("ATYEBC") == -1
    assert checkout("£$AC@") == -1
    assert checkout("AB") == 80
    assert checkout("BBBB") == 90    
    assert checkout("AAAAAA") == 250
    assert checkout("AAAABBCD") == 260   
    assert checkout("ABCDE") == 155
    assert checkout("EEBBB") == 125
    assert checkout("AAAAAEEBAAABB") == 455 
    assert checkout("FF") == 20
    assert checkout("FFF") == 20
    assert checkout("FFFF") == 30
    assert checkout("FFFFFEE") == 120



