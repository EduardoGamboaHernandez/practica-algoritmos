import pytest
import math

# Importa aquí los algoritmos probabilísticos
from algorithms.probabilistic.monte_carlo_pi import estimate_pi
from algorithms.probabilistic.miller_rabin import is_prime_miller_rabin
from algorithms.probabilistic.bloom_filter import BloomFilter
from algorithms.probabilistic.skip_list import SkipList
from algorithms.probabilistic.n_queens_las_vegas import solve_n_queens_las_vegas


def is_implemented(func_or_class):
    if isinstance(func_or_class, type):  # Es una clase
        # Chequea si los métodos clave están implementados
        return "pass" not in func_or_class.__init__.__code__.co_names
    # Es una función
    return (
        callable(func_or_class)
        and func_or_class.__code__.co_code != b"\x64\x01\x53\x00"
    )


def test_monte_carlo_pi():
    # Complejidad: O(n) donde n es el número de puntos
    if not is_implemented(estimate_pi):
        pytest.skip("Monte Carlo Pi no implementado.")

    # Con suficientes puntos, la estimación debería ser cercana a Pi
    pi_estimate = estimate_pi(100000)
    assert math.isclose(pi_estimate, math.pi, rel_tol=0.01)


def test_miller_rabin():
    # Complejidad: O(k * log^3 n)
    if not is_implemented(is_prime_miller_rabin):
        pytest.skip("Miller-Rabin no implementado.")

    assert is_prime_miller_rabin(29) is True
    assert is_prime_miller_rabin(997) is True
    assert is_prime_miller_rabin(30) is False
    assert is_prime_miller_rabin(1) is False
    assert is_prime_miller_rabin(4) is False


def test_bloom_filter():
    # Complejidad (add/check): O(k) donde k es el número de funciones hash
    if not is_implemented(BloomFilter):
        pytest.skip("Bloom Filter no implementado.")

    bf = BloomFilter(size=100, hash_count=4)
    bf.add("apple")
    bf.add("banana")

    assert "apple" in bf
    assert "banana" in bf
    # "cherry" podría dar un falso positivo, pero es poco probable con estos parámetros
    assert "cherry" not in bf


def test_skip_list():
    # Complejidad (search/insert): O(log n) en promedio
    if not is_implemented(SkipList):
        pytest.skip("Skip List no implementado.")

    sl = SkipList()
    elements = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    for el in elements:
        sl.insert(el)

    assert sl.search(19) is True
    assert sl.search(8) is False


def test_n_queens_las_vegas():
    if not is_implemented(solve_n_queens_las_vegas):
        pytest.skip("N-Queens (Las Vegas) no implementado.")

    solution = solve_n_queens_las_vegas(8)
    # Si encuentra una solución, debe ser válida
    if solution is not None:
        assert len(solution) == 8
        # (Test de validez simple) No hay dos reinas en la misma fila
        assert len(set(solution)) == 8
