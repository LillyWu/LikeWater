'''
This is an example of creating abstract model in pyomo based on the official document
References: 
https://pyomo.readthedocs.io/en/stable/pyomo_overview/simple_examples.html
'''

from __future__ import division # Ensure int or long division can be transfered to floating point values
import pyomo.environ as pyo


# This is an example of Abstract Model
model = pyo.AbstractModel()

model.m = pyo.Param(within=pyo.NonNegativeIntegers)
model.n = pyo.Param(within=pyo.NonNegativeIntegers)

model.I = pyo.RangeSet(1, model.m) 
model.J = pyo.RangeSet(1, model.n)

# Index sets
model.a = pyo.Param(model.I, model.J) 
model.b = pyo.Param(model.I)
model.c = pyo.Param(model.J)

# Variables: index by the set J
model.x = pyo.Var(model.J, domain=pyo.NonNegativeReals)

# Use functions to define objective function and constraints
def obj_expression(model):
    return pyo.summation(model.c, model.x)

model.Obj = pyo.Objective(rule=obj_expression)  # By default, it is minimize; To use maximize, need to set "sense=pyo.maximize"

# Constraints for i
def ax_constraint_rule(model, i):
    return sum(model.a[i,j] * model.x[j] for j in model.J) >= model.b[i]
    
model.AxbConstraints = pyo.Constraint(model.I, rule=ax_constraint_rule)
    
    