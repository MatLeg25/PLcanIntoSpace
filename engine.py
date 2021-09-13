import copy
import random
import os
import ui
import util
import main

PLANET_ICON = u"\U0001FA90"
BORDER_ICON = '█'
WALL_ICON = u"\u2593"
QUIZ_ICON = u'\u001b[33;1m★ \u001b[0m'
MEME_ICON = '⚝'
DOOR_ICON = "@"
ENEMY_SHOTS_NUMBER = 3 #quantity of position occupied by one shot
ENEMY_SHOT_ICON = "\u001b[36;1m%\u001b[0m"
EARTH_ICON = u"\U0001F30D"
PLAYER_SHOT1_ICON = u"\u27B3" #strzala
PLAYER_SHOT2_ICON = u"\u27BC" #strzala2
ALKO_ICON = [u"\U0001F37A",	u"\U0001F377", u"\U0001F37E"] #beer,wine,vodka
ALIEN_SHIP_ICON = u"\U0001F6F8" #ufo
LVL3_ALIEN_LIFE_ICON = u"\U0001F47D " #alien
LVL3_PLAYER_LIFE_ICON = (f'\x1b[6;31;40m \u2764 \x1b[0m')


def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []

    for h in range(height):
        board.append([""]*width)

    return create_border(board, width, height)


def create_border(board, width, height):
    '''
    Creates a borders = puts BORDER_ICON on the edges of the board
    '''
    for h in range(height):
        for w in range(width):
            if (h == 0 or w == 0 or h == height-1 or w == width-1):
                board[h][w] = BORDER_ICON
    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    x = player['player_x_position']
    y = player['player_y_position']
    board[x][y] = player['icon']


def player_moves(key, board, player):
    '''
    Changing player position. 
    Obstacles - all symbols you don't wanna player to cross. 
    Returns:
    Nothing
    '''

    obstacles = ['#', BORDER_ICON, WALL_ICON]
    x = player['player_x_position']
    y = player['player_y_position']

    if key == 'a':
        if (y-1) != 0 and (board[x][y-1] not in obstacles):
            player['player_y_position'] = y - 1
    if key == 'w':
        if (x-1) != 0 and (board[x-1][y] not in obstacles):
            player['player_x_position'] = x - 1
    if key == 's':
        if (x+1) != (len(board) - 1) and (board[x+1][y] not in obstacles):
            player['player_x_position'] = x + 1
    if key == 'd':
        if (y+1) != (len(board[0]) - 1) and (board[x][y+1] not in obstacles):
            player['player_y_position'] = y + 1
    else:
        pass


def generate_game_board_1(board):
    mum_house_board = copy.deepcopy(board)

    mum_house_board[13][5] = "E"
    mum_house_board[13][6] = "X"
    mum_house_board[13][7] = "I"
    mum_house_board[13][8] = "T"
    # można dodać ikonki drzwi

    list_of_walls = {(13, 4), (12, 4), (12, 9), (13, 9), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                     (12, 5), (12, 8), (9, 13), (9, 12), (9, 11), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6)}
    for i in list_of_walls:
        mum_house_board[i[0]][i[1]] = BORDER_ICON
    #  ma nie przechodzić przez ściany

    list = set()
    while len(list) < 12:
        position_x = random.randint(2, len(board) - 2)
        position_y = random.randint(2, len(board[0]) - 2)
        if mum_house_board[position_x][position_y] == "":
            list.add((position_x, position_y))
        else:
            position_x = random.randint(2, len(board) - 2)
            position_y = random.randint(2, len(board[0]) - 2)
    flag = 0

    for i in list:
        if flag < 6:
            mum_house_board[i[0]][i[1]] = "B"
            flag += 1
        else:
            mum_house_board[i[0]][i[1]] = "P"
            flag += 1

    return mum_house_board


