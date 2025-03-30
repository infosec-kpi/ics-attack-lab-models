from z3 import *
import time

solver = Solver()


x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = Bools("c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12")
p1, p2, p3, p4, p5 = Bools("p1 p2 p3 p4 p5")

start_time = time.time()

condition = And(
    Or(x1, x2, x3, p1),    # (c1 ∨ c2 ∨ c3 ∨ p1)
    Or(x5, x4, p2),        # (c5 ∨ c4 ∨ p2)
    Or(x6, x7, p3),        # (c6 ∨ c7 ∨ p3)
    Or(x8, x9, p4),        # (c8 ∨ c9 ∨ p4)
    Or(x10, x11, x12, p5)  # (c10 ∨ c11 ∨ c12 ∨ p5)
)

answers = []

solver.add(condition)
solver.add(x1 == True)
solver.add(x5 == True)

for i in range(2**17):
    assignment = [
    (x1, (i >> 16) & 1),
    (x2, (i >> 15) & 1),
    (x3, (i >> 14) & 1),
    (x4, (i >> 13) & 1),
    (x5, (i >> 12) & 1),
    (x6, (i >> 11) & 1),
    (x7, (i >> 10) & 1),
    (x8, (i >> 9) & 1),
    (x9, (i >> 8) & 1),
    (x10, (i >> 7) & 1),
    (x11, (i >> 6) & 1),
    (x12, (i >> 5) & 1),
    (p1, (i >> 4) & 1),
    (p2, (i >> 3) & 1),
    (p3, (i >> 2) & 1),
    (p4, (i >> 1) & 1),
    (p5, i & 1)
]

    solver.push() 

    for var, value in assignment:
        solver.add(var == (value == 1))

    if solver.check() == sat:
        
        model = solver.model()
        answer = {"c1": model[x1],"c2": model[x2],"c3": model[x3],"c4": model[x4],"c5": model[x5],"c6": model[x6],"c7": model[x7],
        "c8": model[x8],"c9": model[x9],"c10": model[x10],"c11": model[x11],"c12": model[x12],"p1": model[p1],"p2": model[p2],"p3":model[p3]
        ,"p4": model[p4],"p5": model[p5]}
        answers.append(answer)
    
    solver.pop()

end_time = time.time()
total_time = end_time - start_time
print(f"Total script time: {total_time:.6f} seconds")
if answers:
    with open("out3","w") as f:
        for a in answers:
            f.write(str(a) + "\n")
        f.close()
else:
    print("No satisfying assignment found")

