# from cython_vector.vectors import Vector as VectorC
# from cython_vector.vectors_py import Vector as VectorP
# from time import time
#
# c = VectorC([416.23468, 123.67348, 45223.89321])
# p = VectorP([416.23468, 123.67348, 45223.89321])
#
# n = 1_000_000
#
# start = time()
# for i in range(n):
#     c.length()
# print(time() - start)
#
# start = time()
# for i in range(n):
#     p.length()
# print(time() - start)


from cython_vector.foobar import print_stuff, test_the_list

print_stuff("ÖÄÜüäö€@~")
test_the_list([1, 4, 5.5, 2])
