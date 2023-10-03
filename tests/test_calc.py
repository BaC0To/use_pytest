from calc import sum_positive, sum_negative


def test_positive_sum():
    result = sum_positive(2,3)
    assert result , 5
    result2 = sum_positive(-2,3)
    assert result2 == None

def test_negative_sum():
    result = sum_negative(2,3)
    assert result == None
    result2 = sum_negative(-2,-3)
    assert result2 == -5