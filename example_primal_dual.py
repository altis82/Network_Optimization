# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Chuan Pham

This is an example of primal-dual problem in LP
"""
from pulp import *
from fractions import Fraction

prob =LpProblem("example",LpMaximize)

#add non-negative constraints
x1=LpVariable("x1",0)
x2=LpVariable("x2",0)
#add objective function
prob+=x1+x2


prob += x1 + 2*x2 <= 4, "constraint 1"
prob += 4*x1 + 2*x2 <= 12, "constraint 2"
prob += -x1 + x2 <= 1, "constraint 3"


prob.solve()


# status of the solution
print(f"Status: {LpStatus[prob.status]}")
for v in prob.variables():
    print(f"{v.name} = {str(Fraction(v.varValue).limit_denominator())}")
    # maximum value of the objective function
    print(f"max (x1 + x2) = {str(Fraction(value(prob.objective)).limit_denominator())}")
    
    


prob = LpProblem("Dual problem",LpMinimize)
# nonnegativity constraints
y1=LpVariable("y1",0)
y2=LpVariable("y2",0)
y3=LpVariable("y3",0)
# objective function
prob += 4*y1 + 12*y2 + y3, "Minimum value of 4*y1 + 12*y2 + y3"
# main constraints
prob += y1 + 4*y2 - y3 >= 1, "constraint 1"
prob += 2*y1 + 2*y2 + y3 >= 1, "constraint 2"
# The problem is solved using PuLP's choice of Solver
prob.solve()
# status of the solution
print("==========================================")
print(f"\nStatus: {LpStatus[prob.status]}")
for v in prob.variables():
    print(f"{v.name} = {str(Fraction(v.varValue).limit_denominator())}")
# maximum value of the objective function
print(f"min (4*y1 + 12*y2 + y3) = {str(Fraction(value(prob.objective)).limit_denominator())}")