"""
 Place this file in the same folder as NIM.py

 Before you run this test code you MUST check that:
 - Your NIM code file is named as "NIM.py" (exactly the same)
 - Your NIM.py file is in the same directory(folder) as this file
 - the call to start() is in the  if __name__ == "__main__": control structure
   or has been commented out, i.e. #start()
 to ensure that this test code file controls the order functions are run

# import code in file from NIM (NIM.py)
>>> from NIM import *
>>> import random
>>> random.seed(1)

# Should show the menu, not ask for input
>>> show_menu()
======================
G A M E   O F   N I M
======================
PLEASE CHOOSE FROM:
<BLANKLINE>
1. PLAY NIM NIM NIM
2. EXIT
======================


## Test set_up_game_line function
# Should show three lines with random amounts of 0's on each line
>>> print(set_up_game_line())
 0 0 0
>>> print(set_up_game_line())
 0 0 0 0 0 0 0 0 0 0
>>> print(set_up_game_line())
 0 0 0 0 0 0 0 0 0 0 0 0 0 0

## Test display_lines
# Should display the lines neatly formatted with
# 1: 2: and 3: at the start of each line
>>> lines = [" 0", " 0 0", " 0 0 0 0 0 0 0"]
>>> display_lines(lines)
1 :   0
2 :   0 0
3 :   0 0 0 0 0 0 0

>>> print(change_line(" 0 0 0", 2))
 0
>>> print(change_line(" 0 0 0 0 0", 6))
<BLANKLINE>
>>> print(change_line(" 0 0 0 0 0 0 0", 2))
 0 0 0 0 0

>>> print(check_game_finished(lines))
False

>>> lines = ["", "", " 0"]
>>> print(check_game_finished(lines))
False
>>> lines[2] = ""
>>> print(check_game_finished(lines))
True

>>> print(get_next_player_number(1))
2
>>> print(get_next_player_number(2))
1

>>> congratulate_player(1)
<BLANKLINE>
** Y O U   H A V E   W O N **
    PLAYER NUMBER:  1
**   W E L L   D O N E !   **

>>> congratulate_player(2)
<BLANKLINE>
** Y O U   H A V E   W O N **
    PLAYER NUMBER:  2
**   W E L L   D O N E !   **


"""
import doctest
doctest.testmod()
