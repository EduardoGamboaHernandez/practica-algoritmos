import pytest
import numpy as np
from tests.utils.performance_meter import measure_performance

# Importa aquí las funciones de búsqueda que vas a implementar
from algorithms.search.linear_search import linear_search
from algorithms.search.binary_search import binary_search
from algorithms.search.jump_search import jump_search
from algorithms.search.interpolation_search import interpolation_search
from algorithms.search.exponential_search import exponential_search


@pytest.fixture
def test_data():
    """Fixture para generar datos de prueba."""
    return list(range(100))


@pytest.mark.parametrize(
    "search_func, name",
    [
        (linear_search, "Linear Search"),
        (binary_search, "Binary Search"),
        (jump_search, "Jump Search"),
        (interpolation_search, "Interpolation Search"),
        (exponential_search, "Exponential Search"),
    ],
)
def test_search_correctness(search_func, name, test_data):
    """Test para verificar la correctitud de los algoritmos de búsqueda."""
    # Skip si la función no está implementada
    if (
        not callable(search_func) or search_func.__code__.co_code == b"\x64\x01\x53\x00"
    ):  # pass
        pytest.skip(f"{name} no implementado.")

    # Elemento presente
    target_present = 55
    assert search_func(test_data, target_present) == 55, (
        f"{name} falló al encontrar un elemento existente."
    )

    # Elemento no presente
    target_absent = 101
    assert search_func(test_data, target_absent) == -1, (
        f"{name} falló al no encontrar un elemento inexistente."
    )

    # Borde: primer elemento
    assert search_func(test_data, 0) == 0, f"{name} falló con el primer elemento."

    # Borde: último elemento
    assert search_func(test_data, 99) == 99, f"{name} falló con el último elemento."


# --- Tests de Rendimiento y Complejidad ---
# La complejidad se analiza observando los tiempos de ejecución.


@pytest.fixture
def large_test_data():
    """Genera una lista grande para tests de rendimiento."""
    return list(range(1_000_000))


@measure_performance
def test_performance_linear_search(large_test_data):
    # Complejidad: O(n)
    linear_search(large_test_data, 999_999)


@measure_performance
def test_performance_binary_search(large_test_data):
    # Complejidad: O(log n)
    binary_search(large_test_data, 999_999)


@measure_performance
def test_performance_jump_search(large_test_data):
    # Complejidad: O(sqrt(n))
    jump_search(large_test_data, 999_999)
