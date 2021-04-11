# distutils: language = c++

# cdef extern from "kacken.h":
#     void hello()
#
# def py_hello() -> None:
#     hello()

import math


class Vector:
    def __init__(self, target_coordinates: list, position_coordinates: list = None):
        self.position = position_coordinates
        self.target = target_coordinates

        if self.position is None:  # init origin as position
            self.position = [0 for _ in self.target]

        if len(self.target) != len(self.position):
            raise IndexError(f"Position is defined in {len(self.position)} dimensions, target has {len(self.target)} dimensions!")

    def length(self) -> float:
        diff = [self.target[i] - self.position[i] for i in range(len(self.target))]
        return math.sqrt(sum([x ** 2 for x in diff]))
