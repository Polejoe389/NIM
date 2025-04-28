"""
NIM NIM NIM
"""
import random

MAX_LINE = " 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"


def start():
    """
    Starting point for the game of NIM
    :return:
    """
    show_menu()
    choice = input("PLEASE ENTER 1 or 2:")
    if choice == "1":
        play_one_game()



def show_menu():
    """
    Show main menu to the user
    :return:
    """
    pass


def play_one_game():
    """
    Play a single game of NIM
    :return:
    """
    pass


def get_user_move(player_number):
    """
    Get a list object representing the user move
    :param player_number:
    :return:
    """
    pass


def change_line(line, number_to_remove):
    """
    Remove the correct number from the line
    :param line:
    :param number_to_remove:
    :return:
    """
    pass


def check_game_finished(game_lines):
    """
    Check if the game has finished
    :param game_lines:
    :return:
    """
    pass


def get_next_player_number(player_number):
    """
    Get the number of the next player
    :param player_number:
    :return:
    """
    pass


def set_up_game_line():
    """
    Set up a single line of nim
    :return:
    """
    pass


def display_lines(game_lines):
    """
    Display the three lines
    :param game_lines:
    :return:
    """
    pass


def congratulate_player(player_number):
    """
    Display a congratulatory message
    :param player_number:
    :return:
    """
    pass


if __name__ == "__main__":
    # Start playing NIM NIM NIM!
    start()
