# distutils: language = c++

from typing import List

from libcpp.vector cimport vector
from libcpp.string cimport string


cdef extern from "foobar.h":
    void print_my_stuff(char*)
    void test_list(vector[float])


cpdef print_stuff(text: str):
    print_my_stuff(text.encode())

cpdef test_the_list(k: List[float]):
    test_list(k)

#
# cdef class CVector:
#     cdef Vector*_c_vector
#
#     def __cinit__(self):
#         pass
#
#     def __init__(self, target_coordinates: list, position_coordinates: list = None):
#         self.position = position_coordinates
#         self.target = target_coordinates
#
#         if self.position is None:  # init origin as position
#             self.position = [0 for _ in self.target]
#
#         if len(self.target) != len(self.position):
#             raise IndexError(f"Position is defined in {len(self.position)} dimensions, target has {len(self.target)} dimensions!")
#
#     cdef float length(self):
#         diff = [self.target[i] - self.position[i] for i in range(len(self.target))]
#         return math.sqrt(sum([x ** 2 for x in diff]))
