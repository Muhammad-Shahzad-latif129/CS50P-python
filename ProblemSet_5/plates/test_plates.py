import plates

def test_minimum_length():
    assert plates.is_valid("A") == False
    assert plates.is_valid("AB") == True

def test_maximum_length():
    assert plates.is_valid("ABCDEF") == True
    assert plates.is_valid("ABCDEFG") == False

def test_start_with_letters():
    assert plates.is_valid("AB123") == True
    assert plates.is_valid("A1234") == False
    assert plates.is_valid("12ABC") == False

def test_alphanumeric_only():
    assert plates.is_valid("ABC123") == True
    assert plates.is_valid("AB!123") == False
    assert plates.is_valid("AB CD") == False

def test_number_placement():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS05") == False  # cannot start numbers with 0
    assert plates.is_valid("CS50P") == False  # no letters after numbers

def test_all_letters():
    assert plates.is_valid("HELLO") == True
    assert plates.is_valid("WORLD") == True

def test_only_numbers_invalid():
    assert plates.is_valid("1234") == False
