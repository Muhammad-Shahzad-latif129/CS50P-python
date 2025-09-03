import bank

def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO, friend") == 0

def test_h_only():
    assert bank.value("hi") == 20
    assert bank.value("Hey") == 20
    assert bank.value("Hola") == 20

def test_other():
    assert bank.value("Good morning") == 100
    assert bank.value("What's up") == 100
   
