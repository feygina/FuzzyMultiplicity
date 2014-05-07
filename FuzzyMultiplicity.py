

class FuzzyMultiplicity(object):

    def __init__(self, fuzzy_one, fuzzy_two):
        self.__fuzzy_number_one = fuzzy_one
        self.__fuzzy_number_two = fuzzy_two

    def get_func_of_belonging(self, cord_one, cord_two):
        return (self.__fuzzy_number_one.get(cord_one).get_func_of_belonging() + self.__fuzzy_number_two.get(cord_two).get_func_of_belonging()) / 2

    def get_key_points(self):
        key_points = []
        for point_one in self.__fuzzy_number_one.get_points():
            for point_two in self.__fuzzy_number_two.get_points():
                key_points.append((point_one.get_coordinate(), point_two.get_coordinate()))
        return key_points

    def get_straight_key_points(self, point_of_straight, k):
        key_points = []
        for point_one in self.__fuzzy_number_one.get_points():
            key_points.append(
                (
                    point_one.get_coordinate(),
                    k * point_one.get_coordinate() - (point_of_straight[0] - point_of_straight[1])
                )
            )
        for point_two in self.__fuzzy_number_two.get_points():
            key_points.append(
                (
                    (point_two.get_coordinate() + (point_of_straight[0] - point_of_straight[1])) / k,
                    point_two.get_coordinate()
                )
            )
        clear_key_points = []
        for key_point in key_points:
            if not key_point in clear_key_points:
                clear_key_points.append(key_point)
        return clear_key_points