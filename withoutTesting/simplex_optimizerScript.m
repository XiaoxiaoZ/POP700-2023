This a single function that performs Simplex Linear Optimization for LP programming

This example is for maximising an Objective Function. This can be converted into a minimizing problem by multiplying a negative one across the constraint equations

function simplex_optimizer(x1,x2,a1,a2,b1,b2,s1,s2,p1,p2)
x1,x2 -> Coeff of variable in the objective function
a1,a2 -> Coeff of variable x1 in the first and second objective function respectively.
b1,b2 -> Coeff of variable x2, x1 