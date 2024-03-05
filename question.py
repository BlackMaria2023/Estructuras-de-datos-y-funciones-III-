import preguntas as p
import random
from shuffle import shuffle_alt
from preguntas import pool_preguntas

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = pool_preguntas[dificultad]
    
    question_number = random.choice(list(preguntas.keys()))
    
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas.pop(question_number)
    alternativas = shuffle_alt(pregunta)
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')