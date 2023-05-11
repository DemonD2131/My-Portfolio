import pygame

#EDIT: May 11, 2023: I made this from scratch using some of the code from chess1.0. I wanted to make it better than it previously was. I don't remmeber if I suceeded? But I'm pretty sure the code is cleaner.
class Piece:
    possibleMoves = []
    def __init__(self,x,y,type,board):
        self.x = x
        self.y = y
        self.type = type
        self.board = board
        self.possibleMoves = []
    def getMoves(self):
        self.possibleMoves = []
        for i in range(Chess.height):
            for j in range(Chess.width):
                if self.type == BROOK:
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y+i < 8:
                            if self.board[self.y+i][self.x] == 0:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                            elif self.board[self.y+i][self.x] in white:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x] not in white and self.board[self.y+i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up movement
                        i += 1
                        if self.y-i > -1:
                            if self.board[self.y-i][self.x] == 0:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                            elif self.board[self.y-i][self.x] in white:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x] not in white and self.board[self.y-i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x-i > -1:
                            if self.board[self.y][self.x-i] == 0:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                            elif self.board[self.y][self.x-i] in white:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x-i] not in white and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#right
                        i += 1
                        if self.x+i < 8:
                            if self.board[self.y][self.x+i] == 0:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                            elif self.board[self.y][self.x+i] in white:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x+i] not in white and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == BKNIGHT:
                    if self.y+2 < 8 and self.x+1 < 8 : #downright
                        if self.board[self.y+2][self.x+1] in white or self.board[self.y +2][self.x+1] == 0:
                            if (self.x+1,self.y+2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y+2))
                    
                    
                    if self.y-2 > -1 and self.x+1 < 8 : #up right
                        if self.board[self.y-2][self.x+1] in white or self.board[self.y-2][self.x+1] == 0:
                            if (self.x+1,self.y-2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y-2))
                    
                    
                    if self.y+2 < 8 and self.x-1 > -1 : #down left
                        if self.board[self.y+2][self.x-1] in white or self.board[self.y+2][self.x-1] == 0:
                            if (self.x-1,self.y+2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y+2))
                    
                    if self.y-2 > -1 and self.x-1 > -1 : #up left
                        if self.board[self.y-2][self.x-1] in white or self.board[self.y-2][self.x-1] == 0:
                            if (self.x-1,self.y-2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y-2))
                    
                    if self.y+1 < 8 and self.x-2 > -1 : #down left
                        if self.board[self.y+1][self.x-2] in white or self.board[self.y+1][self.x-2] == 0:
                            if (self.x-2,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-2, self.y+1))
                    
                    if self.y-1 > -1 and self.x-2 > -1 : #up left
                        if self.board[self.y-1][self.x-2] in white or self.board[self.y-1][self.x-2] == 0:
                            if (self.x-2,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-2, self.y-1))
                    
                    if self.y+1 < 8 and self.x+2 < 8 : #down right
                        if self.board[self.y+1][self.x+2] in white or self.board[self.y+1][self.x+2] == 0:
                            if (self.x+2,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+2, self.y+1))
                elif self.type == BBISHOP:
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y+i < 8 and self.x+i < 8:
                            if self.board[self.y+i][self.x+i] == 0:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                            elif self.board[self.y+i][self.x+i] in white:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x+i] not in white and self.board[self.y+i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up right
                        i += 1
                        if self.y-i > -1 and self.x+i < 8:
                            if self.board[self.y-i][self.x+i] == 0:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                            elif self.board[self.y-i][self.x+i] in white:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x+i] not in white and self.board[self.y-i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up left
                        i += 1
                        if self.y-i > -1 and self.x-i > -1:
                            if self.board[self.y-i][self.x-i] == 0:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                            elif self.board[self.y-i][self.x-i] in white:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x-i] not in white and self.board[self.y-i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y+i < 8 and self.x-i > -1:
                            if self.board[self.y+i][self.x-i] == 0:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                            elif self.board[self.y+i][self.x-i] in white:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x-i] not in white and self.board[self.y+i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == BQUEEN:
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y+i < 8 and self.x+i < 8:
                            if self.board[self.y+i][self.x+i] == 0:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                            elif self.board[self.y+i][self.x+i] in white:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x+i] not in white and self.board[self.y+i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up right
                        i += 1
                        if self.y-i > -1 and self.x+i < 8:
                            if self.board[self.y-i][self.x+i] == 0:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                            elif self.board[self.y-i][self.x+i] in white:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x+i] not in white and self.board[self.y-i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up left
                        i += 1
                        if self.y-i > -1 and self.x-i > -1:
                            if self.board[self.y-i][self.x-i] == 0:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                            elif self.board[self.y-i][self.x-i] in white:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x-i] not in white and self.board[self.y-i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down left
                        i += 1
                        if self.y+i < 8 and self.x-i > -1:
                            if self.board[self.y+i][self.x-i] == 0:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                            elif self.board[self.y+i][self.x-i] in white:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x-i] not in white and self.board[self.y+i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y+i < 8:
                            if self.board[self.y+i][self.x] == 0:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                            elif self.board[self.y+i][self.x] in white:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x] not in white and self.board[self.y+i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up movement
                        i += 1
                        if self.y-i > -1:
                            if self.board[self.y-i][self.x] == 0:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                            elif self.board[self.y-i][self.x] in white:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x] not in white and self.board[self.y-i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x-i > -1:
                            if self.board[self.y][self.x-i] == 0:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                            elif self.board[self.y][self.x-i] in white:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x-i] not in white and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#right
                        i += 1
                        if self.x+i < 8:
                            if self.board[self.y][self.x+i] == 0:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                            elif self.board[self.y][self.x+i] in white:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x+i] not in white and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == BKING:
                    if self.y+1 < 8: # down
                        if self.board[self.y+1][self.x] == 0 or self.board[self.y+1][self.x] in white:
                            if (self.x,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x, self.y+1))
                    if self.y-1 > -1: # up
                        if self.board[self.y-1][self.x] == 0 or self.board[self.y-1][self.x] in white:
                            if (self.x,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x, self.y-1))
                    if self.x-1 > -1: # left
                        if self.board[self.y][self.x-1] == 0 or self.board[self.y][self.x-1] in white:
                            if (self.x-1,self.y) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y))
                    if self.x+1 < 8: # right
                        if self.board[self.y][self.x+1] == 0 or self.board[self.y][self.x+1] in white:
                            if (self.x+1,self.y) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y))

                    if self.x-1 > -1 and self.y-1 > -1: # up left
                        if self.board[self.y-1][self.x-1] == 0 or self.board[self.y-1][self.x-1] in white:
                            if (self.x-1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y-1))
                    if self.x+1 < 8 and self.y-1 > -1: # up right
                        if self.board[self.y-1][self.x+1] == 0 or self.board[self.y-1][self.x+1] in white:
                            if (self.x+1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y-1))
                    if self.x+1 < 8 and self.y+1 < 8: # downn right
                        if self.board[self.y+1][self.x+1] == 0 or self.board[self.y+1][self.x+1] in white:
                            if (self.x+1,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y+1))
                    if self.x-1 > -1 and self.y+1 < 8: # downn left
                        if self.board[self.y+1][self.x-1] == 0 or self.board[self.y+1][self.x-1] in white:
                            if (self.x-1,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y+1))
                elif self.type == BPAWN:
                    if self.y-1 < 8: #up
                        if self.board[self.y-1][self.x] == 0:
                            if (self.x,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x,self.y-1))
                    if self.y-2 < 8: #extra up
                        if self.board[self.y-2][self.x] == 0 and self.y == 1:
                            if self.board[self.y-1][self.x] == 0:
                                if (self.x,self.y-2) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x,self.y-2))
                    if self.y-1 < 8 and self.x+1 < 8: #up right
                        if self.board[self.y-1][self.x+1] in white:
                            if (self.x+1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y-1))
                    if self.y-1 < 8 and self.x-1 > -1: #up left
                        if self.board[self.y-1][self.x-1] in white:
                            if (self.x-1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y-1))
                elif self.type == WROOK:
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y+i < 8:
                            if self.board[self.y+i][self.x] == 0:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                            elif self.board[self.y+i][self.x] in black:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x] not in black and self.board[self.y+i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up movement
                        i += 1
                        if self.y-i > -1:
                            if self.board[self.y-i][self.x] == 0:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                            elif self.board[self.y-i][self.x] in black:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x] not in black and self.board[self.y-i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x-i > -1:
                            if self.board[self.y][self.x-i] == 0:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                            elif self.board[self.y][self.x-i] in black:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x-i] not in black and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#right
                        i += 1
                        if self.x+i < 8:
                            if self.board[self.y][self.x+i] == 0:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                            elif self.board[self.y][self.x+i] in black:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x+i] not in black and self.board[self.y][self.x+i] != 0:
                                collide = True
                elif self.type == WKNIGHT:
                    if self.y+2 < 8 and self.x+1 < 8 : #downright
                        if self.board[self.y+2][self.x+1] in black or self.board[self.y +2][self.x+1] == 0:
                            if (self.x+1,self.y+2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y+2))
                    
                    
                    if self.y-2 > -1 and self.x+1 < 8 : #up right
                        if self.board[self.y-2][self.x+1] in black or self.board[self.y-2][self.x+1] == 0:
                            if (self.x+1,self.y-2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y-2))
                    
                    
                    if self.y+2 < 8 and self.x-1 > -1 : #down left
                        if self.board[self.y+2][self.x-1] in black or self.board[self.y+2][self.x-1] == 0:
                            if (self.x-1,self.y+2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y+2))
                    
                    if self.y-2 > -1 and self.x-1 > -1 : #up left
                        if self.board[self.y-2][self.x-1] in black or self.board[self.y-2][self.x-1] == 0:
                            if (self.x-1,self.y-2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y-2))
                    
                    if self.y+1 < 8 and self.x-2 > -1 : #down left
                        if self.board[self.y+1][self.x-2] in black or self.board[self.y+1][self.x-2] == 0:
                            if (self.x-2,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-2, self.y+1))
                    
                    if self.y-1 > -1 and self.x-2 > -1 : #up left
                        if self.board[self.y-1][self.x-2] in black or self.board[self.y-1][self.x-2] == 0:
                            if (self.x-2,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-2, self.y-1))
                    
                    if self.y+1 < 8 and self.x+2 < 8 : #down right
                        if self.board[self.y+1][self.x+2] in black or self.board[self.y+1][self.x+2] == 0:
                            if (self.x+2,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+2, self.y+1))
                elif self.type == WBISHOP:
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y+i < 8 and self.x+i < 8:
                            if self.board[self.y+i][self.x+i] == 0:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                            elif self.board[self.y+i][self.x+i] in black:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x+i] not in black and self.board[self.y+i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up right
                        i += 1
                        if self.y-i > -1 and self.x+i < 8:
                            if self.board[self.y-i][self.x+i] == 0:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                            elif self.board[self.y-i][self.x+i] in black:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x+i] not in black and self.board[self.y-i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up left
                        i += 1
                        if self.y-i > -1 and self.x-i > -1:
                            if self.board[self.y-i][self.x-i] == 0:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                            elif self.board[self.y-i][self.x-i] in black:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x-i] not in black and self.board[self.y-i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y+i < 8 and self.x-i > -1:
                            if self.board[self.y+i][self.x-i] == 0:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                            elif self.board[self.y+i][self.x-i] in black:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x-i] not in black and self.board[self.y+i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == WQUEEN:
                    i = 0
                    collide = False
                    while collide == False: # down right
                        i += 1
                        if self.y+i < 8 and self.x+i < 8:
                            if self.board[self.y+i][self.x+i] == 0:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                            elif self.board[self.y+i][self.x+i] in black:
                                if (self.x+i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x+i] not in black and self.board[self.y+i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up right
                        i += 1
                        if self.y-i > -1 and self.x+i < 8:
                            if self.board[self.y-i][self.x+i] == 0:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                            elif self.board[self.y-i][self.x+i] in black:
                                if (self.x+i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x+i] not in black and self.board[self.y-i][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up left
                        i += 1
                        if self.y-i > -1 and self.x-i > -1:
                            if self.board[self.y-i][self.x-i] == 0:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                            elif self.board[self.y-i][self.x-i] in black:
                                if (self.x-i,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x-i] not in black and self.board[self.y-i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down left
                        i += 1
                        if self.y+i < 8 and self.x-i > -1:
                            if self.board[self.y+i][self.x-i] == 0:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                            elif self.board[self.y+i][self.x-i] in black:
                                if (self.x-i,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x-i] not in black and self.board[self.y+i][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # down movement
                        i += 1
                        if self.y+i < 8:
                            if self.board[self.y+i][self.x] == 0:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                            elif self.board[self.y+i][self.x] in black:
                                if (self.x,self.y+i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y+i))
                                collide = True
                            elif self.board[self.y+i][self.x] not in black and self.board[self.y+i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0
                    collide = False
                    while collide == False: # up movement
                        i += 1
                        if self.y-i > -1:
                            if self.board[self.y-i][self.x] == 0:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                            elif self.board[self.y-i][self.x] in black:
                                if (self.x,self.y-i) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x, self.y-i))
                                collide = True
                            elif self.board[self.y-i][self.x] not in black and self.board[self.y-i][self.x] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#left
                        i += 1
                        if self.x-i > -1:
                            if self.board[self.y][self.x-i] == 0:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                            elif self.board[self.y][self.x-i] in black:
                                if (self.x-i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x-i, self.y))
                                collide = True
                            elif self.board[self.y][self.x-i] not in black and self.board[self.y][self.x-i] != 0:
                                collide = True
                        else:
                            collide = True
                    i = 0 
                    collide = False
                    while collide == False:#right
                        i += 1
                        if self.x+i < 8:
                            if self.board[self.y][self.x+i] == 0:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                            elif self.board[self.y][self.x+i] in black:
                                if (self.x+i,self.y) not in self.possibleMoves:
                                    self.possibleMoves.append((self.x+i, self.y))
                                collide = True
                            elif self.board[self.y][self.x+i] not in black and self.board[self.y][self.x+i] != 0:
                                collide = True
                        else:
                            collide = True
                elif self.type == WKING:
                    if self.y+1 < 8: # down
                        if self.board[self.y+1][self.x] == 0 or self.board[self.y+1][self.x] in black:
                            if (self.x,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x, self.y+1))
                    if self.y-1 > -1: # up
                        if self.board[self.y-1][self.x] == 0 or self.board[self.y-1][self.x] in black:
                            if (self.x,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x, self.y-1))
                    if self.x-1 > -1: # left
                        if self.board[self.y][self.x-1] == 0 or self.board[self.y][self.x-1] in black:
                            if (self.x-1,self.y) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y))
                    if self.x+1 < 8: # right
                        if self.board[self.y][self.x+1] == 0 or self.board[self.y][self.x+1] in black:
                            if (self.x+1,self.y) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y))

                    if self.x-1 > -1 and self.y-1 > -1: # up left
                        if self.board[self.y-1][self.x-1] == 0 or self.board[self.y-1][self.x-1] in black:
                            if (self.x-1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y-1))
                    if self.x+1 < 8 and self.y-1 > -1: # up right
                        if self.board[self.y-1][self.x+1] == 0 or self.board[self.y-1][self.x+1] in black:
                            if (self.x+1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y-1))
                    if self.x+1 < 8 and self.y+1 < 8: # downn right
                        if self.board[self.y+1][self.x+1] == 0 or self.board[self.y+1][self.x+1] in black:
                            if (self.x+1,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y+1))
                    if self.x-1 > -1 and self.y+1 < 8: # downn left
                        if self.board[self.y+1][self.x-1] == 0 or self.board[self.y+1][self.x-1] in black:
                            if (self.x-1,self.y+1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y+1))
                elif self.type == WPAWN:
                    if self.y-1 > -1: #up
                        if self.board[self.y-1][self.x] == 0:
                            if (self.x,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x,self.y-1))
                    if self.y-2 > -1: #exxtra up
                        if self.board[self.y-2][self.x] == 0 and self.y == 1:
                            if (self.x,self.y-2) not in self.possibleMoves:
                                self.possibleMoves.append((self.x,self.y-2))
                    if self.y-1 < 8 and self.x+1 < 8: #up right
                        if self.board[self.y-1][self.x+1] in black:
                            if (self.x+1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x+1, self.y-1))
                    if self.y-1 < 8 and self.x-1 > -1: #up left
                        if self.board[self.y-1][self.x-1] in black:
                            if (self.x-1,self.y-1) not in self.possibleMoves:
                                self.possibleMoves.append((self.x-1, self.y-1))
        print("MOves- " + str(self.possibleMoves))
        return self.possibleMoves


