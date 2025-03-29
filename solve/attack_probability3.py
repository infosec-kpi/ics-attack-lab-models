from z3 import *
import random
import matplotlib.pyplot as plt

# Імена змінних у F3
var_names = [
    'c1', 'c2', 'c3', 'p1',
    'c4', 'c5', 'p2',
    'c6', 'c7', 'p3',
    'c8', 'c9', 'p4',
    'c10', 'c11', 'c12', 'p5'
]

# Створення булевих змінних
vars_map = {name: Bool(name) for name in var_names}

# Визначення формули F3
F3 = And(
    Or(vars_map['c1'], vars_map['c2'], vars_map['c3'], vars_map['p1']),
    Or(vars_map['c5'], vars_map['c4'], vars_map['p2']),
    Or(vars_map['c6'], vars_map['c7'], vars_map['p3']),
    Or(vars_map['c8'], vars_map['c9'], vars_map['p4']),
    Or(vars_map['c10'], vars_map['c11'], vars_map['c12'], vars_map['p5'])
)

# Параметри симуляції
num_trials = 100
max_active = len(var_names)
results = []

# Аналіз: для кожної k-величини активних змінних — рахуємо ймовірність F3=True
for k in range(1, max_active + 1):
    success_count = 0
    for _ in range(num_trials):
        active_vars = set(random.sample(var_names, k))
        s = Solver()
        for name in var_names:
            s.add(vars_map[name] == (name in active_vars))
        s.push()
        s.add(F3)
        if s.check() == sat:
            success_count += 1
        s.pop()
    probability = success_count / num_trials
    results.append(probability)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_active + 1), results, marker='o', linestyle='-', color='green')
plt.title('Probability that F3 = True vs. Number of Active Elements')
plt.xlabel('Number of Active (Vulnerable) Variables')
plt.ylabel('Probability that Attack is Feasible (F3 = True)')
plt.grid(True)
plt.tight_layout()
plt.show()