def generate_game_board_2(board):
    city_board = copy.deepcopy(board)
    list_of_walls = {(11, 13), (11, 12), (11, 11), (10, 11), (9, 11), (9, 12), (4, 1), (4, 2), (4, 3), (4, 4),(3,4),
                     (4, 5), (3, 5), (2, 5), (2, 4), (2, 3), (2, 2), (12, 4), (12, 3), (12, 2), (12, 1),(3,1),(3,2),(3,3),(9,12),(9,13),(13,1),(13,2),(13,3)}
    for i in list_of_walls:
        city_board[i[0]][i[1]] = BORDER_ICON

    list_of_excluded_fields = {(11, 13), (11, 12), (11, 11), (10, 11), (9, 11), (9, 12), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (3, 5), (2, 5), (
        2, 4), (2, 3), (2, 2), (12, 1), (12, 4), (12, 3), (12, 2), (13, 1), (13, 2), (13, 3), (10, 12), (10, 13), (3, 1), (3, 2), (3, 3), (3, 4), 
        (13,5), (13,6), (13,7), (13,8), (2, 1), (1, 4), (9, 13), (13, 4)}

    city_board[2][1] = DOOR_ICON
    city_board[1][4] = "F"
    city_board[9][13] = DOOR_ICON
    city_board[13][4] = DOOR_ICON

    list = set()
    while len(list) < 12:
        position_x = random.randint(2, len(board) - 2)
        position_y = random.randint(2, len(board[0]) - 2)
        is_possible = (position_x, position_y)
        for field in list_of_excluded_fields:
            if field == is_possible:
                position_x = random.randint(2, len(board) - 2)
                position_y = random.randint(2, len(board[0]) - 2)
            elif not is_possible in list_of_excluded_fields:
                list.add((position_x, position_y))

    flag = 0

    for i in list:
        if flag < 6:
            city_board[i[0]][i[1]] = "S"
            flag += 1
        else:
            city_board[i[0]][i[1]] = "Z"
            flag += 1

    return city_board


def add_to_inventory(player, board, inventory):
    x = player['player_x_position']
    y = player['player_y_position']
    if board[x][y] == "B":
        inventory["Bigos"] += 1
        board[x][y] = " "
    if board[x][y] == "P":
        inventory["Pierogi"] += 1
        board[x][y] = " "
    if board[x][y] == "Z":
        inventory["Złom"] += 1
        board[x][y] = " "
    if board[x][y] == "S":
        inventory["Sliptape"] += 1
        board[x][y] = " "



def exit_board(level, player):
    if level == 1:
        x = player['player_x_position']
        y = player['player_y_position']
        exit_list = (5, 6, 7, 8)

        if x == 13 and y in exit_list:
            return True
        else:
            return False
    if level == 2:
        x = player['player_x_position']
        y = player['player_y_position']    
        if x == 13 and y == 4:
            return True
        else:
            return False


def going_to_the_moon():
    txt=("Spotykasz typowego Sebę. Który pyta czy masz jakiś problem?\nPo krótkiej wymianie zdań, postanawia ci pomóc...")
    ui.print_text(txt,font_color=36)
    im = ui.get_ascii("./ascii_files/ziomek.txt") #import text from ASCII file
    ui.display_ascii(im,font_colors=[37],spacing=5) #displays ASCII file with color defined by number
    input()
    os.system('cls')
    txt="Ruszamy w kosmos!"
    ui.print_text(txt,font_color=36)
    im = ui.get_ascii("./ascii_files/gulf.txt") #import text from ASCII file
    ui.display_ascii(im,font_colors=[37],spacing=5) #displays ASCII file with color defined by number
    input()
    os.system('cls')
    txt=("Trzeciego dnia podróży postanawiacie wypić wódkę zabraną przez Twojego kompana i zasypiacie. Budzicie się a Waszym oczom ukazuje się wileki labirynt!")
    ui.print_text(txt,font_color=36)
    im = ui.get_ascii("./ascii_files/flaszka.txt") #import text from ASCII file
    ui.display_ascii(im,font_colors=[37],spacing=5) #displays ASCII file with color defined by number
    input()


