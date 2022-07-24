import sys
intType=1
floatType=2.2
doubleType=2.22222222222
charType='c'
#sizeof evaluates the size of a variable
print("Size of int: {} bytes".format(sys.getsizeof(intType)))
print("Size of float: {} bytes".format(sys.getsizeof(floatType)))
print("Size of double: {} bytes".format(sys.getsizeof(doubleType)))
print("Size of char: {} bytes".format(sys.getsizeof(charType)))
