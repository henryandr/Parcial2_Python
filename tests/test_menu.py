import pytest
from unittest.mock import patch
from io import StringIO
from src.Ejercicio1 import menu


def test_menu_opcion_valida():
    # Se crea un simulacro de la función input() para devolver el valor 1
    mock_input = patch("builtins.input", return_value=1)

    # Se inicia el parcheo de la función input()
    with mock_input:
        # Se ejecuta la función de menú
        assert menu() == 1

    # Se detiene el parcheo de la función input()
    mock_input.stop()


def test_menu_opcion_salida():
    # Se crea un simulacro de la función input() para devolver el valor 3
    mock_input = patch("builtins.input", return_value=3)

    # Se inicia el parcheo de la función input()
    with mock_input:
        # Se ejecuta la función de menú
        assert menu() == 3

    # Se detiene el parcheo de la función input()
    mock_input.stop()


# Simula la entrada del usuario
@pytest.fixture
def user_input(monkeypatch):
    user_input = StringIO()
    monkeypatch.setattr("sys.stdin", user_input)
    return user_input


# Captura la salida del programa
@pytest.fixture
def capsys(capsys):
    return capsys


# Prueba para la función main()
def test_menu_opcion_invalida(user_input, capsys):
    # Simula la entrada del usuario
    user_input.write("4\n")  # opción inválida
    user_input.write("3\n")  # Salir del programa
    user_input.seek(0)  # Vuelve al inicio del flujo de entrada

    # Ejecuta la función menu
    menu()

    # Captura la salida del programa
    captured = capsys.readouterr()

    # Verifica que el programa haya respondido como se esperaba
    assert "Opción no válida. Por favor, ingrese 1, 2 o 3." in captured.out