def chceck_inventory(inventory, level):
    if level == 1:
        if inventory["Pierogi"] > 4 and inventory["Bigos"] > 4:
            return True
        else:
            return False

    if level == 2:
        control_sum = 0
        for i in inventory:
            if inventory[i] > 2:
                control_sum += 1

        if control_sum == 6:
            return True
        elif control_sum < 6:
            return False


    


def exchange_of_goods(player, inventory):
    x = player['player_x_position']
    y = player['player_y_position']
    if x == 9 and y == 13:
        im = ui.get_ascii("./ascii_files/meta.txt") #import text from ASCII file
        ui.display_ascii(im,font_colors=[37],spacing=5) #displays ASCII file with color defined by number
        txt=("Cześć, chcesz wymienić bigos i pierogi na ODLOTOWY PREPARAT?")
        ui.print_text(txt,font_color=36)
        choice = input("T / N: ")
        os.system('cls')
        if choice == "t":
            if inventory["Pierogi"] > 0 and inventory["Bigos"] > 0:
                inventory["Pierogi"] -= 1
                inventory["Bigos"] -= 1
                inventory["Ropa"] += 1
                return inventory
            if choice == "n":
                return inventory
    else:
        return inventory


def ferdek(player):
    x = player['player_x_position']
    y = player['player_y_position']
    if x == 1 and y == 4:
        txt=("Tu nie ma pracy dla ludzi z moim wykształceniem")
        ui.print_text(txt,font_color=36)
        im = ui.get_ascii("./ascii_files/ferdek.txt") #import text from ASCII file
        ui.display_ascii(im,font_colors=[37],spacing=5) #displays ASCII file with color defined by number
        input(" ")
        os.system('cls')

def get_blasters(player, inventory):
    x = player['player_x_position']
    y = player['player_y_position']
    if x == 2 and y == 1:
        txt=("Czekasz w kolejce do pokoju, po chwili słyszysz swoje nazwisko i wchodzisz do środka")
        ui.print_text(txt,font_color=36)
        input(" ")
        os.system('cls')
        im = ui.get_ascii("./ascii_files/urzednik.txt") #import text from ASCII file
        ui.display_ascii(im,font_colors=[37],spacing=5) #displays ASCII file with color defined by number
        input(" ")
        txt=("Po obszernym wywiadzie dotyczącym Twojej sytuacji zawodowej otrzymujesz zasiłek dla bezrobotnych")
        ui.print_text(txt,font_color=36)
        input(" ")
        os.system('cls')
        im = ui.get_ascii("./ascii_files/banknoty.txt") #import text from ASCII file
        ui.display_ascii(im,font_colors=[32],spacing=5) #displays ASCII file with color defined by number
        input(" ")
        os.system('cls')
        txt=("Odpalasz swojego smatrfona i kupujesz blastery do startku")
        ui.print_text(txt,font_color=36)
        input(" ")
        im = ui.get_ascii("./ascii_files/allezlo.txt") #import text from ASCII file
        ui.display_ascii(im,font_colors=[32],spacing=5) #displays ASCII file with color defined by number
        input(" ")
        os.system('cls')
        inventory["Działko"] += 1
        return inventory
    else:
        return inventory





def display_players_card(inventory):
    print("============================")
    print('{:<10}{:<10}{:<10}'.format("SYMBOL", "ITEM", "QUANTITY"))
    for key, value in inventory.items():
        item = key
        quantity = value
        symbol = item[0].upper()
        print("----------------------------")
        print('{:<10}{:<13}{:<10}'.format("  " + symbol, item, quantity))

###################################### LEVEL 2

def grid_generator(board):
    '''
    Creat grid on board
    '''
    for i in range(len(board) - 1):
        if i % 2 == 0:
            board[i] = [WALL_ICON] * len(board[0])

    for j in board:
        for n in range(len(j) - 1):
            if n % 2 == 0:
                j[n] = WALL_ICON


