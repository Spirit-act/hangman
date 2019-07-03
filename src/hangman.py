#!/usr/bin/env python3
# -*- coding: utf8 -*-

import art
import files
import random
import re
import os
import time

# print(drawing.POS_ONE)
# print(drawing.POS_TWO)
# print(drawing.POS_THREE)
# print(drawing.POS_FOUR)
# print(drawing.POS_FIVE)
# print(drawing.POS_SIX)
# print(drawing.POS_SEVEN)


class Hangman:
    def __init__(self):
        art.startart()
        self.word = self.getword()
        self.empty = '_'*len(self.word)
        self.drawing = 0

    def readwordlist(self):
        return files.read(os.path.dirname(os.path.realpath(__file__)) + '/words.txt')

    def getword(self):
        length = int(input('Word length: '))
        length += 1
        wordlist = self.readwordlist()
        choosenwords = []
        for word in wordlist:
            if len(word) == length:
                choosenwords.append(word.rstrip())
        return choosenwords[random.randint(0, len(choosenwords))]

    def printspaces(self, word):
        out = ''
        for i in word:
            out += '_ '
        return out.rstrip()

    def findchars(self, char):
        out = []
        p = r'(' + char.upper() + '|' + char.lower() + ')'
        for c in re.finditer(p, self.word):
            out.append(c.start())
        return out

    def printnewlines(self, chars, char):
        e = list(self.empty)
        for ci in chars:
            e[ci] = char
        self.empty = "".join(e)
        print(self.empty)

    def issolved(self):
        s = self.empty
        if len(s.replace('_', '')) == len(self.empty):
            return True
        return False

    def close(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        exit()

    def run(self):
        #print(self.word)
        self.printspaces(self.word)
        while True:
            char = input('Enter your first Query: ')
            if len(char) > 1 or len(char) == 0:
                if char == '/exit':
                    self.close()
                continue
            x = self.findchars(char)
            if len(x) == 0:
                if self.drawing == 0:
                    print(art.POS_ONE)
                elif self.drawing == 1:
                    print(art.POS_TWO)
                elif self.drawing == 2:
                    print(art.POS_THREE)
                elif self.drawing == 3:
                    print(art.POS_FOUR)
                elif self.drawing == 4:
                    print(art.POS_FIVE)
                elif self.drawing == 5:
                    print(art.POS_SIX)
                elif self.drawing == 6:
                    print(art.POS_SEVEN)
                else:
                    print('The man is dead. But the word was: ' + self.word)
                    time.sleep(3)
                    self.close()
                self.drawing += 1
            self.printnewlines(x, char)
            if self.issolved():
                time.sleep(3)
                self.close()


def main():
    hangman = Hangman()
    hangman.run()


if __name__ == '__main__':
    main()
