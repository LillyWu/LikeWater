'''
This script is used to get familiar with pyomo (Python Optimization Modeling Objects)
References: 
https://pyomo.readthedocs.io/en/stable/installation.html

'''

import pyomo.environ as pyo

# This is an example of Concrete Model
model = pyo.ConcreteModel()

model.x = pyo.Var([1,2], domain=pyo.NonNegativeReals)
model.Obj = pyo.Objective(expr=2*model.x[1] + 3*model.x[2])

model.constraints = pyo.Constraint(expr=3*model.x[1] + 4*model.x[2] >= 1)


opt = pyo.SolverFactory('glpk')
opt.solve(model)

print(model.Obj)
print(model.x)
print(model.constraints)

 