def surrounding_cells(cell, board):
    sur_cells = []
    x = cell[0]
    y = cell[1]

    # up
    if x - 1 != 0:
        sur_cells.append((x-1, y))
    # down
    if x + 1 != len(board) -1:
        sur_cells.append((x+1, y))
    # left
    if y - 1 != 0:
        sur_cells.append((x, y-1))
    # right
    if y + 1 != len(board[0]) -1:
        sur_cells.append((x, y+1))

    return sur_cells


def edges(board):

    edges = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if x != 0 and x != len(board) - 1 \
                    and y != 0 and y != len(board[0]) - 1:

                if x % 2 == 0 and not y % 2 == 0:
                    edges.append([x, y])
                if y % 2 == 0 and not x % 2 == 0:
                    edges.append([x, y])
    return edges


def remove_not_used_cells(cells, board):
    approved_cells = []
    for cell in cells:
        x = cell[0]
        y = cell[1]
        if board[x][y] == '':
            approved_cells.append(cell)
        else:
            pass

    return approved_cells

def maze_algorithm(cells, tree, edge, board):

    '''
    Checking if two cells have determinated origin. If not - edge is their orgin. Edge - kaboom
    '''
    if cells[0] not in tree and cells[1] not in tree:
        tree[cells[0]] = edge
        tree[cells[1]] = edge
        board[edge[0]][edge[1]] = ''

    '''
    1 cell have origin, 1 not. Origin of 1st cell = origin of cell without. Edge - kaboom
    '''
    if cells[0] in tree and cells[1] not in tree:
        tree[cells[1]] = tree[cells[0]]
        board[edge[0]][edge[1]] = ''

    if cells[1] in tree and cells[0] not in tree:
        tree[cells[0]] = tree[cells[1]]
        board[edge[0]][edge[1]] = ''

    '''
    cell1 and cell2 have origins. If it is the same origin - do nothing. Else - edge is the new origin for them 
    and cells with the same origin.
    '''

    if cells[0] in tree and cells[1] in tree:
        if tree[cells[0]] != tree[cells[1]]:
            board[edge[0]][edge[1]] = ''
            root_1 = tree[cells[0]] 
            root_2 = tree[cells[1]] 
            for key, value in tree.items():
                if value == root_1 or value == root_2:
                    tree[key] = edge
        else:
            pass

def maze_generator(board_to_maze):

    board = copy.deepcopy(board_to_maze)
    grid_generator(board) # Creates grid on board
    maze_edges = edges(board) # Returns edges between 2 blank spaces on board
    '''
    tree[node] = root
    To determinate origin of path. Root - edge that creat path.
    '''
    tree = {}
    random.shuffle(maze_edges) # To randomize order of edges
    
    for edge in maze_edges:
        
        cells = surrounding_cells(edge, board) # returns surrounding cells of edge (up, down, right, left) 
        cells = remove_not_used_cells(cells, board) # removes not blank cells (up, down) (left, right)
        maze_algorithm(cells, tree,edge,board)

    return board


def put_quizzes(board):
    quizzes = util.quiz_file_reader('quizzes.csv')
    quizzes_xy = []
    
    while len(quizzes_xy) != len(quizzes):
        x = random.randint(2,len(board) - 1)
        y = random.randint(2,len(board[0]) - 1)

        if ([x,y] not in quizzes_xy) and \
            board[x][y] == '':
            quizzes_xy.append([x,y])

    for i in quizzes_xy:
        board[i[0]][i[1]] = QUIZ_ICON

def quiz_function(board, player):
    x = player['player_x_position']
    y = player['player_y_position']
    quizzes = util.quiz_file_reader('quizzes.csv')
    if board[x][y] == QUIZ_ICON:
        quiz = random.choice(quizzes)
        quiz_read = quiz[0].split('|')
        for i in quiz_read:
            print(i)
        answer = input('Podaj odp.: ').lower
        if answer == quiz[1].lower:
            txt=('Dobra robota! Zdobywasz 5 gwiazdek!')
            ui.print_text(txt,font_color=36)
            player['player_*'] += 5
        else:
            txt=('Nie dobrze. Tracisz 30 HP')
            ui.print_text(txt,font_color=36)
            player['player_hp'] -= 30
        board[x][y] = ''
        quizzes.remove(quiz)


