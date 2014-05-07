

class FuzzyPoint(object):

    def __init__(self, coordinate, func_of_belonging):
        self.__coordinate = coordinate
        self.__func_of_belonging = func_of_belonging

    def get_coordinate(self):
        return self.__coordinate

    def get_func_of_belonging(self):
        return self.__func_of_belonging

    def __eq__(self, other):
        return self.get_coordinate() == other.get_coordinate() and \
            self.get_func_of_belonging() and other.get_func_of_belonging()

    def multiply_function_of_belonging(self, coefficient):
        self.__func_of_belonging *= coefficient