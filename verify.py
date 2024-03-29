import preguntas as p

def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    respuesta_correcta = next(filter(lambda x: x[1] == 1, alternativas))[0]
    if eleccion == respuesta_correcta:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
    
if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






