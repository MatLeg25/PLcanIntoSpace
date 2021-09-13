import util
import engine
import os
import ui
from copy import deepcopy

PLAYER_ICON = u'\u001b[31m◓ \u001b[0m'
PLAYER_START_X = 1
PLAYER_START_Y = 1

BOARD_WIDTH = 15
BOARD_HEIGHT = 15

BOARD_WIDTH_lvl3 = 50
BOARD_HEIGHT_lvl3 = 4


# wywoływanie funkcji

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {'icon': PLAYER_ICON, 
    'player_x_position': PLAYER_START_X,
    'player_y_position': PLAYER_START_Y,
    'player_hp': 100,
    'player_vision': 4,
    'player_*': 0}

    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    level = 1

    inventory = {"Pierogi": 5, "Bigos": 5, "Złom": 5,
                 "Sliptape": 5, "Ropa": 5, "Działko": 5}

    if level == 1:
        # import text from ASCII file
        title = ui.get_ascii("./ascii_files/poland_can_into_space.txt")
        # displays ASCII file with color defined by number
        ui.display_ascii(title, font_colors=[34], spacing=5)
        input(" ")
        os.system('cls')
        print("\n\n")
        txt="Rok 2030. Trwa wyścig światowych mocarstw o każdy kawłek lądu. Pewnej nocy na niebie pojawia się tajemnicza anomalia... "
        ui.print_text(txt,font_color=33)

        # import text from ASCII file
        anomaly = ui.get_ascii("./ascii_files/saturn.txt")
        # displays ASCII file with color defined by number
        ui.display_ascii(anomaly, font_colors=[35], spacing=5)
        input(" ")
        os.system('cls')
        # import text from ASCII file
        im = ui.get_ascii("./ascii_files/roz1.txt")
        # displays ASCII file with color defined by number
        ui.display_ascii(im, font_colors=[31], spacing=1)
        input(" ")
        os.system('cls')
        txt=('''
        
        Po Twojej głowie wędruje wyłącznie jedna myśl. To jest mój czas. Muszę polecieć i zbadać tajemniczą anomalię. 
        Postanawiasz przerobić swojego Golfa 1.9 TDI pieszczotliwie nazywanego Gulfem na statek kosmiczny i niezwłocznie wyruszyć w drogę.''')
        ui.print_text(txt,font_color=33)
        input(" ")
        os.system('cls')

        mum_house = engine.generate_game_board_1(board)

        is_running = True
        while is_running:
            x = player['player_x_position']
            y = player['player_y_position']
            engine.add_to_inventory(player, mum_house, inventory)
            temporary_board = deepcopy(mum_house)
            engine.put_player_on_board(temporary_board, player)
            ui.display_board(temporary_board)
            engine.display_players_card(inventory)
            # print(f"Player position: ({x},{y})")
            key = util.key_pressed()
            if key == 'q':
                is_running = False
            else:
                engine.player_moves(key, mum_house, player)
            util.clear_screen()
            pass_condition = engine.chceck_inventory(inventory, level)
            if engine.exit_board(level, player) == True:
                if pass_condition == True:
                    is_running = False
                    level = 2

            else:
                is_running = True

    if level == 2:
        txt=('''Wyszedłeś na miasto. Uzupełnij zasoby, zdobądź paliwo, osłony i działa do statku.''')
        ui.print_text(txt,font_color=33)
        input(" ")
        os.system('cls')
        city = engine.generate_game_board_2(board)
        is_running = True
        while is_running:
            x = player['player_x_position']
            y = player['player_y_position']
            engine.add_to_inventory(player, city, inventory)
            temporary_board = deepcopy(city)
            engine.put_player_on_board(temporary_board, player)
            ui.display_board(temporary_board)
            engine.display_players_card(inventory)
            # print(f"Player position: ({x},{y})")
            key = util.key_pressed()
            if key == 'q':
                is_running = False
            else:
                engine.player_moves(key, city, player)
            util.clear_screen()
            inventory = engine.exchange_of_goods(player, inventory)
            engine.ferdek(player)
            inventory = engine.get_blasters(player, inventory)
            pass_condition = engine.chceck_inventory(inventory, level)
            if engine.exit_board(level, player) == True:
                if pass_condition == True:
                    engine.going_to_the_moon()
                    level = 3
                    is_running = False
            elif engine.exit_board(level, player) == False:
                is_running = True

    if level == 3:
        player['player_x_position'] = PLAYER_START_X
        player['player_y_position'] = PLAYER_START_Y
        board = engine.create_board(21, 15)
        util.clear_screen()
        board_level_2 = engine.maze_generator(board)
        engine.put_quizzes(board_level_2)
        engine.put_memes(board_level_2)
        is_running = True
        level_2 = True
        while is_running:
            engine.level_2_start()
            while level_2:
                engine.quiz_function(board_level_2, player)
                engine.meme_function(board_level_2, player)
                temporary_board = deepcopy(board_level_2)
                engine.put_player_on_board(temporary_board, player)
                engine.display_maze_status(player)
                ui.display_maze(temporary_board, player)

                key = util.key_pressed()

                if key == 'q':
                    is_running = False
                else:
                    engine.player_moves(key, temporary_board, player)
                util.clear_screen()
                level_4 = player['player_*']
                if  level_4 > 7:
                    level = 4
                    is_running = False
                    level_2 = False
    if level == 4:
        txt=("Po latach podrózy i licznych przeszkodach na horyzoncie ukazuje się anomalia. Aby do niej dotrzeć musisz zmierzyć się z obcymi...")
        ui.print_text(txt,font_color=33)
        input()
        os.system("cls||clear")
        level_3=True
        player['player_x_position'] = PLAYER_START_X
        player['player_y_position'] = PLAYER_START_Y    

        board_level_3 = engine.create_board(BOARD_WIDTH_lvl3,BOARD_HEIGHT_lvl3)
        im = ui.get_ascii("./ascii_files/battle.txt") #import text from ASCII file
        ui.display_ascii(im,font_colors=[31],spacing=1) #displays ASCII file with color defined by number
        input()
        os.system('cls')
        counter=0
        engine.intro_lvl3()
        while level_3:
            counter+=1
        
            temporary_board = deepcopy(board_level_3)
            engine.put_player_on_board(temporary_board, player)
            level_3 = engine.play_level3(temporary_board,player,counter)
            if level_3:
                ui.display_board(temporary_board)

        is_running = False
        util.clear_screen()
        level =5

    if level ==5:
        engine.end_game()


if __name__ == '__main__':
    main()
