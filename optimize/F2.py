from z3 import *


opt = Optimize()


c1, c2, c3, c4, c5, c6 = Bools("c1 c2 c3 c4 c5 c6")
p1, p2, p3 = Bools("p1 p2 p3")


opt.add(p1 == True)


# attack formula
F2 = And(
    Or(c1, c2, p1),   
    Or(c3, c4, c5, p2),        
    Or(p3, c6),        
  
)


#opt.add(Not(F2))
opt.add(F2)

# minimize active configurations
opt.maximize(Sum([
    If(c1, 1, 0), If(c2, 1, 0), If(c3, 1, 0),If(c4, 1, 0), If(c5, 1, 0),
    If(c6, 1, 0)
]))

# maximize number of privileges
opt.maximize(Sum([If(p1, 1, 0), If(p2, 1, 0), If(p3, 1, 0)]))


if opt.check() == sat:
    model = opt.model()
   
    for v in [c1, c2, c3, c4, c5, c6, p1, p2, p3]:
        print(f"{v}: {model[v]}")
else:
    print("Немає рішення")