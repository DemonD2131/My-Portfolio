
import pygame
#Edit May 11, 2023: I didn't document when I made this very well. But I made this from scratch, its chess, it doesn't have all the rules implemented but its mostly functioning. Its very scuffed but I'm still really proud of it.

BROOK = 1
BKNIGHT = 2
BBISHOP = 3
BQUEEN = 4
BKING = 5
BPAWN = 6
WROOK = 7
WKNIGHT = 8
WBISHOP = 9
WQUEEN = 10
WKING = 11
WPAWN = 12

white = [7, 8, 9, 10, 11, 12]
black = [1,2,3,4,5,6]

class Pieces:
    x = 0
    y = 0
    possibleMoves = []
    def __init__(self, x, y, type, board): 
        self.x = x #0
        self.y = y #6
        self.board = board 
        self.type = type #12
    def move_getter(self):
        self.possibleMoves = []
        for i in range(Chess.height): #0-7
            for j in range(Chess.width): #0-7
                if self.type == BROOK:
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y + i < 8:
                            if self.board[self.y + i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y + i))
                            elif self.board[self.y + i][self.x] in white:
                                self.possibleMoves.append((self.x, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x] not in white and self.board[self.y + i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#up
                        i += 1
                        if self.y - i > -1:
                            if self.board[self.y - i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y - i))
                            elif self.board[self.y - i][self.x] in white:
                                self.possibleMoves.append((self.x, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x] not in white and self.board[self.y - i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x - i > -1:
                            if self.board[self.y][self.x -i] == 0:
                                self.possibleMoves.append((self.x - i, self.y))
                            elif self.board[self.y][self.x -i] in white:
                                self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x -i] not in white and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#Right
                        i += 1
                        if self.x + i < 8:
                            if self.board[self.y][self.x +i] == 0:
                                self.possibleMoves.append((self.x + i, self.y))
                            elif self.board[self.y][self.x +i] in white:
                                self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x +i] not in white and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == BKNIGHT:
                    if self.y + 2 < 8 and self.x + 1 < 8 : #downright
                        if self.board[self.y + 2][self.x +1] in white or self.board[self.y +2][self.x +1] == 0:
                            self.possibleMoves.append((self.x + 1, self.y + 2))
                    
                    if self.y - 2 > -1 and self.x + 1 < 8 : #up right
                        if self.board[self.y - 2][self.x +1] in white or self.board[self.y - 2][self.x +1] == 0:
                            self.possibleMoves.append((self.x + 1, self.y - 2))
                    
                    if self.y + 2 < 8 and self.x - 1 > -1 :
                        if self.board[self.y + 2][self.x -1] in white or self.board[self.y +2][self.x -1] == 0:
                            self.possibleMoves.append((self.x - 1, self.y + 2))
                    
                    if self.y - 2 > -1 and self.x - 1 > -1 :
                        if self.board[self.y - 2][self.x -1] in white or self.board[self.y - 2][self.x -1] == 0:
                            self.possibleMoves.append((self.x - 1, self.y - 2))
                    
                    if self.y + 1 < 8 and self.x - 2 > -1 :
                        if self.board[self.y + 1][self.x -2] in white or self.board[self.y +1][self.x -2] == 0:
                            self.possibleMoves.append((self.x - 2, self.y + 1))
                    
                    if self.y - 1 > -1 and self.x - 2 > -1 :
                        if self.board[self.y - 1][self.x -2] in white or self.board[self.y - 1][self.x -2] == 0:
                            self.possibleMoves.append((self.x - 2, self.y - 1))
                    
                    if self.y + 1 < 8 and self.x + 2 < 8 :
                        if self.board[self.y + 1][self.x +2] in white or self.board[self.y +1][self.x +2] == 0:
                            self.possibleMoves.append((self.x +2, self.y + 1))
                    
                    if self.y - 1 > -1 and self.x + 2 < 8 :
                        if self.board[self.y - 1][self.x +2] in white or self.board[self.y -1][self.x +2] == 0:
                            self.possibleMoves.append((self.x +2, self.y - 1))
                elif self.type == BBISHOP:
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y + i < 8 and self.x +i < 8:
                            if self.board[self.y + i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y + i))
                            elif self.board[self.y + i][self.x +i] in white:
                                self.possibleMoves.append((self.x +i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x +i] not in white and self.board[self.y + i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down left
                        i += 1
                        if self.y + i < 8 and self.x -i > -1:
                            if self.board[self.y + i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y + i))
                            elif self.board[self.y + i][self.x -i] in white:
                                self.possibleMoves.append((self.x -i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x -i] not in white and self.board[self.y + i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up left
                        i += 1
                        if self.y - i > -1 and self.x -i > -1:
                            if self.board[self.y - i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y - i))
                            elif self.board[self.y - i][self.x -i] in white:
                                self.possibleMoves.append((self.x -i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x -i] not in white and self.board[self.y - i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up Right
                        i += 1
                        if self.y - i > -1 and self.x +i < 8:
                            if self.board[self.y - i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y - i))
                            elif self.board[self.y - i][self.x +i] in white:
                                self.possibleMoves.append((self.x +i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x +i] not in white and self.board[self.y - i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == BQUEEN:
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y + i < 8:
                            if self.board[self.y + i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y + i))
                            elif self.board[self.y + i][self.x] in white:
                                self.possibleMoves.append((self.x, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x] not in white and self.board[self.y + i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#up
                        i += 1
                        if self.y - i > -1:
                            if self.board[self.y - i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y - i))
                            elif self.board[self.y - i][self.x] in white:
                                self.possibleMoves.append((self.x, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x] not in white and self.board[self.y - i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x - i > -1:
                            if self.board[self.y][self.x -i] == 0:
                                self.possibleMoves.append((self.x - i, self.y))
                            elif self.board[self.y][self.x -i] in white:
                                self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x -i] not in white and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#Right
                        i += 1
                        if self.x + i < 8:
                            if self.board[self.y][self.x +i] == 0:
                                self.possibleMoves.append((self.x + i, self.y))
                            elif self.board[self.y][self.x +i] in white:
                                self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x +i] not in white and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y + i < 8 and self.x +i < 8:
                            if self.board[self.y + i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y + i))
                            elif self.board[self.y + i][self.x +i] in white:
                                self.possibleMoves.append((self.x +i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x +i] not in white and self.board[self.y + i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down left
                        i += 1
                        if self.y + i < 8 and self.x -i > -1:
                            if self.board[self.y + i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y + i))
                            elif self.board[self.y + i][self.x -i] in white:
                                self.possibleMoves.append((self.x -i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x -i] not in white and self.board[self.y + i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up left
                        i += 1
                        if self.y - i > -1 and self.x -i > -1:
                            if self.board[self.y - i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y - i))
                            elif self.board[self.y - i][self.x -i] in white:
                                self.possibleMoves.append((self.x -i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x -i] not in white and self.board[self.y - i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up Right
                        i += 1
                        if self.y - i > -1 and self.x +i < 8:
                            if self.board[self.y - i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y - i))
                            elif self.board[self.y - i][self.x +i] in white:
                                self.possibleMoves.append((self.x +i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x +i] not in white and self.board[self.y - i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == BKING:
                    if self.y + 1 < 8: # down
                        if self.board[self.y + 1][self.x] == 0 or self.board[self.y + 1][self.x] in white:
                            self.possibleMoves.append((self.x, self.y + 1))
                    
                    if self.y - 1 > -1: # up
                        if self.board[self.y - 1][self.x] == 0 or self.board[self.y - 1][self.x] in white:
                            self.possibleMoves.append((self.x, self.y - 1))

                    if self.x -1 > -1: # left
                        if self.board[self.y][self.x-1] == 0 or self.board[self.y][self.x-1] in white:
                            self.possibleMoves.append((self.x-1, self.y))
                    
                    if self.x+1 > -1: # RIGHT
                        if self.board[self.y][self.x+1] == 0 or self.board[self.y][self.x+1] in white:
                            self.possibleMoves.append((self.x+1, self.y))

                    if self.x-1 > -1 and self.y -1 > -1: # up left
                        if self.board[self.y - 1][self.x-1] == 0 or self.board[self.y - 1][self.x-1] in white:
                            self.possibleMoves.append((self.x-1, self.y - 1))

                    if self.x-1 > -1 and self.y +1 < 8: # down left
                        if self.board[self.y + 1][self.x-1] == 0 or self.board[self.y + 1][self.x-1] in white:
                            self.possibleMoves.append((self.x-1, self.y + 1))
                    
                    if self.x+1 < 8 and self.y -1 > -1: # up right
                        if self.board[self.y - 1][self.x+1] == 0 or self.board[self.y - 1][self.x+1] in white:
                            self.possibleMoves.append((self.x+1, self.y - 1))

                    if self.x+1 < 8 and self.y +1 < 8: # down right
                        if self.board[self.y + 1][self.x+1] == 0 or self.board[self.y + 1][self.x+1] in white:
                            self.possibleMoves.append((self.x+1, self.y + 1)) 
                elif self.type == BPAWN:
                    if self.y + 1 < 8 and self.board[self.y + 1][self.x] == 0:
                        self.possibleMoves.append((self.x, self.y + 1))
                    if self.y +2 < 8 and self.board[self.y +2][self.x] == 0 and self.y == 1:
                       self.possibleMoves.append((self.x, self.y + 2))
                    if self.y +1 < 8 and self.x + 1 < 8:
                        if self.board[self.y +1][self.x + 1] in white:
                            self.possibleMoves.append((self.x + 1, self.y +1))
                    if self.y +1 < 8 and self.x - 1 > -1:
                        if self.board[self.y +1][self.x - 1] in white:
                            self.possibleMoves.append((self.x - 1, self.y +1))
                elif self.type == WROOK:
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y + i < 8:
                            if self.board[self.y + i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y + i))
                            elif self.board[self.y + i][self.x] in black:
                                self.possibleMoves.append((self.x, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x] not in black and self.board[self.y + i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#up
                        i += 1
                        if self.y - i > -1:
                            if self.board[self.y - i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y - i))
                            elif self.board[self.y - i][self.x] in black:
                                self.possibleMoves.append((self.x, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x] not in black and self.board[self.y - i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x - i > -1:
                            if self.board[self.y][self.x -i] == 0:
                                self.possibleMoves.append((self.x - i, self.y))
                            elif self.board[self.y][self.x -i] in black:
                                self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x -i] not in black and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#Right
                        i += 1
                        if self.x + i < 8:
                            if self.board[self.y][self.x +i] == 0:
                                self.possibleMoves.append((self.x + i, self.y))
                            elif self.board[self.y][self.x +i] in black:
                                self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x +i] not in black and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == WKNIGHT:
                    if self.y + 2 < 8 and self.x + 1 < 8 :
                        if self.board[self.y + 2][self.x +1] in black or self.board[self.y +2][self.x +1] == 0:
                            self.possibleMoves.append((self.x + 1, self.y + 2))
                    if self.y - 2 > -1 and self.x + 1 < 8 :
                        if self.board[self.y - 2][self.x +1] in black or self.board[self.y - 2][self.x +1] == 0:
                            self.possibleMoves.append((self.x + 1, self.y - 2))
                    
                    if self.y + 2 < 8 and self.x - 1 > -1 :
                        if self.board[self.y + 2][self.x -1] in black or self.board[self.y +2][self.x -1] == 0:
                            self.possibleMoves.append((self.x - 1, self.y + 2))
                    if self.y - 2 > -1 and self.x - 1 > -1 :
                        if self.board[self.y - 2][self.x -1] in black or self.board[self.y - 2][self.x -1] == 0:
                            self.possibleMoves.append((self.x - 1, self.y - 2))
                    
                    if self.y + 1 < 8 and self.x - 2 > -1 :
                        if self.board[self.y + 1][self.x -2] in black or self.board[self.y +1][self.x -2] == 0:
                            self.possibleMoves.append((self.x - 2, self.y + 1))
                    if self.y - 1 > -1 and self.x - 2 > -1 :
                        if self.board[self.y - 1][self.x -2] in black or self.board[self.y - 1][self.x -2] == 0:
                            self.possibleMoves.append((self.x - 2, self.y - 1))
                    
                    if self.y + 1 < 8 and self.x + 2 < 8 :
                        if self.board[self.y + 1][self.x +2] in black or self.board[self.y +1][self.x +2] == 0:
                            self.possibleMoves.append((self.x +2, self.y + 1))
                    if self.y - 1 > -1 and self.x + 2 < 8 :
                        if self.board[self.y - 1][self.x +2] in black or self.board[self.y -1][self.x +2] == 0:
                            self.possibleMoves.append((self.x +2, self.y - 1))
                elif self.type == WBISHOP:
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y + i < 8 and self.x +i < 8:
                            if self.board[self.y + i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y + i))
                            elif self.board[self.y + i][self.x +i] in black:
                                self.possibleMoves.append((self.x +i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x +i] not in black and self.board[self.y + i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down left
                        i += 1
                        if self.y + i < 8 and self.x -i > -1:
                            if self.board[self.y + i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y + i))
                            elif self.board[self.y + i][self.x -i] in black:
                                self.possibleMoves.append((self.x -i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x -i] not in black and self.board[self.y + i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up left
                        i += 1
                        if self.y - i > -1 and self.x -i > -1:
                            if self.board[self.y - i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y - i))
                            elif self.board[self.y - i][self.x -i] in black:
                                self.possibleMoves.append((self.x -i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x -i] not in black and self.board[self.y - i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up Right
                        i += 1
                        if self.y - i > -1 and self.x +i < 8:
                            if self.board[self.y - i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y - i))
                            elif self.board[self.y - i][self.x +i] in black:
                                self.possibleMoves.append((self.x +i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x +i] not in black and self.board[self.y - i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == WQUEEN:
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y + i < 8:
                            if self.board[self.y + i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y + i))
                            elif self.board[self.y + i][self.x] in black:
                                self.possibleMoves.append((self.x, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x] not in black and self.board[self.y + i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#up
                        i += 1
                        if self.y - i > -1:
                            if self.board[self.y - i][self.x] == 0:
                                self.possibleMoves.append((self.x, self.y - i))
                            elif self.board[self.y - i][self.x] in black:
                                self.possibleMoves.append((self.x, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x] not in black and self.board[self.y - i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x - i > -1:
                            if self.board[self.y][self.x -i] == 0:
                                self.possibleMoves.append((self.x - i, self.y))
                            elif self.board[self.y][self.x -i] in black:
                                self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x -i] not in black and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#Right
                        i += 1
                        if self.x + i < 8:
                            if self.board[self.y][self.x +i] == 0:
                                self.possibleMoves.append((self.x + i, self.y))
                            elif self.board[self.y][self.x +i] in black:
                                self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x +i] not in black and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y + i < 8 and self.x +i < 8:
                            if self.board[self.y + i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y + i))
                            elif self.board[self.y + i][self.x +i] in black:
                                self.possibleMoves.append((self.x +i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x +i] not in black and self.board[self.y + i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down left
                        i += 1
                        if self.y + i < 8 and self.x -i > -1:
                            if self.board[self.y + i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y + i))
                            elif self.board[self.y + i][self.x -i] in black:
                                self.possibleMoves.append((self.x -i, self.y + i))
                                collide = True
                            elif self.board[self.y + i][self.x -i] not in black and self.board[self.y + i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up left
                        i += 1
                        if self.y - i > -1 and self.x -i > -1:
                            if self.board[self.y - i][self.x -i] == 0:
                                self.possibleMoves.append((self.x -i, self.y - i))
                            elif self.board[self.y - i][self.x -i] in black:
                                self.possibleMoves.append((self.x -i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x -i] not in black and self.board[self.y - i][self.x -i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # Up Right
                        i += 1
                        if self.y - i > -1 and self.x +i < 8:
                            if self.board[self.y - i][self.x +i] == 0:
                                self.possibleMoves.append((self.x +i, self.y - i))
                            elif self.board[self.y - i][self.x +i] in black:
                                self.possibleMoves.append((self.x +i, self.y - i))
                                collide = True
                            elif self.board[self.y - i][self.x +i] not in black and self.board[self.y - i][self.x +i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == WKING:
                    if self.y + 1 < 8: # down
                        if self.board[self.y + 1][self.x] == 0 or self.board[self.y + 1][self.x] in black:
                            self.possibleMoves.append((self.x, self.y + 1))
                    
                    if self.y - 1 > -1: # up
                        if self.board[self.y - 1][self.x] == 0 or self.board[self.y - 1][self.x] in black:
                            self.possibleMoves.append((self.x, self.y - 1))

                    if self.x -1 > -1: # left
                        if self.board[self.y][self.x-1] == 0 or self.board[self.y][self.x-1] in black:
                            self.possibleMoves.append((self.x-1, self.y))
                    
                    if self.x+1 > -1: # RIGHT
                        if self.board[self.y][self.x+1] == 0 or self.board[self.y][self.x+1] in black:
                            self.possibleMoves.append((self.x+1, self.y))

                    if self.x-1 > -1 and self.y -1 > -1: # up left
                        if self.board[self.y - 1][self.x-1] == 0 or self.board[self.y - 1][self.x-1] in black:
                            self.possibleMoves.append((self.x-1, self.y - 1))

                    if self.x-1 > -1 and self.y +1 < 8: # down left
                        if self.board[self.y + 1][self.x-1] == 0 or self.board[self.y + 1][self.x-1] in black:
                            self.possibleMoves.append((self.x-1, self.y + 1))
                    
                    if self.x+1 < 8 and self.y -1 > -1: # up right
                        if self.board[self.y - 1][self.x+1] == 0 or self.board[self.y - 1][self.x+1] in black:
                            self.possibleMoves.append((self.x+1, self.y - 1))

                    if self.x+1 < 8 and self.y +1 < 8: # down right
                        if self.board[self.y + 1][self.x+1] == 0 or self.board[self.y + 1][self.x+1] in black:
                            self.possibleMoves.append((self.x+1, self.y + 1))
                elif self.type == WPAWN:
                    if self.y - 1 > -1 and self.board[self.y - 1][self.x] == 0:
                        self.possibleMoves.append((self.x, self.y - 1))
                    if self.y -2 > -1 and self.board[self.y -2][self.x] == 0 and self.y == 6:
                       self.possibleMoves.append((self.x, self.y - 2))
                    if self.y -1 > -1 and self.x + 1 < 8:
                        if self.board[self.y -1][self.x + 1] in black:
                            self.possibleMoves.append((self.x + 1, self.y -1))
                    if self.y -1 > -1 and self.x - 1 < 8:
                        if self.board[self.y -1][self.x - 1] in black:
                            self.possibleMoves.append((self.x - 1, self.y -1))
    
class Chess:
    scale = 40
    x = 150
    y = 160
    height = 8
    width = 8
    field = []
    piece = None
    def __init__(self):
        self.piece = None
        self.field = [[BROOK, BKNIGHT, BBISHOP, BQUEEN, BKING, BBISHOP, BKNIGHT,BROOK],[BPAWN,BPAWN,BPAWN,BPAWN,BPAWN,BPAWN,BPAWN,BPAWN],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[WPAWN,WPAWN,WPAWN,WPAWN,WPAWN,WPAWN,WPAWN,WPAWN],[WROOK,WKNIGHT,WBISHOP,WQUEEN,WKING,WBISHOP,WKNIGHT,WROOK]]
    
    def current_piece(self, x, y, type):
        self.piece = Pieces(x, y, type, self.field)
    def piece_unselecter(self):
        self.piece = None




pygame.init()


GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (120, 37, 179)

WHITETURN = True


size = (600, 800)
screen = pygame.display.set_mode(size)
game = Chess()
fps = 25
clock = pygame.time.Clock()
pygame.display.set_caption("Chess")
clicked_pos = None
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            for i in range(game.height):
                for j in range(game.width):
                    x = game.x + (game.scale *j) #150 + (40 * 8) = 470, 150 + (40*5) = 350, 150 
                    xend = x + game.scale -1 #470 + 40, 350 + 40 = 390
                    y = game.y + (game.scale *i) 
                    yend = y + game.scale - 1
                    if (event.pos[0] >= game.x and event.pos[0] <= game.x +  (game.scale * game.width)) and (event.pos[1] >= game.y and event.pos[1] <= game.y + (game.scale * game.height)):
                        if (event.pos[0] > x and event.pos[0] < xend) and (event.pos[1] > y and event.pos[1] < yend):
                            clicked_pos = (j, i)
                            clicked_x = clicked_pos[0]
                            clicked_y = clicked_pos[1]
                            #print(clicked_pos)
                            #print(game.field[clicked_y][clicked_x])
                    elif event.pos[0] <= game.x or event.pos[0] >= game.x + (game.scale * game.width) or event.pos[1] <= game.y or event.pos[1] >= game.y +(game.scale * game.height):
                        clicked_pos = None
                        clicked_x = None
                        clicked_y = None
            if clicked_pos is not None:
                if WHITETURN:
                    if game.field[clicked_y][clicked_x] in white:
                        game.current_piece(clicked_x, clicked_y, game.field[clicked_y][clicked_x]) #0, 6, 12
                        game.piece.move_getter()
                    elif game.field[clicked_y][clicked_x] == 0:
                        pass
                else:
                    if game.field[clicked_y][clicked_x] in black:
                        game.current_piece(clicked_x, clicked_y, game.field[clicked_y][clicked_x]) #0, 6, 12
                        game.piece.move_getter()
                    elif game.field[clicked_y][clicked_x] == 0:
                        pass
            elif clicked_pos is None:
                game.piece_unselecter()
            if game.piece is not None:
                old_clicked_pos = (game.piece.y,game.piece.x)
                if clicked_pos in game.piece.possibleMoves:
                    game.field[old_clicked_pos[0]][old_clicked_pos[1]] = 0
                    game.field[clicked_pos[1]][clicked_pos[0]] = game.piece.type
                    game.piece_unselecter()
                    if WHITETURN:
                        WHITETURN = False
                    else:
                        WHITETURN = True

    screen.fill(WHITE)
    
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2] )
    pygame.draw.rect(screen, BLACK, [game.x , game.y  , game.scale * game.width, game.scale * game.height],5)
    for i in range(game.height):
        for j in range(game.width):
            if game.piece is not None:
                #print(game.piece.possibleMoves)
                if (j, i) in game.piece.possibleMoves:
                    pygame.draw.rect(screen, PURPLE, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2])
            if game.field[i][j] != 0:
                text = font.render(str(game.field[i][j]), True, BLACK)
                screen.blit(text, [game.x + (game.scale*j), game.y + (game.scale * i)])
            if game.field[i][j] == BKING:
                bkingpos = (j,i)
            if game.field[i][j] == WKING:
                wkingpos = (j,i)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit