import pytest
import numpy as np
from tests.utils.performance_meter import measure_performance

# Importa aquí las funciones de ordenamiento
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort

SORTING_FUNCTIONS = [
    (bubble_sort, "Bubble Sort"),
    (selection_sort, "Selection Sort"),
    (insertion_sort, "Insertion Sort"),
    (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
]


@pytest.mark.parametrize("sort_func, name", SORTING_FUNCTIONS)
def test_sorting_correctness(sort_func, name):
    """Test para verificar la correctitud de los algoritmos de ordenamiento."""
    if not callable(sort_func) or sort_func.__code__.co_code == b"\x64\x01\x53\x00":
        pytest.skip(f"{name} no implementado.")

    test_cases = [
        ([], []),
        ([1], [1]),
        ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
        ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),
        ([1, 1, 2, 1, 2], [1, 1, 1, 2, 2]),
    ]

    for unsorted, expected in test_cases:
        # Hacemos una copia para no modificar la lista original en el test
        result = sort_func(unsorted.copy())
        assert result == expected, f"{name} falló con la entrada {unsorted}"


# --- Tests de Rendimiento y Complejidad ---


@pytest.fixture(params=[100, 1000, 5000])
def sorting_performance_data(request):
    """Genera datos de diferentes tamaños para tests de rendimiento."""
    size = request.param
    data = np.random.randint(0, size, size).tolist()
    return data, size


@pytest.mark.parametrize("sort_func, name", SORTING_FUNCTIONS)
def test_sorting_performance(sort_func, name, sorting_performance_data):
    """
    Test de rendimiento. Observa cómo los algoritmos O(n^2) (Bubble, Selection, Insertion)
    se vuelven mucho más lentos que los O(n log n) (Merge, Quick) a medida que aumenta el tamaño.
    """
    if not callable(sort_func) or sort_func.__code__.co_code == b"\x64\x01\x53\x00":
        pytest.skip(f"{name} no implementado.")

    data, size = sorting_performance_data

    @measure_performance
    def run_sort():
        sort_func(data)

    print(f"\nEjecutando {name} con {size} elementos...")
    run_sort()
