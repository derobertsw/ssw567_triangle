#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional

"""
    This program classifies triangles based on the lengths of the sides
"""
__author__ = "Will DeRoberts"
__date__ = "September 6th, 2020"


def classify_triangle(a: float, b: float, c: float) -> str:
    """
    This function takes 3x sides of a triangle and returns a string that specifies whether the triangle is scalene,
    isosceles, or equilateral, and whether it is a right triangle as well
    """
    _validate_triangle(a, b, c)
    return _classify_angle(a, b, c) + _classify_shape(a, b, c)


def _validate_triangle(a: float, b: float, c: float) -> None:
    """
    This function validates the sides of a triangle and throws an exception if the triangle is not valid
    """

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be greater than 0")

    if a > b + c or b > a + c or c > a + b:
        raise ValueError("Side lengths must not exceed the sum of the opposite sides")


def _classify_shape(a: float, b: float, c: float) -> str:
    """
    This function takes 3x sides of a triangle and returns a string that specifies whether the triangle is scalene,
    isosceles, or equilateral
    """
    if a is b is c:
        return 'equilateral'

    if a is b or b is c or a is c:
        return 'isosceles'

    return 'scalene'


def _classify_angle(a: float, b: float, c: float) -> str:
    """
    This function takes 3x sides of a triangle and returns a string that specifies whether the triangle is a right
    triangle
    """
    side1: float
    side2: float
    hypotenuse: float

    side1, side2, hypotenuse = sorted([a, b, c])

    if round(side1 ** 2 + side2 ** 2, 2) == round(hypotenuse ** 2, 2):
        return 'right '
    return ''


def main() -> None:
    print(classify_triangle(3, 4, 5))


if __name__ == '__main__':
    main()
