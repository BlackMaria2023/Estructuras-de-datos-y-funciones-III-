def choose_level(n_pregunta, p_level):
    basica, intermedia, avanzada = 1, 2, 3

    if p_level == 2:
        if n_pregunta in [1, 2]:
           return basica
        elif n_pregunta in [3, 4]:
            return intermedia
        elif n_pregunta in [5, 6]:
            return avanzada
    elif p_level == 3:
        if n_pregunta in [1, 2, 3]:
            return basica
        elif n_pregunta in [4, 5, 6]:
            return intermedia
        elif n_pregunta in [7, 8, 9]:
            return avanzada

if __name__ == '__main__':
    pregunta_numero = 4
    preguntas_por_nivel = 3
    print(choose_level(pregunta_numero, preguntas_por_nivel))
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias