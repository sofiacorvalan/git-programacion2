"""Type, Comprensión de Listas, Sorted y Filter."""

import string
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    respuesta=[]
    letras=[]
    num=[]
    
    for i in lista:
        if type(i)==str:
            letras.append(i)
        elif type(i)==int:
            num.append(i)

    respuesta.extend(letras)
    respuesta.extend(num)

    return respuesta



# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    letras=[]
    numeros=[]
    respuesta=[]

    letras = [num for num in lista if type(num)==str]
    numeros= [num for num in lista if type(num)==int]

    respuesta.extend(letras)
    respuesta.extend(numeros)

    return respuesta



# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
