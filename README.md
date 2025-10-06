# Curso de Procesos Estocásticos en Python
¿Te ha interesado alguna vez  modelar fenómenos como el clima, el tráfico o el comportamiento del mercado financiero? Estos fenomenos si lo observas detenidamente, parecen tener un comportamiento poco predecible, mejor dicho parecen impredecible  u aleatorio. ¿Pero sabias que estos procesos aleatorios se pueden modelar? Esto es posible gracias a los procesos estocásticos, que son herramientas matemáticas que nos permiten analizar y predecir el comportamiento de sistemas que evolucionan de manera aleatoria a lo largo del tiempo.


Este curso te introduce a los fundamentos de los procesos estocásticos utilizando Python, una de las herramientas más populares en ciencia de datos y análisis estadístico. A lo largo del curso, aprenderás a implementar modelos estocásticos, simular procesos aleatorios y aplicar estos conceptos a problemas del mundo real.
# Objetivos
## Objetivo General
Desarrollar la capacidad de modelar, analizar y simular sistemas estocásticos utilizando Python, aplicando los fundamentos de la teoría de probabilidades, cadenas de Markov y teoría de colas en contextos reales de ingeniería, datos y sistemas.
## Objetivos Específicos
- Comprender los fundamentos de los procesos estocásticos, su clasificación, propiedades y aplicaciones en distintos dominios (finanzas, transporte, producción, servicios, entre otros).

- Analizar y simular cadenas de Markov en tiempo discreto y continuo, identificando su estructura, estados recurrentes, absorbentes y ergódicos, así como su distribución estacionaria.

- Implementar simulaciones de procesos de Markov con Python, construyendo y visualizando matrices de transición, trayectorias de estados y grafos de transición.

- Aplicar la teoría de colas para modelar sistemas de servicio, evaluando métricas de desempeño como número promedio de clientes en el sistema, tiempo de espera y utilización del servidor.

- Modelar y analizar sistemas de colas de un solo servidor, múltiples servidores y redes de colas (modelos de Jackson) mediante simulaciones computacionales y análisis de equilibrio.

- Interpretar los resultados obtenidos a partir de modelos estocásticos, relacionándolos con problemas reales y formulando estrategias de optimización o mejora en procesos productivos o de servicios.
# Contenido del repositorio
Este repositorio contiene material didáctico, ejemplos prácticos y proyectos en Python para el estudio de Procesos Estocásticos. Está orientado a estudiantes y profesionales de áreas como estadística, matemáticas aplicadas, ingeniería e inteligencia artificial que deseen comprender y aplicar herramientas de probabilidad y simulación en la modelación de sistemas aleatorios.

El curso combina teoría y práctica, cubriendo desde cadenas de Markov hasta procesos continuos, con ejemplos implementados en NumPy, pandas y matplotlib.
📑 Módulos sugeridos del curso

1. Introducción a procesos estocásticos

2. Variables aleatorias y cadenas de tiempo

3. Ejemplos prácticos

4. Cadenas de Markov en tiempo discreto

Matrices de transición

Estados recurrentes y absorbentes

Ejemplos con fútbol, consumo y máquinas

Simulación Monte Carlo en Python

Generación de números aleatorios

Aplicaciones en estimación de probabilidades

Procesos de Poisson y renovación

Modelado de llegadas y tiempos de espera

Simulación en Python

Cadenas de Markov en tiempo continuo

Generadores infinitesimales

Aplicaciones en confiabilidad

Aplicaciones avanzadas

Procesos estocásticos en Machine Learning y Data Science
Procesos-Estocasticos-Python/
│
├── 📄 README.md                  -> Descripción general del curso
├── 📁 notebooks/                 -> Notebooks con teoría y ejercicios prácticos
│   ├── 01_Introduccion.ipynb
│   ├── 02_Cadenas_Markov_Discretas.ipynb
│   ├── 03_Cadenas_Markov_Absorbentes.ipynb
│   ├── 04_Simulacion_MonteCarlo.ipynb
│   ├── 05_Procesos_Poisson.ipynb
│   ├── 06_Procesos_Renovacion.ipynb
│   ├── 07_Cadenas_Markov_Continuas.ipynb
│   └── 08_Aplicaciones_MachineLearning.ipynb
│
├── 📁 data/                      -> Conjuntos de datos usados en ejemplos
│   ├── futbol_liverpool.csv
│   ├── consumo_productos.csv
│   └── voltaje_maquina.csv
│
├── 📁 scripts/                   -> Funciones y módulos en Python reutilizables
│   ├── markov_chain.py
│   ├── poisson_process.py
│   └── simulacion_utils.py
│
├── 📁 projects/                  -> Proyectos aplicados
│   ├── proyecto_liverpool_markov/
│   │   ├── README.md
│   │   └── liverpool_markov.ipynb
│   ├── proyecto_consumo/
│   │   ├── README.md
│   │   └── simulacion_consumo.ipynb
│   └── proyecto_voltaje_maquina/
│       ├── README.md
│       └── voltaje_markov.ipynb
│
├── requirements.txt              -> Librerías necesarias (numpy, pandas, matplotlib, scipy, jupyter)
└── LICENSE                       -> Licencia del proyecto
