import pytest

# Importa aquí los algoritmos de PD
from algorithms.dynamic_programming.fibonacci_memo import fibonacci_memo
from algorithms.dynamic_programming.knapsack_01 import knapsack_01
from algorithms.dynamic_programming.longest_common_subsequence import lcs
from algorithms.dynamic_programming.coin_change import coin_change
from algorithms.dynamic_programming.matrix_chain_multiplication import (
    matrix_chain_order,
)


def is_implemented(func):
    return callable(func) and func.__code__.co_code != b"\x64\x01\x53\x00"


def test_fibonacci_memo():
    # Complejidad: O(n)
    if not is_implemented(fibonacci_memo):
        pytest.skip("Fibonacci (Memoization) no implementado.")
    assert fibonacci_memo(10) == 55
    assert fibonacci_memo(1) == 1


def test_knapsack_01():
    # Complejidad: O(n*W) donde n es el número de items y W la capacidad
    if not is_implemented(knapsack_01):
        pytest.skip("Knapsack 0/1 no implementado.")

    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)
    assert knapsack_01(capacity, weights, values, n) == 220


def test_lcs():
    # Complejidad: O(m*n) donde m y n son las longitudes de las cadenas
    if not is_implemented(lcs):
        pytest.skip("Longest Common Subsequence no implementado.")

    X = "AGGTAB"
    Y = "GXTXAYB"
    assert lcs(X, Y) == 4  # "GTAB"


def test_coin_change():
    # Complejidad: O(amount * n) donde n es el número de monedas
    if not is_implemented(coin_change):
        pytest.skip("Coin Change no implementado.")

    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1


def test_matrix_chain_order():
    # Complejidad: O(n^3)
    if not is_implemented(matrix_chain_order):
        pytest.skip("Matrix Chain Multiplication no implementado.")

    dims = [10, 30, 5, 60]  # Matrices A1(10x30), A2(30x5), A3(5x60)
    assert matrix_chain_order(dims) == 4500  # (A1*A2)*A3
