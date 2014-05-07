from FuzzyPoint import *


class FuzzyNumber(object):

    def __init__(self):
        self.__points = []

    def insert(self, fuzzy_point):
        if not fuzzy_point in self.__points:
            self.__points.append(fuzzy_point)

    def get_points(self):
        return self.__points

    def get(self, coordinate):
        required_fuzzy_point = None
        for fuzzy_point in self.__points:
            if coordinate == fuzzy_point.get_coordinate():
                required_fuzzy_point = fuzzy_point
        if required_fuzzy_point is None:
            left_nearest_point = None
            right_nearest_point = None
            for fuzzy_point in self.__points:
                if fuzzy_point.get_coordinate() < coordinate:
                    if left_nearest_point is None:
                        left_nearest_point = fuzzy_point
                    else:
                        if left_nearest_point.get_coordinate() < fuzzy_point.get_coordinate():
                            left_nearest_point = fuzzy_point
                if fuzzy_point.get_coordinate() > coordinate:
                    if right_nearest_point is None:
                        right_nearest_point = fuzzy_point
                    else:
                        if right_nearest_point.get_coordinate() > fuzzy_point.get_coordinate():
                            right_nearest_point = fuzzy_point
            if left_nearest_point is None or right_nearest_point is None:
                raise Exception('Can\'t perform linear interpolation')

            func_of_belonging = \
                (right_nearest_point.get_func_of_belonging() - left_nearest_point.get_func_of_belonging()) * (
                    (coordinate - left_nearest_point.get_coordinate()) /
                    (
                        (coordinate - left_nearest_point.get_coordinate())
                        + (right_nearest_point.get_coordinate() - coordinate)
                    )
                ) + left_nearest_point.get_func_of_belonging()

            required_fuzzy_point = FuzzyPoint(coordinate, func_of_belonging)

        return required_fuzzy_point

    def get_square(self):
        self.__sort_points()
        square = 0
        for i in range(0, len(self.__points) - 1):
            square += 0.5 * \
                (self.__points[i].get_func_of_belonging() + self.__points[i + 1].get_func_of_belonging()) * \
                (self.__points[i + 1].get_coordinate() - self.__points[i].get_coordinate())
        return square

    def normalize(self):
        coefficient = 1 / self.get_square()
        for point in self.__points:
            point.multiply_function_of_belonging(coefficient)

    def __sort_points(self):
        self.__points = sorted(self.__points, key=lambda x: x.get_coordinate())