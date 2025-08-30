# Prácticas de Complejidad Algorítmica en Python

Este repositorio es una recopilación de diversos algoritmos escritos en Python. Su objetivo es facilitar el aprendizaje sobre la complejidad algorítmica y el desarrollo de la lógica de programación.

## Estructura del Proyecto
El proyecto tiene la siguiente estructura, manteniendo separada la lógica algorítmica de las pruebas.
```
 ├── algorithms/
 │ ├── search/     # Algoritmos de búsqueda
 │ └── sorting/    # Algoritmos de ordenamiento
 ├── tests/        # Pruebas unitarias y de rendimiento para los algoritmos
 ├── utils/        # Herramientas y utilidades, como el medidor de rendimiento
 ├── algorithms/
 │ ├── dynamic_programming/  # Algoritmos de Programación Dinámica
 │ ├── greedy/               # Algoritmos Voraces (Greedy)
 │ ├── probabilistic/        # Algoritmos Probabilísticos
 │ └── sorting/              # Algoritmos de Ordenamiento
 ├── tests/
 │ ├── utils/         # Herramientas para las pruebas (ej. medidor de rendimiento)
 │ └── ...            # Archivos de pruebas
 ├── requirements.txt # Dependencias del proyecto
 └── README.md

```

## Instalación
Después de clonar el repositorio y crear un entorno virtual, es necesario instalar las dependencias para poder ejecutar las pruebas con [pytest](https://docs.pytest.org/en/stable/) y formatear el código con [ruff](https://docs.astral.sh/ruff/).

```
pip install -r requirements.txt
```


## Ejecución de Pruebas
Las pruebas son una parte fundamental de este proyecto para garantizar que los algoritmos sean correctos y para medir su rendimiento. Utilizamos `pytest` para la ejecución de las mismas.

Desde el directorio raíz del proyecto, ejecuta el siguiente comando en una terminal:
```
pytest -v
```
El flag `-v` (verbose) mostrará un desglose detallado de cada prueba ejecutada. Las pruebas de rendimiento imprimirán en la consola el tiempo que tardan en ejecutarse, permitiéndote comparar su eficiencia.

## Formato de código
Para mantener una sintaxis que cumpla con las reglas de la PEP 8, debes ejecutar el comando `ruff format` después de escribir tu código. Esto asegurará que el código tenga una presentación estética y coherente.