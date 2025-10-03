import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# --- Визначення функції ---
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# --- Метод Монте-Карло ---
N = 100000  # кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, max(f(x_random)), N)

# Визначення точок під кривою
under_curve = y_random <= f(x_random)
integral_mc = (b - a) * max(f(x_random)) * np.sum(under_curve) / N
print(f"Інтеграл методом Монте-Карло: {integral_mc}")

# --- Перевірка точності за допомогою quad ---
integral_exact, error = spi.quad(f, a, b)
print(f"Аналітичний інтеграл (quad): {integral_exact}, оцінка помилки: {error}")

# --- Графічне відображення ---
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, 200)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Відображення випадкових точок
ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=1, label='Під кривою')
ax.scatter(x_random[~under_curve], y_random[~under_curve], color='blue', s=1, label='Поза кривою')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y)+0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
ax.legend()
plt.grid()
plt.show()
