from z3 import *
import time

solver = Solver()


x1 = Bool('x1')
x2 = Bool('x2')
x3 = Bool('x3')
x4 = Bool('x4')
x5 = Bool('x5')
x6 = Bool('x6')
p1 = Bool('p1')
p2 = Bool('p2')


start_time = time.time()

condition = And(Or(x1,x2,p1),Or(x3,x4,p2),Or(x5,x6))
answers = []

solver.add(condition)
solver.add(x5 == True)
solver.add(x1 == True)
for i in range(2**8):

    assignment = [
        (x1, (i >> 7) & 1),
        (x2, (i >> 6) & 1),
        (x3, (i >> 5) & 1),
        (x4, (i >> 4) & 1),
        (x5, (i >> 3) & 1),
        (x6, (i >> 2) & 1),
        (p1, (i >> 1) & 1),
        (p2, i & 1)
    ]
  
    solver.push() 

    for var, value in assignment:
        solver.add(var == (value == 1))

    if solver.check() == sat:
        
        model = solver.model()
        answer = {"c1": model[x1],"c2": model[x2],"c3": model[x3],"c4": model[x4],"c5": model[x5],"c6": model[x6],"p1": model[p1],"p2": model[p2]}
        answers.append(answer)
    
    solver.pop()

end_time = time.time()
total_time = end_time - start_time
print(f"Total script time: {total_time:.6f} seconds") 
if answers:
    with open("out1.2","w") as f:
        for a in answers:
            f.write(str(a) + "\n")
        f.close()
else:
    print("No satisfying assignment found")

