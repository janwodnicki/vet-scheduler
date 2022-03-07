# vet-scheduler
v1: Gurobi specific implementation, ~2x faster but only supports GUROBI solver
![gurobi example](./doc/ex1_gurobi_solution.png)

v2: General implementation with cvxpy, CBC performs the best of free solvers but 5-10x slower than v1 or 3-5x slower than v2 CBC![gurobi example](./doc/ex1_cbc_solution.png)