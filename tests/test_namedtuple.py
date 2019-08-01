import pytest
from collections import namedtuple
from variants.namedtuple import Point


@pytest.fixture
def point():
    return Point(30, 40)


def test_is_immutable(point):
    with pytest.raises(AttributeError):
        point.x = 50
    with pytest.raises(AttributeError):
        point.y = 60


def test_equality(point):
    assert point == Point(30, 40)
    assert point != Point(40, 30)


def test_unfortunate_equality(point):
    assert point == (30, 40)

    SomethingCompletelyDifferent = namedtuple("SomethingCompletelyDifferent", "a b")
    assert point == SomethingCompletelyDifferent(30, 40)
