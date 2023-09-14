import unittest
from main import Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.get_area(), 78.53981633974483)

    def test_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0)
        self.assertTrue(triangle.is_right_angled())


if __name__ == '__main__':
    unittest.main()
