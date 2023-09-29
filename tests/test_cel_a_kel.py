import pytest
from src.Ejercicio1 import celsius_a_kelvin

# Define los casos de prueba y sus valores de entrada y salida esperados
test_cases = [
    ([0.0], [273.15]),
    ([25.0, -10.0, 100.0], [298.15, 263.15, 373.15]),
    ([-20.0, -40.0, -273.15], [253.15, 233.15, 0.0]),
    ([32, 100, -40], [305.15, 373.15, 233.15]),  # Valores enteros
    (0, TypeError),  # Entero como entrada, esperamos un TypeError
    (-5, TypeError),  # Entero negativo como entrada, esperamos un TypeError
]


# Utiliza el decorador para generar pruebas para cada caso
@pytest.mark.parametrize("entrada, esperado", test_cases)
def test_celsius_a_kelvin(entrada, esperado):
    if esperado == TypeError:
        # Verificamos que se lance un ValueError
        with pytest.raises(TypeError):
            resultado = celsius_a_kelvin(entrada)
    else:
        # Verificamos el resultado si no esperamos un ValueError
        resultado = celsius_a_kelvin(entrada)
        assert resultado == esperado
