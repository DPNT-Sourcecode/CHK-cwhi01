from .checkout_solution import checkout

def test_checkout():

    assert checkout(76) == -1
    assert checkout("£$AC@") == -1

    assert checkout("") == 0
    assert checkout("A") == 50
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

    assert checkout("HHHHH") == 45
    assert checkout("HHHHHHHHHHH") == 90

    assert checkout("KK") == 150

    assert checkout("NNNNM") == 160

    assert checkout("PPPPP") == 200

    assert checkout("RRRQ") == 150
    assert checkout("RRRRRRQQQ") == 330

    assert checkout("UUUU") == 120

    assert checkout("VVVV") == 180

    assert checkout("STX") == 45
    assert checkout("XYZ") == 45
    assert checkout("STXYZS") == 90
    assert checkout("STZZ") == 65

    assert checkout("STXAAA") == 175
    assert checkout("STXYZAAAEEB") == 285




