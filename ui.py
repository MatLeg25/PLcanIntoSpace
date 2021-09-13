def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for i in board:
        row = ''
        bar = ''
        for j in i:
            row += f'{j:^2}'
        row += ''
        for x in range(len(row)):
            bar += ''
        print(bar)
        print(row)
    print(bar)

import random

def get_ascii(filename):
    '''
    From ASCII art txt file, return string text
    '''
    try:
      with open(filename,"r", encoding="utf8") as file:
          return file.readlines()
    except FileNotFoundError as file_error:
      print(file_error)

def display_ascii(text,font_colors=[30,31,32,33,34,35,36,37],spacing=0):
    ''' 
    Displays ASCII from txt files with defined color. If the color is nott defined - choose a random color.
    COLORS:  30-black,31-red,32-green,33-yellow,34-blue,35-pink,36-light blue,37-white
    '''
    font_color = random.choice(font_colors) #selects a color from the list, if color not defined - takes a random color
    spacing = "\t"*spacing
    print(f'\x1b[6;{font_color};40m') #COLOR START
    for line in text:
        line=spacing+line
        print(line.rstrip()) #printing line by line, without white spaces at the end of the string
    print('\x1b[0m') #COLOR END

def display_maze(board, player):

    x = player['player_x_position']
    y = player['player_y_position']
    vision = player['player_vision']
    bar = ''
    vision_list = []
    blocked_vision = '✹'
    for i in range(x - vision, x + vision + 1):
        for j in range(y-vision,y+vision +1):
            vision_list.append([i,j])
            
    for x in range(63):
        bar += ''
    for i in range(len(board)):
        row = ''
        for j in range(len(board[0])):
            current_cell = board[i][j]
            if [i,j] in vision_list:
                current_cell = board[i][j]
            else:
                current_cell = blocked_vision
            row += f'{current_cell:^2}'
            row += ''
        print(bar)
        print(row)
    print(bar)

def print_text(text,font_color=37,spacing=0):
    ''' 
    Displays ASCII from txt files with defined color. If the color is nott defined - choose a random color.
    COLORS:  30-black,31-red,32-green,33-yellow,34-blue,35-pink,36-light blue,37-white
    '''
    spacing = "\t"*spacing
    print(f'\x1b[6;{font_color};40m') #COLOR START
    text=spacing + text
    print(text)
    print('\x1b[0m') #COLOR END

