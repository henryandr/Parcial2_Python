import pytest
from src.Ejercicio1 import fahrenheit_a_celsius

# Define los casos de prueba y sus valores de entrada y salida esperados
test_cases = [
    ([32.0], [0.0]),
    ([98.6, 212.0, -40.0], [37.0, 100.0, -40.0]),
    ([68.0, -22.0, 50.0], [20.0, -30.0, 10.0]),
    ([0, 100, -22], [-17.78, 37.78, -30.0]),  # Valores enteros
    (32, TypeError),  # Entero como entrada, esperamos un TypeError
    (-5, TypeError),  # Entero negativo como entrada, esperamos un TypeError
]


# Utiliza el decorador para generar pruebas para cada caso
@pytest.mark.parametrize("entrada, esperado", test_cases)
def test_fahrenheit_a_celsius(entrada, esperado):
    if esperado == TypeError:
        # Verificamos que se lance un TypeError
        with pytest.raises(TypeError):
            resultado = fahrenheit_a_celsius(entrada)
    else:
        # Verificamos el resultado si no esperamos un TypeError
        resultado = fahrenheit_a_celsius(entrada)
        assert resultado == esperado
