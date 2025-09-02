import twttr

def test_shorten_for_lowercase():
    assert twttr.shorten('khan') == 'khn'

def test_shorten_for_uppercase():
    assert twttr.shorten('KHAN') == 'KHN'

def test_shorten_for_mixedcase():
    assert twttr.shorten('KhAN') == 'KhN'

def test_shorten_for_numbers():
    assert twttr.shorten('12345') == '12345'

def test_shorten_for_punctuation():
    assert twttr.shorten('hello!') == 'hll!'

