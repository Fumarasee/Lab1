import numpy as np

mu0 = [0, 2, 3]
mu1 = [3, 5,1]
sigma0= [2, 1, 2]
sigma1 = [1, 2, 1]

N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков
class0 = np.random.normal(mu0[0],sigma0[0],[N,1]) # инициализируем первый столбец класса 0
class1 = np.random.normal(mu1[0],sigma1[0],[N,1])

for i in range(1,col): # подумайте, почему нумерация с 1, а не с 0
    v0 = np.random.normal(mu0[i],sigma0[i],[N,1])
    class0 = np.hstack((class0,v0))
    v1 = np.random.normal(mu1[i],sigma1[i],[N,1])
    class1 = np.hstack((class1,v1))

Y1 = np.ones((N, 1), dtype=bool)# массив логических единиц
Y0 = np.zeros((N, 1), dtype=bool)

N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков
X = np.vstack((class0,class1))
Y = np.vstack((Y0,Y1)).ravel()

import DataGenerator as dg
mu = [mu0, mu1]
sigma = [sigma0, sigma1]
X, Y = dg.norm_dataset(mu, sigma, N)