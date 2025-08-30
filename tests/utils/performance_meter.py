import time
import functools


def measure_performance(func):
    """
    Un decorador para medir e imprimir el tiempo de ejecución de una función.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        # Extrae el nombre del algoritmo del nombre de la función de test
        algo_name = func.__name__.replace("test_performance_", "")
        print(
            f"\n[Rendimiento] Algoritmo: {algo_name:<25} | Tiempo: {run_time:.6f} segundos"
        )

        return result

    return wrapper
