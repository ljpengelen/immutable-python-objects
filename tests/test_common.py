import pytest
from variants.attrs import Point as AttrsPoint
from variants.attrs import Point as DataClassPoint
from variants.namedtuple import Point as NamedTuplePoint


@pytest.fixture
def attrs_point():
    return AttrsPoint(10, 20)


@pytest.fixture
def data_class_point():
    return DataClassPoint(30, 40)


@pytest.fixture
def named_tuple_point():
    return NamedTuplePoint(50, 60)


def test_points_can_scale(attrs_point, data_class_point, named_tuple_point):
    for point in [attrs_point, data_class_point, named_tuple_point]:
        scaled_point = point.scale(2)

        assert scaled_point.x == 2 * point.x
        assert scaled_point.y == 2 * point.y


def test_points_can_be_translated(attrs_point, data_class_point, named_tuple_point):
    for point in [attrs_point, data_class_point, named_tuple_point]:
        translated_point = point.translate(2, 3)

        assert translated_point.x == point.x + 2
        assert translated_point.y == point.y + 3
