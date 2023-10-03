from palindrome import is_palindrome
import pytest


@pytest.mark.parametrize(
        'test_data', ['', 'a', 'bob','Ne']
)
def test_is_palindrome(test_data):
    assert is_palindrome(test_data)

@pytest.mark.parametrize(
        'test_data2', ['ab', 'boba', 'Never']
)
def test_is_not_palindrome(test_data2):
    assert not is_palindrome(test_data2)