def put_memes(board):

    memes_xy = []
    while len(memes_xy) != 1:
        x = random.randint(2,len(board) - 1)
        y = random.randint(2,len(board[0]) - 1)

        if ([x,y] not in memes_xy) and \
            board[x][y] == '':
            memes_xy.append([x,y])

    for i in memes_xy:
        board[i[0]][i[1]] = MEME_ICON


def meme_function(board, player):
    x = player['player_x_position']
    y = player['player_y_position']
    
    if board[x][y] == MEME_ICON:
        os.system('memes\poland-cannot-into-space.jpg')
        txt=("Odnalazłeś starożytnego mema! Zdobywasz 3 gwiazdki!")
        ui.print_text(txt,font_color=36)
        player['player_*'] += 3
        board[x][y] = ''

def display_maze_status(player):
    hp = player['player_hp']
    stars = player['player_*'] * "*"
    print(f'You have {hp} HP and {stars} stars!')

def level_2_start():
    maze = ui.get_ascii("./ascii_files/maze.txt") #import text from ASCII file
    ui.display_ascii(maze,font_colors=[31],spacing=1) #displays ASCII file with color defined by number
    input()
    util.clear_screen()
    input(''' 
    "(...) wyższa cywilizacja przyjeżdża tymi UF-ami
    i innymi i przygląda się: co oni tu wyprawiają."
                                            \u001b[36;1mLech Wałęsa\u001b[0m
    ''')
    util.clear_screen()
    input("""
    Znajdź w kosmicznym labiryncie 8 gwiazdek (★ ★ ★ ★ ★   ★ ★ ★)
    i sprostaj wyzwaniom jakie stawiają obce cywilizacje!""")
    util.clear_screen()


##### LEVEL3
def display_ascii_with_move(text,counter,bg_color=6, font_colors=[30,31,32,33,34,35,36,37]):
    
    font_color = random.choice(font_colors)

    print(f'\x1b[{bg_color};{font_color};40m') #COLOR START
    #x = random.randint(1,15)
    counter=counter%10
    spacing = "\t"*counter #*x
    if counter%2==0:
        print("\n\n\n\n")
    for line in text:
        line = spacing + line
        print(line.rstrip())

    print('\x1b[0m') #COLOR END


def kometa(board,iter,HEIGHT):
    iter=(iter%(HEIGHT-1)) if iter>=HEIGHT-1 else iter
    iter=iter+1 if iter==0 else iter
    board[iter][7]=board[iter][8]=board[iter][9]="*"

def level3_shot():
    '''
    Random shot probability 
    '''
    result = random.randint(1,1)
    if result == 1:
        return True
    else:
        return False

def first_shot():
    txt=("Potrzymaj mi piwo! I patrz!!!\n")
    ui.print_text(txt,font_color=36)
    enemy= ui.get_ascii("./ascii_files/alien_sitting_to_ufo.txt")
    ui.display_ascii(enemy,font_colors=[32], spacing=7)

def get_random_position(board,number_of_positions):
 
    board_width = len(board[0])-1
    board_height = len(board)-1

    shots_list = set()
    
    #shot in random position
    while len(shots_list) < number_of_positions:
        h,w = random.randint(1,board_height-1),random.randint(1,board_width-1)
        shots_list.add((h,w))
    return shots_list

def intro_lvl3():
    txt=("W obliczu konfrontacji z obcymi, topowe ziemskie technologie zdają się być zawodne. Załoga postnawia zdobyć cel podstępem... \nProponujecie grę w alchemika: zamiana procentów na promile")
    ui.print_text(txt,font_color=33)
    input()

