import pytest

@pytest.fixture
def fixture_function():
    return [1, 2, 3]

@pytest.fixture
def test_sum(fixture_function):
    assert sum(fixture_function) == 6

@pytest.fixture
def test_max(fixture_function):
    assert max(fixture_function) == 3