def find(search_list, value):
    #Ordeno la lista
    search_list.sort()

    #Lista auxiliar que irá disminuyendo en la búsqueda
    aux_list = sorted(search_list)

    #Si el valor no está en la lista lanzo excepción
    if value not in aux_list:
            raise ValueError("No se encontró")

    #Mientras hayan valores en la lista seguimos buscando
    while(aux_list):
        #Definición de la mitad de la lista
        medium = (len(aux_list) - 1) // 2
        
        #Encontramos el valor
        if value == aux_list[medium]:
            return search_list.index(value), aux_list[medium]
    
        #Si no encontramos el valor, reducimos la lista y
        #apuntamos hacia donde esté el valor que buscamos

        #Se corta la lista a la mitad y se apunta a la izquierda
        if aux_list[medium] > value:
            aux_list = aux_list[:medium + 1]
        
        #Se corta la lista a la mitad y se apunta a la derecha
        if aux_list[medium] < value:
            aux_list = aux_list[medium + 1:]




if __name__ == "__main__":
    lista = [1,15,65,9,8,7,92,3,6,5]
    lista_2 = [1]
    lista_3 = [1, 3, 4, 6, 8, 9, 11]
    print(find(lista, 11))
    print(find(lista_3, 11))