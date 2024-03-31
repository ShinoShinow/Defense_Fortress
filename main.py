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
shoot_lines = []
shoot_cols = []
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
    global enemy_cols , enemy_lines , game_left , game_right
    if random() > 0.95 :
        enemy_cols.append(randint(game_left+2,game_right-2))
        enemy_lines.append(0)

def enemy_draw() :
    global enemy_cols , enemy_lines
    for i in range(len(enemy_cols)) :
        stdscr.addch(enemy_lines[i],enemy_cols[i],'E')
    stdscr.refresh()

def enemy_move() : 
    global enemy_cols , enemy_lines , rand
    if random() > 0.96 :
        for item in range(len(enemy_cols)) :
            stdscr.addch(enemy_lines[item],enemy_cols[item],' ')
            enemy_lines[item] += 1
            stdscr.addch(enemy_lines[item],enemy_cols[item],'E')
        stdscr.refresh()        

def shoot() :
    global shoot_lines, shoot_cols
    shoot_lines.append(Player_line-1)
    shoot_cols.append(Player_cols)
    stdscr.addch(Player_line-1,Player_cols,'*')
    stdscr.refresh()

def shoot_move() :
    for i in range(0,len(shoot_lines)) :
        stdscr.addch(shoot_lines[i],shoot_cols[i],' ')
        shoot_lines[i] -= 1
        stdscr.addch(shoot_lines[i],shoot_cols[i],'*')
    stdscr.refresh()

def shoot_aim() :
    global shoot_lines , shoot_cols
    try :
        for i in shoot_lines :
            if shoot_lines[i] == 0 :
                stdscr.addch(shoot_lines[i],shoot_cols[i],' ')
                stdscr.refresh()
                del shoot_lines[i]
                del shoot_cols[i]
    except:
        pass

def enemy_check() :
    global shoot_lines , shoot_cols , enemy_lines , enemy_cols , game
    Iout = 99999
    Jout = 99999
    for i in range(0,len(shoot_lines)) :
        for j in range(0,len(enemy_lines)) :
            if shoot_lines[i] == enemy_lines[j] and shoot_cols[i] == enemy_cols[j] :
                stdscr.addch(shoot_lines[i],shoot_cols[i],' ')
                stdscr.addch(enemy_lines[j],enemy_cols[j],' ')
                stdscr.refresh()
                Iout = i
                Jout = j
    if Iout != 99999 :
        del shoot_lines[Iout]
        del shoot_cols[Iout]
        del enemy_lines[Jout]
        del enemy_cols[Jout]

def checkdie() :
    global game
    for i in range(0,len(enemy_lines)) :
        if enemy_lines[i] == max_line-1 :
            game = False
            stdscr.addstr(max_line//2,max_cols//2,"YOU LOSE!!")
            stdscr.refresh()
            sleep(2)
            stdscr.clear()
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
        ch = ''
    if ch == 'q' :
        game = False
        stdscr.clear()
        stdscr.refresh()
        sleep(1)
    if ch == ' ' :
        shoot()
    if ch in 'ad':
        move(ch)
    Player()
    draw()
    enemy_init()
    enemy_draw()
    enemy_move()
    enemy_check()
    shoot_move()
    shoot_aim()
    Fortress()
    checkdie()