# def get_int():
#     while True:
#         try:
#             reply = int(input('Enter any number : '))
#             return reply
#         except:
#             print('Not a number! Try again.')
# 
# 
# print(get_int())

import math

import mpmath.visualization

class InvalidTriangeError(Exception):
    """Raised when a triangle has invalid sides"""

def calc_square(ab,ac,bc):
    if ab<=0 or ac<=0 or bc<=0:
        raise InvalidTriangeError("One of the sides is less or equal to 0.")

    p = (ab+ac+bc)/2

    s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))

    return s

try:
    square = calc_square(2,10,10)
except InvalidTriangeError as ex:
    print(ex)
else:
    print(square)
