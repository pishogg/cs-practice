import numpy as np

#1 

hours = np.arange(22, step=3)
line = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours, hours.shape, hours.ndim, hours.size, hours.dtype)
#[ 0  3  6  9 12 15 18 21] (8,) 1 8 int64


#2
print(hours[2]) #3 el
#6
print(hours[-1]) 
#21
print(hours[2:6]) 
#[ 6  9 12 15]
print(hours[::2]) #each 2th
#[ 0  6 12 18]
print(hours[::-1]) #reverse
#[21 18 15 12  9  6  3  0]


#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape) #форма
#(3, 4)
print(temperatures.ndim) #число изм
#2
print(temperatures.size) #число эл
#12
print(temperatures[1,2]) #2стр 3стлб
#16
print(temperatures[:1:,::]) #1стр
#[[12 14 13 15]]
print(temperatures[:,-1:]) #посл столбец
#[[15]
# [17]
# [18]]
print(temperatures[:2,1:]) # 2 3 строка
#[[14 13 15]
# [13 16 17]]
print(temperatures[:2:,1:3:]) #центр (2,2)
#[[14 13]
# [13 16]]


#4


matrix = np.arange(1, 26).reshape(5, 5)

print(matrix)
"""
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
"""


#первые три строки
print(matrix[:3:, ::].shape)
#(3, 5)


# последние две строки
print(matrix[-2::, ::].shape)
#(2, 5)


# первые два столбца
print(matrix[:, :2].shape)
#(5, 2)


# фрагмент из строк с индексами 1–3 и столбцов 2–4
print(matrix[1:4:, 2:5:].shape)
#(3, 3)


# угловой блок 2×2 в правом нижнем углу
print(matrix[-2:, -2:].shape)
#(2, 2)



#5

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9



changed_hours = hours.copy()

changed_hours[2:5] =  99
changed_hours[::2] = -1

print('Исходный hours', hours) 
#Исходный hours [ 0  3  6  9 12 15 18 21]
print('Измененный hours', changed_hours)
#Измененный hours [-1  3 -1 99 -1 15 -1 21]
#copy необходима для изменения значений массива hours так, чтобы его изначальные данные можно было еще вывести
 
 
changed_matrix = matrix.copy()

changed_matrix[1:2:, ::] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4:, 1:4:] = np.full((3,3), 100)


print('Исходный matrix', matrix)
"""
Исходный matrix 
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
"""


print('Измененный matrix', changed_matrix)

"""
Измененный matrix 
[[  1   2   3   4  -1]
 [  0 100 100 100  -1]
 [ 11 100 100 100  -1]
 [ 16 100 100 100  -1]
 [ 21  22  23  24  -1]]
"""



#6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers, table, transposed)
#[ 0  1  2  3  4  5  6  7  8  9 10 11]
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 
 
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]"""
print(numbers.shape, table.shape, transposed.shape)
#(12,) (3, 4) (4, 3)

#reshape(5, 3) вызовет ошибку тк в массиве 12 чисел, а не 15