class Chess():
    scale = 40
    x = 150
    y = 160
    height = 8
    width = 8
    field = []
    piece = None
    pieces = []
    BLACKTURN = False
    whiteWin = False
    blackWin = False
    playerMoves = []
    def __init__(self):
        self.piece = None
        self.whiteWin = False
        self.blackWin = False
        self.pieces = []
        self.BLACKTURN = False
        self.field = STARTBOARD
        self.playerMoves = []
    def get_pieces(self):
        self.pieces = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        self.movesW = []
        self.movesB = []
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j] != 0:
                    #self.pieces[i].append(Piece(j,i,self.field[i][j],self.field))
                    self.pieces[i].insert(j,Piece(j,i,self.field[i][j],self.field))
                    self.pieces[i].pop(j+1)
                #if self.field[i][j] in white:
                    #whiteMoves = self.pieces[i][j].getMoves()
                #    self.movesW.append([(5,10)])
                #if self.field[i][j] in black:
                #    #blackMoves = self.pieces[i][j].getMoves()
                #    self.movesB.append((5,10))
        #print(len(self.pieces))
        #print(len(self.pieces[0]))
    def current_piece(self,x,y):
        self.get_pieces()
        self.piece = self.pieces[y][x]
        self.playerMoves = self.piece.getMoves()
    def flipBoard(self):
        flipVertical(self.field)



 