enemy_state=0
enemy_shots_quantity=1
player_live= [LVL3_PLAYER_LIFE_ICON,LVL3_PLAYER_LIFE_ICON,LVL3_PLAYER_LIFE_ICON,LVL3_PLAYER_LIFE_ICON,LVL3_PLAYER_LIFE_ICON]
alien_live= [LVL3_ALIEN_LIFE_ICON,LVL3_ALIEN_LIFE_ICON,LVL3_ALIEN_LIFE_ICON]
def play_level3(temporary_board,player,counter):
    global enemy_state,enemy_shots_quantity

    x = player['player_x_position']
    y = player['player_y_position']

    print("PLAYER LIFE: ","".join(player_live),"\t\t\t\t\t","ALIEN LIFE: ","".join(alien_live))

    PLAYER_SHOT_ICON= ALKO_ICON#[PLAYER_SHOT1_ICON, PLAYER_SHOT2_ICON]

    if enemy_state<1:
        temporary_board[2][10] = PLAYER_SHOT_ICON[0]
    elif enemy_state==1:
        temporary_board[1][20] = PLAYER_SHOT_ICON[1]
    elif enemy_state>1:
        temporary_board[2][3] = PLAYER_SHOT_ICON[2]

    if enemy_state<1:
        enemy= ui.get_ascii("./ascii_files/alien_standing.txt")
        ui.display_ascii(enemy,font_colors=[32], spacing=5)
    elif enemy_state==1:
        enemy= ui.get_ascii("./ascii_files/alien_in_ufo.txt")
        ui.display_ascii(enemy, spacing=(counter%10))
    elif enemy_state>1:
        enemy = ui.get_ascii("./ascii_files/enemy2.txt")
        display_ascii_with_move(enemy,counter,7,[30,31,33])

    key = util.key_pressed()
    if key == 'q':
        input("You left the game")
        return False
    else:
        player_moves(key, temporary_board, player)
    util.clear_screen()

    #generate PLAYER shot
    if temporary_board[x][y] in PLAYER_SHOT_ICON:

        shot_result = level3_shot()

        player['player_x_position'] = main.PLAYER_START_X 
        player['player_y_position'] = main.PLAYER_START_Y

        if shot_result:
            if enemy_state==0:
                enemy_shots_quantity = ENEMY_SHOTS_NUMBER
                first_shot()
            elif enemy_state==1:
                txt = "Po przejściu na wino, przeciwnik ma probnlemy z kontrolą lotu. Zwycięstwo jest blisko!"
                ui.print_text(txt,font_color=33)
            enemy_state+=1
            del alien_live[-1]

    #generate and puts on board enemy shots
    enemy_shots_position = list(get_random_position(temporary_board,enemy_shots_quantity))

    for position in enemy_shots_position:
        temporary_board[position[0]][position[1]] = ENEMY_SHOT_ICON

        if (position[0],position[1])==(x,y):
            txt=("Mały zielony kosmita wygrywa starcie. Po rozmowie z Posejdonem wracasz do walki.")
            ui.print_text(txt,font_color=33)
            input()
            player['player_x_position'] = main.PLAYER_START_X 
            player['player_y_position'] = main.PLAYER_START_Y
            del player_live[-1]
            break

    if len(alien_live)==0:
        img= ui.get_ascii("./ascii_files/koniec.txt")
        ui.display_ascii(img,font_colors=[31], spacing=0)
        input()
        return False
    elif len(player_live)==0 or counter >200:
        input("Poległeś w walce !")
        return False
    else:
        return True
    


############################END GAME
def end_game():
    txt="Obca cywilizacja jest pod wrażeniem twoich dokonań, zapraszają Cię do wspólnej podrózy w kierunku anomalii"
    ui.print_text(txt,font_color=33)
    img= ui.get_ascii("./ascii_files/alien_head.txt")
    ui.display_ascii(img,font_colors=[32], spacing=5)
    input("=>")
    os.system('memes\Twardowsky2.png')
