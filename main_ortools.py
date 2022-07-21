from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('Glop')

x = solver.NumVar(0, 10, 'x')
y = solver.NumVar(0, 10, 'y')

solver.Add(-x+2*y <= 8)                             
solver.Add(2*x+y <= 14)
solver.Add(2*x-y <= 10)

solver.Maximize(x+y)

results = solver.Solve()
if results == pywraplp.Solver.OPTIMAL:
    print('We have found an optimal solution :)')
else:
    print('No Optimal solution was found for this problem :(')

print(f'x: {x.solution_value()}')
print(f'y: {y.solution_value()}')