def positionGetter(pos):
    ex = pos[0]
    ey = pos[1]
    spot = None
    if game.blackWin == False and game.whiteWin == False:
        for i in range(game.height):
            for j in range(game.width):
                #some helpful variables for the check
                x = game.x + (game.scale *j) 
                xend = x + game.scale
                y = game.y + (game.scale *i) 
                yend = y + game.scale
                #checks if the event position is within the game
                if (ex >= game.x and ex <= game.x + (game.scale * game.width)) and (ey >= game.y and ey <= game.y + (game.scale * game.height)):
                    #checks if the event position is within a square and assigns the clicked pos into coords that make sense
                    if (ex > x and ex < xend) and (ey > y and ey < yend):
                        spot = (j,i)
                elif (ex <= game.x or ex >= game.x + (game.scale * game.width)) or (ey <= game.y or ey >= game.y + (game.scale * game.height)):
                    spot = None
    return spot
def turnToggle():
    game.flipBoard()
    if game.BLACKTURN == True:
        game.BLACKTURN = False
    elif game.BLACKTURN == False:
        game.BLACKTURN = True
def flipVertical(a):
    for y in range(len(a)//2):
        temp = a[y]
        a[y] = a[len(a) - 1 - y]
        a[len(a) - 1 - y] = temp
#MAIN ****************************************************************************************************
pygame.init()

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
#constants
STARTBOARD = [[BROOK, BKNIGHT, BBISHOP, BQUEEN, BKING, BBISHOP, BKNIGHT,BROOK],[BPAWN,BPAWN,BPAWN,BPAWN,BPAWN,BPAWN,BPAWN,BPAWN],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[WPAWN,WPAWN,WPAWN,WPAWN,WPAWN,WPAWN,WPAWN,WPAWN],[WROOK,WKNIGHT,WBISHOP,WQUEEN,WKING,WBISHOP,WKNIGHT,WROOK]]


#colors
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTBLUE = (3, 219, 252)


INVERTRED = ( 77, 223, 146 )

ARED = (255,0,0)
ORANGE = (255, 153, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = ( 59, 79, 221 )
PURPLE = (120, 37, 179)

#Variables
fps = 25
size = (800, 600)
screen = pygame.display.set_mode(size)
game = Chess()
clock = pygame.time.Clock()
pygame.display.set_caption("Chess :)")
done = False
clicked_pos = None
cheatOn = False

while done is False:
    game.get_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = positionGetter(event.pos)
            game.get_pieces()
            print(clicked_pos)
            if game.piece is not None:
                if clicked_pos in game.playerMoves:
                    old_clicked_pos = (game.piece.y, game.piece.x)
                    game.field[old_clicked_pos[0]][old_clicked_pos[1]] = 0
                    game.field[clicked_pos[1]][clicked_pos[0]] = game.piece.type
                    game.piece = None
                    clicked_pos = None
                    turnToggle()


    
    if clicked_pos is not None and cheatOn == False:
        if game.BLACKTURN == True:
            if game.field[clicked_pos[1]][clicked_pos[0]] in black:
                game.current_piece(clicked_pos[0],clicked_pos[1])
        elif game.BLACKTURN == False:
            if game.field[clicked_pos[1]][clicked_pos[0]] in white:
                game.current_piece(clicked_pos[0],clicked_pos[1])
    elif clicked_pos is None:
        game.piece = None

    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    if game.BLACKTURN == True:
        count = 1
    elif game.BLACKTURN == False:
        count = 0
    for i in range(game.height):
        count += 1
        for j in range(game.width):
            count += 1 #for traditional chessboard look
            if count % 2 == 0:
                current_color = GRAY
            elif count % 2 == 1:
                current_color = LIGHTBLUE
            pygame.draw.rect(screen, current_color, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2])#Game tiles
            if game.piece is not None:
                if (j, i) in game.playerMoves:
                    pygame.draw.rect(screen, PURPLE, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2])
            if game.field[i][j] != 0:
                if game.field[i][j] in black:
                    text = font.render(str(game.field[i][j]), True, BLACK)
                elif game.field[i][j] in white:
                    text = font.render(str(game.field[i][j]),True, WHITE)
                screen.blit(text, [game.x + (game.scale*j), game.y + (game.scale * i)])
    pygame.display.flip()
    clock.tick(fps)

pygame.quit