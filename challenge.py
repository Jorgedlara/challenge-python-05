import math


def square_area(side):
    """Returns the area of a square"""
    area = side ** 2
    return area


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    area = base * height
    return area


def triangle_area(base, height):
    """Returns the area of a triangle"""
    area = (base * height) / 2
    return area


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    area = (diagonal_1 * diagonal_2) / 2
    return area


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    area = ((base_minor + base_major) / 2) * height
    return area


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    area = (perimeter * apothem) / 2
    return area


def circumference_area(radius):
    """Returns the area of a circumference"""
    area = math.pi * (radius**2)
    return round (area,2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.parameters = {
                'side': 5,
                'neg_side': -5,
                'base': 10,
                'neg_base': -10,
                'height': 3,
                'neg_height': -3,
                'diagonal_1': 15, 
                'neg_diagonal_1': -15,
                'diagonal_2': 6,
                'neg_diagonal_2': -6,
                'base_minor': 4,
                'neg_base_minor': -4,
                'base_major': 8,
                'neg_base_major': -8,
                'perimeter': 30,
                'neg_perimeter': -30,
                'apothem': 7,
                'neg_apothem': -7,
                'radius': 10,
                'neg_radius': -10,
            }


        def test_square_area(self):
            square_answer = square_area(self.parameters['side'])
            square_answer_neg = square_area(self.parameters['neg_side'])
            self.assertEqual(square_answer, 25)
            self.assertEqual(square_answer_neg, 25)

        def test_rectangle_area(self):
            rectangle_answer = rectangle_area(self.parameters['base'], self.parameters['height'])
            rectangle_answer_neg = rectangle_area(self.parameters['neg_base'], self.parameters['neg_height'])
            self.assertEqual(rectangle_answer, 30)
            self.assertEqual(rectangle_answer_neg, 30)

        def test_triangle_area(self):
            triangle_answer = triangle_area(self.parameters['base'], self.parameters['height'])
            triangle_answer_neg = triangle_area(self.parameters['neg_base'], self.parameters['neg_height'])
            self.assertEqual(triangle_answer, 15)
            self.assertEqual(triangle_answer_neg, 15)

        def test_rhombus_area(self):
            rhombus_answer = rhombus_area(self.parameters['diagonal_1'], self.parameters['diagonal_2'])
            rhombus_answer_neg = rhombus_area(self.parameters['neg_diagonal_1'], self.parameters['neg_diagonal_2'])
            self.assertEqual(rhombus_answer, 45)
            self.assertEqual(rhombus_answer_neg, 45)

        def test_trapezoid_area(self):
            trapezoid_answer = trapezoid_area(self.parameters['base_minor'], self.parameters['base_major'], self.parameters['height'])
            trapezoid_answer_neg = trapezoid_area(self.parameters['neg_base_minor'], self.parameters['neg_base_major'], self.parameters['neg_height'])
            self.assertEqual(trapezoid_answer, 18)
            self.assertEqual(trapezoid_answer_neg, 18)

        def test_regular_polygon_area(self):
            regular_polygon_answer = regular_polygon_area(self.parameters['perimeter'], self.parameters['apothem'])
            regular_polygon_answer_neg = regular_polygon_area(self.parameters['neg_perimeter'], self.parameters['neg_apothem'])
            self.assertEqual(regular_polygon_answer, 105)
            self.assertEqual(regular_polygon_answer_neg, 105)

        def test_circumference_area(self):
            circumference_answer = circumference_area(self.parameters['radius'])
            circumference_answer_neg = circumference_area(self.parameters['neg_radius'])
            self.assertEqual(circumference_answer, 314.16)
            self.assertEqual(circumference_answer_neg, 314.16)

        def tearDown(self):
            del(self.parameters)

    unittest.main()
