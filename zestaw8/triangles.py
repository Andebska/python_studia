from time import sleep

from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        if self._is_collinear():
            raise ValueError("Punkty są współliniowe")

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Lista musi zawierać trzy punkty")
        return cls(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)

    def _is_collinear(self):        # sprawdzanie czy punkty są współliniowe, prywatna metoda
        return  (self.pt2 - self.pt1).cross(self.pt3 - self.pt1) == 0

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):    # obsługa tr1 == tr2   # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,  # niezależnie od kolejności pt1, pt2, pt3.
        if not isinstance(other, Triangle):
            return False
        vertices_self = {self.pt1, self.pt2, self.pt3}
        vertices_other = {other.pt1, other.pt2, other.pt3}
        return vertices_self == vertices_other

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    @property
    def center(self):           # zwraca środek trójkąta
        center_x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        center_y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(center_x, center_y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return abs(self.right - self.left)

    @property
    def height(self):
        return abs(self.top - self.bottom)

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def area(self):            # pole powierzchni
        return abs((self.pt2 - self.pt1).cross(self.pt3 - self.pt1) / 2)

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)
        self.pt3 += Point(x, y)

    def make4(self):                            # zwraca krotkę czterech mniejszych
        #     A       po podziale    A
        #    / \                    / \
        #   /   \                  +---+
        #  /     \                / \ / \
        # C-------B              C---+---B
        m1 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        m2 = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        m3 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)

        return (
            Triangle(self.pt1.x, self.pt1.y, m1.x, m1.y, m2.x, m2.y),
            Triangle(m1.x, m1.y, self.pt2.x, self.pt2.y, m2.x, m3.y),
            Triangle(m2.x, m2.y, self.pt3.x, self.pt3.y, m3.x, m3.y),
            Triangle(m1.x, m1.y, m2.x, m2.y, m3.x, m3.y)
        )

