import numpy as np
import matplotlib.pyplot as plt

# Input values for x and y
x = list(map(float, input("Enter x values (space-separated): ").split()))
x = np.array(x)
y = list(map(float, input("Enter y values (space-separated): ").split()))
y = np.array(y)

# Analytical solution for z
z = 3 * x - 3 + 4 * np.exp(-x)

# Plotting the solutions
plt.figure(dpi=300, figsize=(8,8))
plt.plot(x, y, label="Numerical solution (Runge-Kutta)", color="orange")
plt.plot(x, z, linestyle="--", label=r"Analytical solution $y=3x-3+4e^{-x}$", color="purple")

# Setting title and labels
plt.title(r"Graph for $y(x)$ where $\frac{dy}{dx}=3x-y$")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("runge_kutta_graph.png")
plt.show()
