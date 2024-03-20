from random import randint
import curses
from time import sleep

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
curses.curs_set(False)
stdscr.clear()
max_line = curses.LINES - 1
max_cols = curses.COLS - 1
Player_line = 0
Player_cols = 0
world = []

def init() :
    global world
    for i in range(0,max_line) :
        world.append([])
        for j in range(0,max_cols) :
            world[i].append('+')


def draw() :
    global game_right ,game_left
    for i in range(0,max_line) :
        for j in range(0,max_cols) :
            stdscr.addch(i,j//4,world[i][j//4])
            game_right = 1000
            for r in range(int(max_cols*0.75),max_cols) :
                game_left = (max_cols//4) +1
                if r < game_right :
                    game_right = r
                stdscr.addch(i,r,world[i][r])
    stdscr.refresh()

def Fortress() :
    global game_right ,game_left
    for F in range(game_left,game_right) :
        stdscr.addch(max_line-1,F,"#")
    for end in range(game_right,max_cols) :
        stdscr.addch(max_line-1,end,"+")
    stdscr.refresh()

def Player() :
    global Player_line , Player_cols
    stdscr.addch(Player_line,Player_cols,'^')
    stdscr.refresh()

def move(ch) :
    global Player_cols , Player_line, game_right , game_left
    stdscr.addch(Player_line,Player_cols,' ')
    if ch == 'a' and  Player_cols > game_left:
        Player_cols = Player_cols - 1
    if ch == 'd' and  Player_cols < game_right -1 :
        Player_cols = Player_cols + 1


game = True
init()
Player_line = max_line-2
Player_cols = max_cols//2
while game :
    Player()
    draw()
    Fortress()
    try  :
        ch = stdscr.getkey()
    except :
        ch = ' '
    if ch == 'q' :
        game = False
        sleep(1)
        stdscr.clear()
        stdscr.refresh()
    if ch in 'ad':
        move(ch)
