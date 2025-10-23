import numpy as np
import matplotlib.pyplot as plt

# Parámetros
g = 32  # ft/s^2
h0 = 800  # altura inicial granada
target_h = 400  # altura de encuentro
delay = 2  # s

# --- 1. Resolver analíticamente ---
# Ecuación granada: y_g(t) = 800 - 16 t^2
# Queremos t tal que y_g(t) = 400
t_meet = np.sqrt((h0 - target_h) / (0.5 * g))
print(f"Tiempo de encuentro: t = {t_meet:.2f} s")

# Velocidad inicial proyectil
v0 = (target_h + 16*(t_meet - delay)**2) / (t_meet - delay)
print(f"Velocidad inicial necesaria: v0 = {v0:.2f} ft/s")

# --- 2. Simulación de trayectorias ---
t_vals = np.linspace(0, t_meet+1, 200)
y_granada = h0 - 0.5*g*t_vals**2
y_proyectil = np.where(t_vals >= delay,
                       v0*(t_vals-delay) - 0.5*g*(t_vals-delay)**2,
                       np.nan)

plt.figure(figsize=(8,5))
plt.plot(t_vals, y_granada, label="Granada")
plt.plot(t_vals, y_proyectil, label="Proyectil")
plt.axhline(target_h, color="gray", linestyle="--", label="Altura 400 ft")
plt.axvline(t_meet, color="red", linestyle="--", label=f"Encuentro t={t_meet:.2f}s")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (ft)")
plt.title("Trayectorias: Granada vs Proyectil")
plt.legend()
plt.grid(True)
plt.show()

# --- 3. Campo de isoclinas ---
# EDO: y' = v, v' = -g
y = np.linspace(0, 850, 20)
v = np.linspace(-200, 200, 20)
Y, V = np.meshgrid(y, v)

dY = V
dV = -g * np.ones_like(V)

plt.figure(figsize=(8,6))
plt.quiver(Y, V, dY, dV, angles="xy")
plt.xlabel("Posición y (ft)")
plt.ylabel("Velocidad v (ft/s)")
plt.title("Campo de isoclinas para el movimiento vertical")
plt.grid(True)
plt.show()
