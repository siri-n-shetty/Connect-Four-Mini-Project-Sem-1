import turtle
import time

screen = turtle.Screen()
screen.setup(600,600)
screen.setworldcoordinates(-500,-500,500,500)
screen.title("Connect Four")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)
score = turtle.Turtle()
score.up()
score.hideturtle()

ROWS = 6
COLS = 7
STARTX = -450
STARTY = -450*ROWS/COLS
WIDTH = -2*STARTX
HEIGHT = -2*STARTY

def draw_rectangle(x,y,w,h,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

def draw_circle(x,y,r,color):
    turtle.up()
    turtle.goto(x,y-r)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r,360,150)
    turtle.end_fill()

def draw_board():
    draw_rectangle(STARTX,STARTY,WIDTH,HEIGHT,'light blue')

def draw_pieces():
    global board
    row_gap = HEIGHT/ROWS
    col_gap = WIDTH/COLS
    Y = STARTY + row_gap / 2;
    for i in range(ROWS):
        X = STARTX + col_gap/2
        for j in range(COLS):
            if board[i][j] == 0:
                draw_circle(X,Y,row_gap/3,'white')
            elif board[i][j] == 1:
                draw_circle(X,Y,row_gap/3,'black')
            else:
                draw_circle(X,Y,row_gap/3,'red')
            X += col_gap
        Y += row_gap

def draw():
    draw_board()
    draw_pieces()
    screen.update()
    
def game_over_lastmove(bb,turn,r,c):
    # check horizontals
    cnt = 1
    i = c+1
    while i<COLS and bb[r][i]==turn: cnt, i = cnt+1, i+1
    i = c-1
    while i>=0 and bb[r][i]==turn: cnt, i = cnt+1, i-1
    if cnt>=4: return turn
    
    # check vertical
    if r>=3 and bb[r-1][c]==turn and bb[r-2][c]==turn and bb[r-3][c]==turn: return turn

    # check diag 2
    cnt = 1
    i = 1
    while r+i<ROWS and c+i<COLS and bb[r+i][c+i]==turn: cnt, i = cnt+1, i+1
    i = -1
    while r+i>=0 and c+i>=0 and bb[r+i][c+i]==turn: cnt, i = cnt+1, i-1
    if cnt>=4: return turn

    # check diag 1
    cnt = 1
    i = 1
    while r+i<ROWS and c-i>=0 and bb[r+i][c-i]==turn: cnt, i = cnt+1, i+1
    i = -1
    while r+i>=0 and c-i<COLS and bb[r+i][c-i]==turn: cnt, i = cnt+1, i-1
    if cnt>=4: return turn
    
    for i in range(COLS):
        if bb[ROWS-1][i] == 0:
            return -2
    return 0

# place piece in col for turn
def place_piece(bb,turn,col):
    for i in range(ROWS):
        if bb[i][col] == 0:
            bb[i][col] = turn
            return i

def init_board():
    global board
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)
        board.append(row)
    
def place_piece_and_draw(bb,turn,col):
    row = place_piece(bb,turn,col)
    row_gap = HEIGHT/ROWS
    col_gap = WIDTH/COLS
    Y = STARTY + row_gap*row + row_gap / 2;
    X = STARTX + col_gap*col + col_gap/2
    i = row
    j = col
    if board[i][j] == 0:
        draw_circle(X,Y,row_gap/3,'white')
    elif board[i][j] == 1:
        for k in range(5):
            draw_circle(X,Y,row_gap/3,'white')
            screen.update()
            time.sleep(0.05)
            draw_circle(X,Y,row_gap/3,'black')
            screen.update()
            time.sleep(0.05)
    else:
        for k in range(5):
            draw_circle(X,Y,row_gap/3,'white')
            screen.update()
            time.sleep(0.05)
            draw_circle(X,Y,row_gap/3,'red')
            screen.update()
            time.sleep(0.05)
    return row

def play(x,y):
    global turn,working
    if working: return
    working = True
    cols = [ 900/7*i-450+900/14 for i in range(7) ]
    for i in range(len(cols)):
        if abs(x-cols[i]) < 900/14*2/3 and board[ROWS-1][i]==0:
            rn = place_piece_and_draw(board,turn,i)
            r = game_over_lastmove(board,turn,rn,i)
            if r==0:
                screen.textinput('Game over','tie')
            elif r==1:
                screen.textinput('Game Over','player 1 won')
            elif r==-1:
                screen.textinput('Game over','player 2 won')
            if r!=-2: screen.bye()
            turn = -turn
    working = False

board = []
init_board()
draw_board()
draw_pieces()
turn=1
working=False
screen.onclick(play)
screen.mainloop()
