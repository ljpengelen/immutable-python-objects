import pytest
from variants.attrs import Point


@pytest.fixture
def point():
    return Point(30, 40)


def test_is_immutable(point):
    with pytest.raises(AttributeError):
        point.x = 50
    with pytest.raises(AttributeError):
        point.y = 60
