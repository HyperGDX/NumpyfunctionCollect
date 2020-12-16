import sympy

x=sympy.symbols('x')
y=sympy.solve([x*x*x-9*x*x*2+5*x-10],[x])
print(y)