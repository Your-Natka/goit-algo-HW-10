import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# -------------------------
# Визначення функції та меж інтегрування
# -------------------------
def f(x):
    return x ** 2  # приклад: інтегруємо x^2

a, b = 0, 2  # межі інтегрування

# -------------------------
# Метод Монте-Карло
# -------------------------
def monte_carlo_integration(f, a, b, num_samples=100000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    area = (b - a) * np.mean(y_random)
    return area

# Обчислення інтеграла методом Монте-Карло
mc_result = monte_carlo_integration(f, a, b)
print("Інтеграл методом Монте-Карло:", mc_result)

# -------------------------
# Перевірка точності за допомогою quad
# -------------------------
quad_result, error = spi.quad(f, a, b)
print("Інтеграл методом quad:", quad_result, "| Оцінка помилки:", error)

# -------------------------
# Побудова графіка функції та області під кривою
# -------------------------
x = np.linspace(a-0.5, b+0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b, 200), f(np.linspace(a, b, 200)), color='gray', alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Інтеграл f(x)=x^2 від {} до {}'.format(a, b))
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
plt.grid()
plt.show()

# -------------------------
# Висновки
# -------------------------
difference = abs(mc_result - quad_result)
print(f"Різниця між методом Монте-Карло і quad: {difference:.6f}")
if difference < 0.01:
    print("Розрахунок методом Монте-Карло достатньо точний для практичних цілей.")
else:
    print("Розрахунок методом Монте-Карло має помітну похибку. Можна збільшити кількість вибірок.")
