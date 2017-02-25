import numpy as np
import scipy as sp

def sep():
    print('-' * 60)

d = np.random.rand(2, 3)
print(d)
print(d.ndim)
print(d.shape)
print(d.dtype)


d2 = np.array(range(10))
print(d2)
print(d2.shape)
print(d2.ndim)


zeros_arr = np.zeros((4, 3), dtype=np.float32)
print(zeros_arr)
print(zeros_arr.astype(np.int32))

print(np.ones((3, 3), int))
print(np.empty((3, 3), int))


print(np.arange(10).reshape((5, 2)))


# vectorization
#   broadcast

d3 = np.array([[1, 2, 3],
              [4, 5, 6]])
print(d3 * 2)
print(d3 + d3)
print(d3.dot(d3.transpose()))

d4 = np.arange(12).reshape(3, 4)
print("--" * 10)
print(d4)
print(d4[1])
print(d4[0:2, 2])
print(d4[:, 1:3])

print("-")


data = np.random.rand(3, 3)
year_arr = np.array([[2000, 2001, 2000],
                     [2005, 2002, 2009],
                     [2001, 2003, 2010]])
year_after_2005 = year_arr >= 2005
filtered = data[year_arr >= 2005]
print(year_arr)
print(year_after_2005)
print(filtered)

filtered = data[(year_arr <= 2005) & (year_arr % 2 == 0)]
print(filtered)


# transpose
print('-' * 50)
d6 = np.random.randn(3, 4).transpose()
print(d6)

print(np.ceil(d6))
print(np.floor(d6))
print(np.rint(d6))
print(np.isnan(d6))
print(np.ceil(d6))


print('-' * 50)

d = np.random.randn(3, 4)
print(d)
print(np.where(d > 0, 1, -1))


sep()
d = np.arange(10).reshape(5, 2)
print(d)
print(np.sum(d))
print(np.sum(d, axis=0))
print(np.sum(d, axis=1))

sep()
# np.all    np.any  np.unique
print(np.any(np.random.randn(2, 3) > 0))
print(np.all(np.random.randn(2, 3) > 0))
print(np.unique([[1, 2, 3], [2, 3, 4], [1, 2, 4]]))
