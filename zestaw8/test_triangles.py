import pytest
from points import Point
from triangles import Triangle

@pytest.fixture
def triangle():
    return Triangle(0, 0, 0, 2, 2, 0)


def test_init_and_is_collinear(triangle):
    assert triangle.pt1 == Point(0, 0)
    assert triangle.pt2 == Point(0, 2)
    assert triangle.pt3 == Point(2, 0)

    with pytest.raises(ValueError):
        Triangle(0, 0, 1, 1, 2, 2)

def test_from_points():
    p1, p2, p3 = Point(0, 0), Point(0, 2), Point(2, 0)
    triangle = Triangle.from_points((p1, p2, p3))
    assert triangle.pt1 == p1
    assert triangle.pt2 == p2
    assert triangle.pt3 == p3

    with pytest.raises(ValueError):
        Triangle.from_points((p1, p2))


def test_str_and_repr(triangle):
    assert str(triangle) == "[(0, 0), (0, 2), (2, 0)]"
    assert repr(triangle) == "Triangle(0, 0, 0, 2, 2, 0)"


def test_properties(triangle):
    assert triangle.center == Point(2 / 3, 2 / 3)
    assert triangle.top == 2
    assert triangle.left == 0
    assert triangle.bottom == 0
    assert triangle.right == 2
    assert triangle.width == 2
    assert triangle.height == 2
    assert triangle.topleft == Point(0, 2)
    assert triangle.bottomleft == Point(0, 0)
    assert triangle.topright == Point(2, 2)
    assert triangle.bottomright == Point(2, 0)


def test_area(triangle):
    assert triangle.area() == 2


def test_move(triangle):
    triangle.move(1, 1)
    assert triangle.pt1 == Point(1, 1)
    assert triangle.pt2 == Point(1, 3)
    assert triangle.pt3 == Point(3, 1)


def test_make4(triangle):
    divided_triangles = triangle.make4()
    assert len(divided_triangles) == 4
    area = sum(i.area() for i in divided_triangles)
    assert pytest.approx(area) == triangle.area()


if __name__ == "__main__":
    pytest.main()
