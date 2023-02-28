'''
This script is to test optimizer in scipy
References:  
https://blog.csdn.net/HappyRocking/article/details/92574229
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
'''
import numpy as np
from scipy.optimize import minimize


e = 1e-10

fun = lambda x: (x[0] - 0.667) / (x[0] + x[1] + x[2] - 2 )

cons = ({'type': 'eq', 'fun': lambda x: x[0] * x[1] * x[2] - 1 },
        {'type': 'ineq', 'fun': lambda x: x[0] - e},
        {'type': 'ineq', 'fun': lambda x: x[1] - e},
        {'type': 'ineq', 'fun': lambda x: x[2] - e})

x0 = np.array((1.0, 1.0, 1.0))
res = minimize(fun, x0, method='SLSQP', constraints=cons)

print(res.message)
print('The minimal value is: ', res.fun)
print("The optimal values are: ", res.x)




