import pytest
from unittest.mock import patch
from io import StringIO
from src.Ejercicio2 import main


@pytest.fixture
def user_input(monkeypatch):
    user_input = StringIO()
    monkeypatch.setattr("sys.stdin", user_input)
    return user_input


# Captura la salida del programa
@pytest.fixture
def capsys(capsys):
    return capsys


# Prueba unitaria para verificar el ingreso del número de aviones
def test_ejercicio2_ingreso(user_input, capsys):
    # Simula la entrada del usuario
    user_input.write("3\n")  # Número de aviones
    user_input.write("500\n")  # Altura del avión 1
    user_input.write("800\n")  # Altura del avión 2
    user_input.write("1000\n")  # Altura del avión 3
    user_input.seek(0)  # Vuelve al inicio del flujo de entrada

    # Ejecuta la función principal
    main()

    # Captura la salida del programa
    captured = capsys.readouterr()

    # Verifica que la salida contenga las líneas esperadas
    expected_output = [
        "¿Cuántos aviones desea incluir? "
        "Ingrese la altura del avión 1: "
        "Ingrese la altura del avión 2: "
        "Ingrese la altura del avión 3: "
        "El avión 1 debe estar a 226886.95 m de la torre de control",
        "El avión 2 debe estar a 299505.74 m de la torre de control",
        "El avión 3 debe estar a 339393.13 m de la torre de control",
        "El promedio de las alturas es 766.67",
    ]
    assert captured.out.splitlines() == expected_output


# Prueba unitaria para verificar el ingreso del número de aviones
def test_ejercicio2_valor_invalido(user_input, capsys):
    # Simula la entrada del usuario
    user_input.write("-5\n")  # Número de aviones
    user_input.seek(0)  # Vuelve al inicio del flujo de entrada

    # Ejecuta la función principal
    main()

    # Captura la salida del programa
    captured = capsys.readouterr()

    # Verifica que la salida contenga las líneas esperadas
    expected_output = [
        "¿Cuántos aviones desea incluir? "
        "El número de aviones debe ser mayor que cero."
    ]
    assert captured.out.splitlines() == expected_output


# Ejecuta las pruebas con pytest
if __name__ == "__main__":
    pytest.main()
