from functools import reduce


def main():

    #FILTER: filter devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
    first_list = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2 != 0, first_list))
    print(odd)

    #MAP: su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.
    second_list = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, second_list))
    print(squares)

    #REDUCE: toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.
    third_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a * b, third_list)
    print(all_multiplied)


if __name__ == '__main__':
    main()