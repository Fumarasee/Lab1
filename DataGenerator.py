import numpy as np

#объявляем функцию и определяем входные переменные
def norm_dataset(mu,sigma,N):
    mu0 = mu[0]
    mu1 = mu[1]
    sigma0 = sigma[0]
    sigma1 = sigma[1]
    col = len(mu0) # количество столбцов-признаков

    X = X[arr]
    Y = Y[arr]
    return X, Y, class0, class1 # возвращаемые аргументы

N = 1000 # число объектов класса
col = len(mu0) # количество столбцов-признаков
import DataGenerator as dg
mu = [mu0, mu1]
sigma = [sigma0, sigma1]
X, Y, class0, class1 = dg.norm_dataset(mu,sigma,N)