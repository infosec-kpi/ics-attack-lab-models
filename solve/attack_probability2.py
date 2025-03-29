from z3 import *
import random
import matplotlib.pyplot as plt

# Змінні, які входять у формулу F2
var_names = ['c1', 'c2', 'p1', 'c3', 'c4', 'c5', 'p2', 'p3', 'c6']
vars_map = {name: Bool(name) for name in var_names}

# Формула F2
F2 = Or(vars_map['c1'], vars_map['c2'], vars_map['p1']) & \
     Or(vars_map['c3'], vars_map['c4'], vars_map['c5'], vars_map['p2']) & \
     Or(vars_map['p3'], vars_map['c6'])

# Параметри симуляції
num_trials = 100  # кількість спроб для кожного k
max_active = len(var_names)
results = []

# Основний цикл: для кожного значення k перевіряємо ймовірність, що F2=True
for k in range(1, max_active + 1):
    success_count = 0
    for _ in range(num_trials):
        active_vars = set(random.sample(var_names, k))
        s = Solver()
        for name in var_names:
            s.add(vars_map[name] == (name in active_vars))
        s.push()
        s.add(F2)
        if s.check() == sat:
            success_count += 1
        s.pop()
    probability = success_count / num_trials
    results.append(probability)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_active + 1), results, marker='o', linestyle='-')
plt.title('Probability that F2 = True vs. Number of Active Elements')
plt.xlabel('Number of Active (Vulnerable) Variables')
plt.ylabel('Probability that Attack is Feasible (F2 = True)')
plt.grid(True)
plt.tight_layout()
plt.show()
