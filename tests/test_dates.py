import pytest
from datetime import datetime, timedelta
from date_diff import calc_date_diff


data = [(datetime(2023, 10, 3), datetime(2023, 10, 2), timedelta(1)),
        (datetime(2023, 10, 3), datetime(2023, 10, 3), timedelta(0)),
        ]


@pytest.mark.parametrize('a, b, expected', data)
def test_date_difference(a, b, expected):
    result = calc_date_diff(a, b)
    assert result == expected