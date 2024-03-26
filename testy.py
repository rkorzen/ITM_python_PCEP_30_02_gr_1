import pytest

def sum(a, b):
    """Return the sum of a and b.
    :param a:
    :param b:
    :return:

    >>> sum(1, 2)
    3
    >>> sum(2, 3)
    6

    """
    return a + b

def div(a, b):
    try:
        return a / b
    except:
        pass

#
#
# def test_sum():
#     assert sum(1, 2) == 3
#
# def test_sum2():
#     assert sum(2, 3) == 5
#
# def test_div():
#     assert div(4, 2) == 2
#
#
# def test_div_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(1, 0)
