# Ejercicio 1: Conversión de Temperaturas (Valor: 2.5)

En este ejercicio debes crear un programa que convierta entre unidades de temperatura. Para ello, vas a organizar el programa de la siguiente manera: 
## Función menu() (Valor: 0.8)
Debe imprimir las siguientes opciones:

1. Convertir de grados Celsius a Kelvin.
2. Convertir de grados Fahrenheit a grados Celsius.
3. Salir del programa.

### Requisitos Funcionales:

1. Mostrar un menú con las tres opciones mencionadas anteriormente.
2. Solicitar al usuario que ingrese el número de la opción deseada.
3. Validar la entrada del usuario para asegurarse de que sea un número entero válido y que esté dentro del rango de opciones (1, 2 o 3). Si la entrada no es válida, mostrar un mensaje de error y volver a solicitar la entrada hasta que sea válida.
4. Retornar el número de opción ingresado por el usuario.

## Función celsius_a_kelvin(lista_celsius) (Valor 0.8)

Recibe como parámetro una lista de temperaturas en grados Celsius y realiza la conversión de cada temperatura a Kelvin utilizando la siguiente fórmula:

$$ Kelvin (°K) = Celsius (°C) + 273.15 $$ 

### Requisitos Funcionales:

1. Recibe como argumento una lista de temperaturas en grados Celsius.
2. Calcula la equivalencia en Kelvin para cada dato de la lista con la fórmula mencionada.
3. Los datos que se guardan en la lista deben estar redondeados a dos decimales. Para ello utilice la función `round()`. Por ejemplo: $$dato = round(dato,2)$$
4. Retorna una lista con las temperaturas en grados Kelvin en el mismo orden en que se encontraban en la lista original.

## Función fahrenheit_a_celsius(lista_farhenheit) (Valor 0.9)

Convierte de temperaturas en grados Fahrenheit a grados Celsius para una lista de temperaturas.
Utiliza la siguiente ecuación:
$$Celsius = (Fahrenheit - 32) \times \frac{5}{9}$$

### Requisitos funcionales:

1. La función debe recibir una lista con las temperaturas en grados Fahrenheit.
2. La función debe calcular la temperatura equivalente en grados Celsius para cada valor de la lista.
3. Cada resultado debe ser redondeado a dos cifras decimales utilizando la función `round()`. Por ejemplo: $$dato = round(dato,2)$$
4. La función debe retornar una lista que contenga las temperaturas en grados Celsius.

### Ejemplo de uso de la función:

```python
>>> fahrenheit_a_celsius([32.0, 98.6, -40.0])
[0.0, 37.0, -40.0]
```
## Función `main()`

El objetivo de la función `main()` es proporcionar un menú interactivo que permita al usuario realizar diversas conversiones de temperatura.

### Requisitos funcionales:

1. La función `main()` debe implementar un menú interactivo repetitivo utilizando un bucle `while`.
2. Debe utilizar la función `menu()` para permitir al usuario seleccionar una de las opciones posibles. 
3. Según la opción seleccionada por el usuario, debe realizar las siguientes acciones:
   - Llamar a la función `genera_aleatorios()` para generar una lista de números aleatorios y almacenarla en una variable.
   - Llamar a la función correspondiente según la elección del usuario.
   - Imprimir en pantalla la lista resultante.
4. El menú repetitivo debe continuar hasta que el usuario elija la opción de salida.

---
# Ejercicio 2: Comunicaciones con la torre de control (Valor 2.5)

Una de las bandas del espectro electromagnético que usan los aviones para comunicarse con las torres de control es la VHF (_Very High Frequency_). Esta banda de comunicación necesita línea de vista para funcionar correctamente, por lo que la curvatura de la tierra afecta su desempeño. Para determinar la distancia desde la que puede haber comunicación se usa la ecuación:

$$d = \sqrt{2R(h_a-h_t)}$$
donde $R$ corresponde al radio de la tierra ($R = 63710008~m$), $h_a$ la altura del avión y $h_t$ la altura de la torre de control.

Realice un programa que cumpla con los siguientes requisitos:

### Requisitos funcionales:
1.	Pedir al usuario de cuántos aviones desea ingresar la altura.
2.	Verificar que el número ingresado sea mayor que cero. En caso contrario, imprimir en pantalla la frase: `"El número de aviones debe ser mayor que cero."` y terminar el programa.
3. Pedir las alturas, en metros, de cada uno de los aviones que el usuario dijo que iba a ingresar. Almacene esta información en una lista.
4.	Una vez tenga la lista con las alturas de los aviones, construya otra lista con la distancia desde la que puede haber comunicación con la torre de control. Asuma siempre una altura de la torre de control de $96~m$.
5.	Muestre para cada avión la distancia a la que debe estar de la torre de control para tener comunicación. Imprima la información de cada avión por separado, no imprimir la variable que contiene la lista.
6.	Calcule la altura promedio de los aviones ingresados por el usuario e imprima el resultado en pantalla.

### Ejemplo de uso del programa
```c
¿Cuántos aviones desea incluir? 3
Ingrese la altura del avión 1: 200
Ingrese la altura del avión 2: 1000
Ingrese la altura del avión 3: 850

El avión 1 debe estar a 115115.95 m de la torre de control
El avión 2 debe estar a 339393.13 m de la torre de control
El avión 3 debe estar a 309959.18 m de la torre de control
El promedio de las alturas es 1025.00
```
