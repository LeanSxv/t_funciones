import math
import time
import os

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo con su radio

    Args:
        radio (float): El radio del circulo

    Returns:
        float: El área del circulo
    """
    PI = math.pi
    area = PI * radio**2
    return area

def verificar_par_o_impar(numero: int) -> str:
    """Verifica si un numero es par o impar

    Args:
        numero (float): Numero a verificar

    Returns:
        str: Si es par o impar
    """
    if numero % 2 == 0:
        mensaje = f'El numero es par'
    else:
        mensaje = f'El numero es impar'
    return mensaje

def suma_elementos_lista(lista: list)-> float:
    """Suma los elementos de una lista de numeros

    Args:
        lista (list): Lista de numeros

    Returns:
        float: Suma de elementos de la lista
    """
    sumatoria = 0
    for indice in range(len(lista)):
        sumatoria += lista[indice]
    return sumatoria

def saber_el_maximo(valor1: float, valor2: float, valor3:float) -> float:
    """Devuelve el valor maximo entre tres valores

    Args:
        valor1 (float): Primer valor
        valor2 (float): Segundo valor
        valor3 (float): Tercer valor

    Returns:
        float: El valor maximo
    """
    maximo = max(valor1, valor2, valor3)
    return maximo

def invertir_texto(texto: str) -> str:
    """Invierte un tiexto

    Args:
        texto (str): El texto a invertir

    Returns:
        str: El texto invertido
    """
    texto_invertido = texto[::-1]
    return texto_invertido

def ordenar_alfabeticamente_lista(lista: list) -> list:
    """Ordena alfabeticamente una lista

    Args:
        lista (list): Lista a ordenar

    Returns:
        list: Lista ordenada alfabeticamente
    """
    lista_ordenada = sorted(lista)
    return lista_ordenada

def calcular_pontencia(base: float, exponente: float) -> float:
    """Calcula una potencia a partir de la base y el exponente

    Args:
        base (float): Base de la potencia
        exponente (float): Exponente de la potencia

    Returns:
        float: Resultado de la potencia
    """
    resultado = base ** exponente
    return resultado

def lista_solo_pares(lista: list) -> list:
    """Devuelve los elementos pares de una lista de numeros

    Args:
        lista (list): Lista de numeros

    Returns:
        list: Lista de numeros pares
    """
    lista_pares = []
    for indice in range(len(lista)):
        if lista[indice] % 2 == 0:
            lista_pares.append(lista[indice])
    return lista_pares

def producto_lista(lista: list) -> float:
    """Calcula el producto de los elementos de una lista de numeros

    Args:
        lista (list): Lista de numeros

    Returns:
        float: Producto de los elementos de la lista
    """
    producto = 1
    for indice in range(len(lista)):
        producto *= lista[indice]
    return producto

def es_palindromo(texto: str) -> bool:
    """Verifica si el texto es un palindromo

    Args:
        texto (str): Texto a verificar

    Returns:
        bool: True si es palindromo, False si no lo es
    """
    if texto == invertir_texto(texto):
        return True
    else:
        return False
    
continuar = True    
    
while continuar:
    print(f'Menu:')
    print(f'1. Calcular el area de un circulo')
    print(f'2. Verificar si un numero es par o impar')
    print(f'3. Sumar los elementos de una lista')
    print(f'4. Determinar el valor maximo')
    print(f'5. Invertir un texto')
    print(f'6. Ordenar una lista alfabeticamente')
    print(f'7. Calcular potencia')
    print(f'8. Lista de numeros pares')
    print(f'9. Producto de una lista')
    print(f'10. Es un palindromo?')
    print(f'11. Salir')
    opcion = input('Seleccione una opcion: ')
    
    match opcion:
        case '1':
            radio_ingresado = float(input('Ingrese el radio del circulo: '))
            retorno = calcular_area_circulo(radio_ingresado)
            
        case '2':
            numero_ingresado = int(input('Ingrese un numero: '))
            retorno = verificar_par_o_impar(numero_ingresado)
            
        case '3':
            lista_creada = []
            prosiga = True
            while prosiga:
                numero_ingresado = input('Ingrese un numero (para salir ingrese "fin"): ')
                if numero_ingresado == 'fin':
                    prosiga = False
                else:
                    
                    lista_creada.append(float(numero_ingresado))
            retorno = suma_elementos_lista(lista_creada)
            
        case '4':
            valor1 = float(input('Ingrese el primer numero: '))
            valor2 = float(input('Ingrese el segundo numero: '))
            valor3 = float(input('Ingrese el tercer numero: '))
            retorno = saber_el_maximo(valor1, valor2, valor3)
            
        case '5':
            texto = input('Ingrese texto a invertir: ')
            retorno = invertir_texto(texto)
            
        case '6':
            lista_creada = []
            prosiga = True
            while prosiga:
                elemento_ingresado = input('Ingrese un texto (para terminar ingrese "fin"): ')
                if elemento_ingresado == 'fin':
                    prosiga = False
                else:
                    lista_creada.append(elemento_ingresado)
            retorno = ordenar_alfabeticamente_lista(lista_creada)
            
        case '7':
            base = float(input('Ingrese la base: '))
            exponente = float(input('Ingrese el exponente: '))
            retorno = calcular_pontencia(base, exponente)
            
        case '8':
            lista_creada = []
            prosiga = True
            while prosiga:
                elemento_ingresado = input('Ingrese un numero (para terminar ingrese "fin"): ')
                if elemento_ingresado == 'fin':
                    prosiga = False
                else:
                    lista_creada.append(int(elemento_ingresado))
            retorno = lista_solo_pares(lista_creada)
            
        case '9':
            lista_creada = []
            prosiga = True
            while prosiga:
                elemento_ingresado = input('Ingrese un numero (para terminar ingrese "fin"): ')
                if elemento_ingresado == 'fin':
                    prosiga = False
                else:
                    lista_creada.append(float(elemento_ingresado))
            retorno = producto_lista(lista_creada)
            
        case '10':
            texto = input('Ingrese texto a verificar: ')
            retorno = es_palindromo(texto)
            
        case '11':
            continuar = False
            retorno = 'Nos veremos pronto'
            
        case _:
            retorno = 'Opcion no valida, intente nuevamente.'
    
    os.system('cls')
    
    print(retorno)
    
    espera = 7
    for segundo in range(espera, 0, -1):
        print(f'Volviendo al menu en {segundo} segundos')
        time.sleep(1)
        
    os.system('cls')