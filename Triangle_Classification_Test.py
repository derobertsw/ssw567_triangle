import unittest
from Triangle_Classification import classify_triangle


class TriangleClassificationTest(unittest.TestCase):
    def test_triangle_validation(self):
        """
        Tests that classify_triangle raises ValueError Exception for invalid input
        """
        with self.assertRaises(ValueError):
            classify_triangle(-1, 1, 1)
        with self.assertRaises(ValueError):
            classify_triangle(1, 0, 1)
        with self.assertRaises(ValueError):
            classify_triangle(1, 1, 3)

        self.assertTrue(classify_triangle(1, 1, 1))

    def test_triangle_classification(self):
        """
        tests the functionality of the classify_triangle function
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')

        self.assertEqual(classify_triangle(1, 2, 1), 'isosceles')
        self.assertEqual(classify_triangle(1, 1, 2), 'isosceles')
        self.assertEqual(classify_triangle(2, 1, 1), 'isosceles')
        self.assertEqual(classify_triangle(1, 1, 1.4142), 'right isosceles')

        self.assertEqual(classify_triangle(1, 2.5, 3), 'scalene')   
        self.assertEqual(classify_triangle(3, 4, 5), 'right scalene')
        self.assertEqual(classify_triangle(5, 4, 3), 'right scalene')
        self.assertEqual(classify_triangle(5.0, 4.0, 3.0), 'right scalene')
        self.assertEqual(classify_triangle(5.001, 4, 3), 'scalene')


if __name__ == '__main__':
    unittest.main(verbosity=2)
