import numpy as np 
import timeit
print("Addition using vectorization = ",np.prod(np.arange(4)))
print("time taken by vectorized product:",end="")
print(timeit.timeit('np.sum', globals=globals()))
total=1
for item in range(1,4):
    total*=item
a=total 
print("Addition using looping statement =",a)
print("time taken by iterative product:",end="")
print(timeit.timeit('a ', globals=globals()))

print('this is Risheek')
