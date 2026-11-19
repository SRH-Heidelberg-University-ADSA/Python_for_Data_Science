print("called")
import numpy

print("imported")

arr = numpy.array([30, 25, 35])

a = [30, 25, 35]
# print(arr)

# standard
# for each in a:
#    a.append(each * 2)

print(a)

result = arr * 2

# indexing and slicing
numpy.zeros((3, 4))  # 3*4 matrix : rows,columns
numpy.ones((3, 4))
numpy.random.randint(1, 10, 3)


arr = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # to -1 dimension

print(arr[2:7])  # to indexing ranges

print(arr[:1])

# masking
arr = numpy.array([30, 25, 35])

mask = arr > 28
print(arr[mask])
print(arr)
