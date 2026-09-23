# main.py

from turtle import *  # Importa funções e classes da turtle
from interface_paint import *  # Importa e desenha a interface gráfica

v = 0  # Velocidade máxima da tartaruga (0 = instantâneo)
step = 10  # Passo de movimentação ao usar as setas

# Cria e configura a tartaruga de desenho
t = Turtle()
t.color('black')  # Cor inicial do pincel
t.width(5)  # Espessura inicial do traço
t.shape('circle')  # Aparência da tartaruga
t.pendown()
t.speed(v)

# ----------------------------------------
# Funções de controle por eventos
# ----------------------------------------

# Desenha seguindo o movimento do mouse (arrastando)
def draw(x, y):
    t.goto(x, y)

# Move a tartaruga até o clique do mouse, sem desenhar até lá
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# ----------------------------------------
# Funções de mudança de cor
# ----------------------------------------

def setRed():
    t.color('red')

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

def setOrange():
    t.color('orange')

def setYellow():
    t.color('yellow')

def setLightBlue():
    t.color('light blue')

def setViolet():
    t.color('violet')

# ----------------------------------------
# Funções de espessura do pincel
# ----------------------------------------

def setWidth_1():
    t.width(5)

def setWidth_2():
    t.width(10)

def setWidth_3():
    t.width(18)

def setWidth_4():
    t.width(25)

def setWidth_5():
    t.width(35)

# ----------------------------------------
# Movimento com setas do teclado
# ----------------------------------------

def stepUp():
    t.goto(t.xcor(), t.ycor() + step)

def stepDown():
    t.goto(t.xcor(), t.ycor() - step)

def stepLeft():
    t.goto(t.xcor() - step, t.ycor())

def stepRight():
    t.goto(t.xcor() + step, t.ycor())

# ----------------------------------------
# Preenchimento de formas
# ----------------------------------------

def startFill():
    t.begin_fill()

def endFill():
    t.end_fill()

# ----------------------------------------
# Mudança da cor de fundo
# ----------------------------------------

def background_black():
    scr.bgcolor('black')

def background_white():
    scr.bgcolor('white')

# ----------------------------------------
# Associações de eventos
# ----------------------------------------

t.ondrag(draw)  # Desenha enquanto o usuário arrasta com o mouse

scr = t.getscreen()  # Obtém a tela principal

# Clique do mouse move a tartaruga
scr.onscreenclick(move)

# Teclas para mudar a cor
scr.onkey(setRed, 'r')
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
scr.onkey(setOrange, 'o')
scr.onkey(setYellow, 'y')
scr.onkey(setLightBlue, 'l')
scr.onkey(setViolet, 'v')

# Teclas para mudar a espessura
scr.onkey(setWidth_1, '1')
scr.onkey(setWidth_2, '2')
scr.onkey(setWidth_3, '3')
scr.onkey(setWidth_4, '4')
scr.onkey(setWidth_5, '5')

# Teclas de movimentação
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepRight, 'Right')

# Teclas para preenchimento de formas
scr.onkey(startFill, 'f')
scr.onkey(endFill, 'e')

# Teclas para alterar o fundo
scr.onkey(background_black, 'n')  # Night mode
scr.onkey(background_white, 'd')  # Day mode

# Ativa o modo de escuta para eventos de teclado
scr.listen()

# Mantém a janela aberta
scr.mainloop()
