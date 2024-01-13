from app import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(5, 3) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(-1, 1) == -2
    assert subtract_numbers(0, 0) == 0

def test_multiply_numbers():
    assert multiply_numbers(5, 3) == 15
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0

def test_divide_numbers():
    assert divide_numbers(6, 3) == 2.0
    assert divide_numbers(5, 2) == 2.5
    assert divide_numbers(0, 5) == 0.0
