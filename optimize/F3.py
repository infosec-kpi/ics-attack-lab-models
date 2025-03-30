from z3 import *
import time

opt = Optimize()

c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12 = Bools("c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12")
p1, p2, p3, p4, p5 = Bools("p1 p2 p3 p4 p5")

start_time = time.time()
opt.add(c1 == True)
opt.add(c5 == True)

# Attack formula
F3 = And(
    Or(c1, c2, c3, p1),    # (c1 ∨ c2 ∨ c3 ∨ p1)
    Or(c5, c4, p2),        # (c5 ∨ c4 ∨ p2)
    Or(c6, c7, p3),        # (c6 ∨ c7 ∨ p3)
    Or(c8, c9, p4),        # (c8 ∨ c9 ∨ p4)
    Or(c10, c11, c12, p5)  # (c10 ∨ c11 ∨ c12 ∨ p5)
)


#opt.add(Not(F3))
opt.add(F3)

# minimize active configurations
opt.maximize(Sum([
    If(c1, 1, 0), If(c2, 1, 0), If(c3, 1, 0),If(c4, 1, 0), If(c5, 1, 0),
    If(c6, 1, 0), If(c7, 1, 0), If(c8, 1, 0), If(c9, 1, 0),
    If(c10, 1, 0), If(c11, 1, 0), If(c12, 1, 0)
]))

# maximize number of privileges
opt.maximize(Sum([If(p1, 1, 0), If(p2, 1, 0), If(p3, 1, 0), If(p4, 1, 0), If(p5, 1, 0)]))


if opt.check() == sat:
    model = opt.model()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total script time: {total_time:.6f} seconds")
    for v in [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, p1, p2, p3, p4, p5]:
        print(f"{v}: {model[v]}")
