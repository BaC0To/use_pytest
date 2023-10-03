import pytest
from datetime import datetime, timedelta
from date_diff import calc_date_diff


data = [(datetime(2023, 10, 3), datetime(2023, 10, 2), timedelta(1) ),
        (datetime(2023, 10, 3), datetime(2023, 10, 3), timedelta(0) ),
        (datetime(2023, 10, 3), datetime(2023, 9, 1), timedelta(32) ),
        ]



@pytest.mark.parametrize('a, b, expected', data)
def test_date_difference_v0(a, b, expected):
    result = calc_date_diff(a, b)
    assert result == expected

@pytest.mark.parametrize('a, b, expected', data, ids=["trial0", "trial1","trial2"])
def test_date_difference_v1(a, b, expected):
    result = calc_date_diff(a, b)
#     if result <= timedelta(31):
#         over_month = True
#     else:
#         over_month = False
    assert result == expected
#     assert over_month == month_expired

def idfn(val):
    if isinstance(val, (datetime, )):
        # note this wouldn't show any hours/minutes/seconds
        return val.strftime("%Y%m%d")

@pytest.mark.parametrize("a,b,expected", data, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected

@pytest.mark.parametrize("a,b,expected",
        [
        pytest.param(datetime(2001, 12, 14), datetime(2001, 12, 11), timedelta(3), id="???"),
        pytest.param(datetime(2001, 12, 10), datetime(2001, 12, 12), timedelta(-2), id="!!!"),
        pytest.param(datetime(2001, 12, 10), datetime(2001, 12, 12), timedelta(-2))
        ],
)
def test_timedistance_v3(a, b, expected):
    diff = a - b
    assert diff == expected