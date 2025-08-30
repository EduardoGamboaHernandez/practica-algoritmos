import pytest

# Importa aquí los algoritmos voraces
from algorithms.greedy.fractional_knapsack import fractional_knapsack
from algorithms.greedy.dijkstra import dijkstra
from algorithms.greedy.prim import prim
from algorithms.greedy.kruskal import kruskal
from algorithms.greedy.activity_selection import activity_selection


def is_implemented(func):
    return callable(func) and func.__code__.co_code != b"\x64\x01\x53\x00"


def test_fractional_knapsack():
    # Complejidad: O(n log n) por el ordenamiento
    if not is_implemented(fractional_knapsack):
        pytest.skip("Fractional Knapsack no implementado.")

    capacity = 50
    items = [
        {"weight": 10, "value": 60},
        {"weight": 20, "value": 100},
        {"weight": 30, "value": 120},
    ]
    # Valor esperado: 60 (item1) + 100 (item2) + 20/30 * 120 (item3) = 240
    assert abs(fractional_knapsack(capacity, items) - 240.0) < 1e-9


def test_dijkstra():
    # Complejidad: O(E log V) con min-heap
    if not is_implemented(dijkstra):
        pytest.skip("Dijkstra no implementado.")

    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    expected_distances = {"A": 0, "B": 1, "C": 3, "D": 4}
    assert dijkstra(graph, "A") == expected_distances


def test_prim():
    # Complejidad: O(E log V) con min-heap
    if not is_implemented(prim):
        pytest.skip("Prim no implementado.")

    graph = {
        "A": {"B": 2, "D": 5},
        "B": {"A": 2, "C": 1, "D": 1},
        "C": {"B": 1, "D": 3},
        "D": {"A": 5, "B": 1, "C": 3},
    }
    mst = prim(graph, "A")
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 4  # Aristas (A,B,2), (B,C,1), (B,D,1)


def test_kruskal():
    # Complejidad: O(E log E) por el ordenamiento de aristas
    if not is_implemented(kruskal):
        pytest.skip("Kruskal no implementado.")

    edges = [("A", "B", 2), ("A", "D", 5), ("B", "C", 1), ("B", "D", 1), ("C", "D", 3)]
    mst = kruskal(edges)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 4


def test_activity_selection():
    # Complejidad: O(n log n) por el ordenamiento
    if not is_implemented(activity_selection):
        pytest.skip("Activity Selection no implementado.")

    activities = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 9),
        (5, 9),
        (6, 10),
        (8, 11),
        (8, 12),
        (2, 14),
        (12, 16),
    ]
    selected = activity_selection(activities)
    assert selected == [(1, 4), (5, 7), (8, 11), (12, 16)]
