"""Pruebas de la calculadora de multas."""
import pytest
from biblioteca import calcular_multa


def test_calcula_multa_por_retraso():
    assert calcular_multa(3, 2) == 6


def test_no_hay_multa_sin_retraso():
    assert calcular_multa(0, 2) == 0


def test_rechaza_dias_negativos():
    with pytest.raises(ValueError):
        calcular_multa(-1, 2)


def test_rechaza_tarifa_negativa():
    with pytest.raises(ValueError):
        calcular_multa(2, -1)
