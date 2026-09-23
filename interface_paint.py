# interface_paint.py

from turtle import *

# === Funções auxiliares para desenhar elementos da interface ===

# Desenha um quadrado preenchido com a cor fornecida
def draw_square(color):
    ti.pendown()
    ti.color('gray', color)  # Borda cinza, preenchimento colorido
    ti.begin_fill()
    for i in range(4):
        ti.forward(40)
        ti.left(90)
    ti.end_fill()
    ti.penup()

# Escreve um símbolo abaixo do quadrado, centralizado (para as letras da paleta)
def draw_symbol_below(symbol):
    x, y = ti.pos()
    ti.goto(x + 20, y - 20)  # Centro inferior do quadrado (40x40)
    ti.pendown()
    ti.color('gray')
    ti.write(symbol, align="center", font=('Arial', 12, 'normal'))
    ti.penup()

# Escreve um texto ao lado com deslocamento horizontal (para círculos e rótulos)
def draw_symbol_side(symbol, indent):
    ti.forward(indent)
    ti.pendown()
    ti.color('gray')
    ti.write(symbol, font=('Arial', 12, 'normal'))
    ti.penup()

# Desenha um círculo preenchido, usado para representar a espessura do pincel
def circle_t(size):
    ti.pendown()
    ti.begin_fill()
    ti.color('gray')  # Cor do contorno e preenchimento
    ti.circle(size)
    ti.end_fill()
    ti.penup()

# === Inicialização da tartaruga para desenhar a interface ===

ti = Turtle()
ti.penup()
ti.speed(0)  # Velocidade máxima (instantâneo)

# === Título na parte superior ===

ti.goto(-250, 270)
draw_symbol_side('PAINT TOOL - Use keyboard to control', 5)

# === Paleta de Cores (Topo da tela) ===

# Lista com (cor, tecla de atalho, posição X na tela)
colors = [
    ('red', 'R', -300),
    ('orange', 'O', -230),
    ('yellow', 'Y', -160),
    ('green', 'G', -90),
    ('light blue', 'L', -20),
    ('blue', 'B', 50),
    ('violet', 'V', 120),
]

y = 230  # Coordenada Y fixa para todos os quadrados de cor

for color, key, x in colors:
    ti.goto(x, y)           # Move para a posição do quadrado
    draw_square(color)      # Desenha quadrado de cor
    draw_symbol_below(key)  # Escreve a letra de atalho abaixo, centralizada

# === Espessuras do pincel (Lado direito da tela) ===

x = 350  # Posição X fixa para círculos
y_positions = [200, 140, 70, 0, -80]  # Posições Y para os círculos
sizes = [5, 10, 15, 20, 25]           # Tamanhos dos círculos
labels = ['1', '2', '3', '4', '5']    # Teclas de atalho
indent = 30

for y, size, label in zip(y_positions, sizes, labels):
    ti.goto(x, y)
    circle_t(size)                # Desenha o círculo com o tamanho adequado
    draw_symbol_side(label, indent)  # Escreve o número de atalho ao lado

# === Fundo (Canto inferior esquerdo da tela) ===

# Título
ti.goto(-350, -220)
draw_symbol_side('Background:', 5)

# Opção de fundo preto (tecla N)
ti.goto(-350, -280)
draw_square('black')
draw_symbol_side('N', -20)

# Opção de fundo branco (tecla D)
ti.goto(-350, -330)
draw_square('white')
draw_symbol_side('D', -20)

# === Ajuste do tamanho da tela ===

# Aumenta a janela do turtle para dar mais espaço ao usuário para desenhar
screen = Screen()
screen.setup(width=1000, height=800)     # Tamanho visível da janela (em pixels)
screen.screensize(900, 700)              # Tamanho lógico da área de desenho (em unidades turtle)

# Esconde a tartaruga da interface após terminar
ti.ht()
