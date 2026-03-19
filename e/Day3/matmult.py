# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

# NxN matrix
X = np.random.randint(100, size = (N,N))


# Nx(N+1) maxtrix
Y = np.random.randint(100,(N,N+1))

# result is Nx(N+1)
result = np.zeros((N,N+1))


result = X @ Y

print(result)
