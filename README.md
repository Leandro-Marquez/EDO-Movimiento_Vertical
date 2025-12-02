Proyecto Conjunto EDO y Matemática Numérica
Tema 2: Movimiento vertical y aceleración gravitacional Curso 2025–2026, Universidad de La Habana

🎯 Objetivo
Este proyecto aplica Ecuaciones Diferenciales Ordinarias (EDO) y Matemática Numérica (MN) para modelar y analizar el movimiento vertical bajo aceleración gravitacional. Se busca integrar modelación física, análisis teórico, simulación numérica y visualización interactiva.

📂 Estructura del Proyecto
informe.pdf → Documento técnico (máx. 10 páginas) con:

Introducción y modelado del problema.

Análisis teórico (existencia, unicidad, estabilidad).

Comparación de algoritmos numéricos.

Tablas de errores, orden de convergencia y costo computacional.

Gráficos: soluciones, campos de isoclinas, diagramas de bifurcación y planos de fase.

notebooks/ → Carpeta con cuadernos interactivos en Python:

parteA_isoclinas.ipynb → Cinemática vertical, cálculo de velocidad inicial y campo de isoclinas.

parteB_bifurcacion.ipynb → Diagrama de bifurcación con parámetro 
𝑝
.

parteC_plano_fase.ipynb → Plano de fase del sistema altura–velocidad y clasificación de puntos críticos.

data/ → Benchmarks y ejemplos con soluciones analíticas conocidas.

src/ → Código auxiliar en Python (funciones de integración numérica, análisis de error, visualización).

⚙️ Instalación y Requisitos
Instalar Python 3.10+

Instalar librerías necesarias:

bash
pip install numpy scipy matplotlib plotly
Abrir los notebooks con Jupyter o VS Code.

🚀 Ejecución
Parte A (Isoclinas): Ejecutar parteA_isoclinas.ipynb para calcular la velocidad inicial del proyectil y graficar el campo de isoclinas.

Parte B (Bifurcación): Ejecutar parteB_bifurcacion.ipynb para obtener los puntos de equilibrio según el parámetro 
𝑝
, clasificar su estabilidad y visualizar el diagrama de bifurcación.

Parte C (Plano de fase): Ejecutar parteC_plano_fase.ipynb para calcular puntos críticos del sistema altura–velocidad, clasificarlos y graficar el plano de fase.

📊 Métodos Numéricos
Se implementan y comparan al menos dos algoritmos:

Euler explícito

Runge–Kutta de orden 4 (RK4)

Se evalúan:

Error relativo.

Estabilidad (análisis hacia adelante y hacia atrás).

Orden de convergencia.

Complejidad computacional.