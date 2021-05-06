"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
#Codigo modificado por:
#Autor: Arturo Cuauhtémoc Ruiz Leyva
#Autor: Andrea Vianey Díaz Álvarez

"""Se importan las librerías que se usan en el código"""
import turtle       #Para usar las funciones de turtle 
from turtle import *
from freegames import vector


def line(start, end):
    """
    Draw line from start to end.
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x,end.y)


def square(start, end):
    """
    Draw square from start to end.
    """
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """
    Dibuja un circulo con radio (end.x-start.x)/2
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    turtle.circle((end.x-start.x)/2)    
    end_fill()


def rectangle(start, end):
    """
    Draw rectangle from start to end.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """
    Draw triangle from start to end.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
    for count in range(2):
        left(90)
    end_fill()


def tap(x, y):
    """
    Store starting point or draw shape.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """
    Store value in state at key.
    """
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)     #Define la ubicacion de la pantalla 
onscreenclick(tap)     
listen()         #Escucha los eventos del teclado
onkey(undo, 'u')

#Define las teclas que cambian de color 
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')

#Define la letras que cambian las figuras 
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()