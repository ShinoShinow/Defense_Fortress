from random import randint , random
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
enemy_cols = []
enemy_lines = []
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
    
def enemy_init() :
    global enemy_cols , enemy_lines , game_left , game_right , rand
    rand = random()
    if random() > 0.95 :
        enemy_cols.append(randint(game_left,game_right))
        enemy_lines.append(0)

def enemy_draw() :
    global enemy_cols , enemy_lines , rand
    if rand > 0.95 :
        for i in range(len(enemy_cols)) :
            stdscr.addch(enemy_lines[i],enemy_cols[i],'E')
        stdscr.refresh()

def enemy_move() : 
    global enemy_cols , enemy_lines , rand
    if random() > 0.95 :
        for item in range(len(enemy_cols)) :
            stdscr.addch(enemy_lines[item],enemy_cols[item],' ')
            enemy_lines[item] += 1
            stdscr.addch(enemy_lines[item],enemy_cols[item],'E')
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
    try  :
        ch = stdscr.getkey()
    except :
        ch = ' '
    if ch == 'q' :
        game = False
        stdscr.clear()
        stdscr.refresh()
        sleep(1)
    if ch in 'ad':
        move(ch)
    Player()
    draw()
    enemy_init()
    enemy_draw()
    enemy_move()
    Fortress()

