from z3 import *
import time

opt = Optimize()


c1, c2, c3, c4, c5, c6 = Bools("c1 c2 c3 c4 c5 c6")
p1, p2 = Bools("p1 p2")

start_time = time.time()
opt.add(c1 == True)
opt.add(c3 == True)

# attack formula
F1 = And(
    Or(c1, c2, p1),   
    Or(c3, c4, p2),        
    Or(c5, c6),        
  
)

#opt.add(Not(F1))
opt.add(F1)

# minimize active configurations
opt.maximize(Sum([
    If(c1, 1, 0), If(c2, 1, 0), If(c3, 1, 0),If(c4, 1, 0), If(c5, 1, 0),
    If(c6, 1, 0)
]))

# maximize number of privileges
opt.maximize(Sum([If(p1, 1, 0), If(p2, 1, 0)]))


if opt.check() == sat:
    model = opt.model()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total script time: {total_time:.6f} seconds")
    for v in [c1, c2, c3, c4, c5, c6, p1, p2]:
        print(f"{v}: {model[v]}")
else:
    print("Немає рішення")