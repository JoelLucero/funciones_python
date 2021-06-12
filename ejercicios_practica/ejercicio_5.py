import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice
def lista(inicio=1,fin=6,cantidad=5):
    dados_guardados = []
    for i in range(cantidad):
        numeros= random.randrange(inicio,fin+1) 
        dados_guardados.append(numeros)
    return dados_guardados


# --------------------------------
def contar_guardados(lista_numeros):
     max_repeticiones = max(lista_numeros, key=lista_numeros.count)
     print("El numero que se repite es: ", max_repeticiones)
     return max_repeticiones

def guardas_dados(cantidad_iguales,dados_tirados):
    for x in dados_tirados:
        if x == cantidad_iguales:
            dados_guardados.append(x)
    return dados_guardados



if __name__ == '__main__':
    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca al as funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    dados_guardados= []
    dados_tirados =lista()
    print("Los numeros aleatorios son:",dados_tirados)
    cantidad_iguales = contar_guardados (dados_tirados)
    dados_guardados = guardas_dados (cantidad_iguales,dados_tirados)
    print("El dado",cantidad_iguales,"Es el mas repetido",len(dados_guardados),"veces")