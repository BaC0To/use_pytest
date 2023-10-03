import pytest

@pytest.fixture
def ficture_function():
    return [1, 2, 3]

@pytest.fixture
def test_sum(ficture_function):
    assert sum(ficture_function) == 6

def test_max(ficture_function):
    assert max(ficture_function) == 3