import numpy as np

#1 

hours = np.arange(21, step=3)
line = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]
zeros = np.zeros(6)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours, hours.shape, hours.ndim, hours.size, hours.dtype)

#2
print(hours[2]) #3 el
print(hours[-1]) 
print(hours[2:6]) 
print(hours[::2]) #each 2th
print(hours[::-1]) #reverse


#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape) #форма
print(temperatures.ndim) #число изм
print(temperatures.size) #число эл
print(temperatures[1:2:,2:3:]) #2стр 3стлб
print(temperatures[:1:,::]) #1стр
print(temperatures[::,:-1:]) #посл столбец
print(temperatures[1:3:,::]) # 2 3 строка
print(temperatures[:2:,1:3:]) #центр (2,2)
print(temperatures[:1:,::]) #



#4


matrix = np.arange(1, 26).reshape(5, 5)

