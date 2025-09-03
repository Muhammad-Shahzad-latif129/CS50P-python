import twttr

def test_shorten_for_lowercase():
    assert twttr.shorten('shahzad') == 'shhzd'

def test_shorten_for_uppercase():
    assert twttr.shorten('SHAHZAD') == 'SHHZD'

def test_shorten_for_mixedcase():
    assert twttr.shorten('ShAHZad') == 'ShHZd'

def test_shorten_for_numbers():
    assert twttr.shorten('12345') == '12345'

def test_shorten_for_punctuation():
    assert twttr.shorten('hello!') == 'hll!'

