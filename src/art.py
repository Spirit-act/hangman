import os


def startart():
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    half = ((columns - 18) / 2)
    print('=' * int(half) + ' Terminal Hangman ' + '=' * int(half))
    print('# You can Play against the Maschine')
    print('=' * columns)


POS_ONE = """  
+-------+
    |   |
        |
        |
        |
        |
========="""

POS_TWO = """
+-------+
    |   |
    o   |
        |
        |
        |
=========
"""

POS_THREE = """
+-------+
    |   |
    o   |
    |   |
        |
        |
=========
"""

POS_FOUR = """
+-------+
    |   |
    o   |
   /|   |
        |
        |
=========
"""

POS_FIVE = """
+-------+
    |   |
    o   |
   /|\  |
        |
        |
=========
"""

POS_SIX = """
+-------+
    |   |
    o   |
   /|\  |
   /    |
        |
=========
"""

POS_SEVEN = """
+-------+
    |   |
    o   |
   /|\  |
   / \  |
        |
=========
"""