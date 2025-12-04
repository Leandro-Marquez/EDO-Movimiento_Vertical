import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definir el sistema de ecuaciones diferenciales
def sistema(t, z):
    """Define el sistema de ecuaciones dy/dt = v, dv/dt = -2v - 5y"""
    y, v = z
    return [v, -2*v - 5*y]

# 2. Calcular y clasificar el punto crítico
print("=== ANÁLISIS DEL PUNTO CRÍTICO ===")

# Punto crítico: resolver v = 0 y -2v - 5y = 0
punto_critico = np.array([0.0, 0.0])
print(f"1. Punto crítico encontrado: y = {punto_critico[0]}, v = {punto_critico[1]}")

# Matriz Jacobiana del sistema
A = np.array([[0, 1], 
              [-5, -2]])

# Calcular autovalores
autovalores = np.linalg.eigvals(A)
print(f"2. Autovalores de la matriz Jacobiana: {autovalores}")

# Clasificar el punto crítico basado en los autovalores
reales = autovalores.real
imaginarios = autovalores.imag

if np.all(reales < 0):
    if np.any(imaginarios != 0):
        clasificacion = "Foco estable (espiral estable)"
        estabilidad = "Asintóticamente estable"
    else:
        clasificacion = "Nodo estable"
        estabilidad = "Asintóticamente estable"
elif np.all(reales > 0):
    if np.any(imaginarios != 0):
        clasificacion = "Foco inestable (espiral inestable)"
        estabilidad = "Inestable"
    else:
        clasificacion = "Nodo inestable"
        estabilidad = "Inestable"
else:
    if np.any(imaginarios != 0) and np.all(reales == 0):
        clasificacion = "Centro"
        estabilidad = "Estabilidad marginal (oscilaciones sostenidas)"
    else:
        clasificacion = "Punto silla"
        estabilidad = "Inestable"

print(f"3. Clasificación: {clasificacion}")
print(f"4. Estabilidad: {estabilidad}")

# 3. Construir el plano de fase
print("\n=== CONSTRUYENDO PLANO DE FASE ===")

# Crear figura con dos subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Campo vectorial
y_range = np.linspace(-3, 3, 15)
v_range = np.linspace(-3, 3, 15)
Y, V = np.meshgrid(y_range, v_range)

# Calcular las derivadas en cada punto
dYdt = V
dVdt = -2*V - 5*Y

# Normalizar los vectores para mejor visualización
magnitud = np.sqrt(dYdt**2 + dVdt**2)
magnitud[magnitud == 0] = 1  # Evitar división por cero
dYdt_norm = dYdt / magnitud
dVdt_norm = dVdt / magnitud

# Dibujar campo vectorial
ax1.quiver(Y, V, dYdt_norm, dVdt_norm, magnitud, cmap='coolwarm', alpha=0.7, 
           scale=30, width=0.003)
ax1.set_xlabel('y (altura)', fontsize=12)
ax1.set_ylabel('v (velocidad)', fontsize=12)
ax1.set_title('Campo vectorial del sistema', fontsize=14)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)

# Marcar el punto crítico
ax1.plot(0, 0, 'ro', markersize=10, label='Punto crítico (0,0)')
ax1.legend()

# Subplot 2: Trayectorias en el plano de fase
condiciones_iniciales = [
    [2.0, 0.0],   # y=2, v=0
    [1.0, 2.0],   # y=1, v=2
    [-1.0, 2.0],  # y=-1, v=2
    [-2.0, 0.0],  # y=-2, v=0
    [-1.0, -2.0], # y=-1, v=-2
    [1.0, -2.0],  # y=1, v=-2
    [0.5, 0.0],   # y=0.5, v=0
    [-0.5, 0.0]   # y=-0.5, v=0
]

colores = plt.cm.tab10(np.linspace(0, 1, len(condiciones_iniciales)))

for i, (y0, v0) in enumerate(condiciones_iniciales):
    # Resolver el sistema para esta condición inicial
    t_span = [0, 15]  # Integrar hasta t=15
    sol = solve_ivp(sistema, t_span, [y0, v0], 
                   t_eval=np.linspace(0, 15, 1000),
                   method='RK45')
    
    # Dibujar la trayectoria
    ax2.plot(sol.y[0], sol.y[1], color=colores[i], 
            linewidth=2, alpha=0.8, label=f'({y0}, {v0})')
    
    # Marcar el punto inicial
    ax2.plot(y0, v0, 'o', color=colores[i], markersize=8)

ax2.set_xlabel('y (altura)', fontsize=12)
ax2.set_ylabel('v (velocidad)', fontsize=12)
ax2.set_title('Trayectorias en el plano de fase', fontsize=14)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.legend(loc='upper right', fontsize=8, ncol=2)

# Ajustar diseño y guardar
plt.tight_layout()
plt.savefig('plano_fase.png', dpi=150, bbox_inches='tight')
print("✓ Plano de fase guardado como 'plano_fase.png'")

# 4. Interpretación física
print("\n=== INTERPRETACIÓN FÍSICA ===")
print("El sistema modela un oscilador armónico amortiguado:")
print("• y(t) representa la altura o posición")
print("• v(t) = dy/dt representa la velocidad")
print("\nComportamiento observado en las trayectorias:")
print("1. Todas las trayectorias convergen en espiral hacia el origen (0,0)")
print("2. Esto indica que el sistema es ESTABLE asintóticamente")
print("3. La convergencia en espiral se debe a que los autovalores son complejos")
print("   con parte real negativa (-1 ± 2i)")
print("4. El amortiguamiento (-2v) disipa energía, haciendo que las oscilaciones")
print("   decaigan exponencialmente con el tiempo")
print("5. El término -5y representa la fuerza restauradora (como un resorte)")
print("\nEn resumen: Partiendo de cualquier condición inicial, el sistema")
print("oscila con amplitud decreciente hasta alcanzar el reposo en y=0, v=0.")

# Mostrar información adicional
print("\n=== INFORMACIÓN ADICIONAL ===")
print("Para ver el gráfico:")
print("1. Busca el archivo 'plano_fase.png' en tu carpeta actual")
print("2. Ábrelo con cualquier visor de imágenes")
print("\nSi necesitas ver el gráfico en pantalla, cambia plt.savefig() por plt.show()")


plt.show()