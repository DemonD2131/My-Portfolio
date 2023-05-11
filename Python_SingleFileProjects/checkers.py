#Dominic Rondeau v3.0
#Checkers **the hard way**
#A game of checkers made entirely through pygame
#Started April 28, 2022
#Ended May 12, 2022


import pygame


RP = 1
RK = 2
BP = 3
BK = 4

REDPIECES = [1,2]
BLACKPIECES = [3,4]


STARTBOARD = [[0,RP,0,RP,0,RP,0,RP],[RP,0,RP,0,RP,0,RP,0],[0,RP,0,RP,0,RP,0,RP],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[BP,0,BP,0,BP,0,BP,0],[0,BP,0,BP,0,BP,0,BP],[BP,0,BP,0,BP,0,BP,0]]

class Piece:
    possibleNonSelectedMovesRed = []
    possibleNonSelectedMovesBlack = []
    possiblePlayerMoves = []
    killMoves = []
    killSpot = []
    def __init__(self,x,y,type,board):
        self.x = x
        self.y = y
        self.pos = (x,y)
        self.board = board
        self.type = type
    def getMovesPlayer(self):
        self.possiblePlayerMoves = []
        self.killMoves = []
        self.killSpot = []
        for i in range(Checkers.height):
            for j in range(Checkers.width):
                if self.type == RP:
                    """
                    if self.x - 1 > -1 and self.y + 1 < 8:#down left
                        if self.board[self.y + 1][self.x - 1] == 0:
                            if (self.x - 1,self.y + 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y + 1))
                                
                        elif self.board[self.y + 1][self.x - 1] in BLACKPIECES:
                            if self.x - 2 > -1 and self.y + 2 < 8:
                                if self.board[self.y + 2][self.x - 2] == 0:
                                    if (self.x-2,self.y+2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y + 2))
                                        self.killSpot.append((self.x - 1,self.y + 1))
                    
                    if self.x + 1 < 8 and self.y + 1 < 8: #down right
                        if self.board[self.y + 1][self.x + 1] == 0:
                            if (self.x + 1,self.y + 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y + 1))
                                
                        elif self.board[self.y + 1][self.x + 1] in BLACKPIECES:
                            if self.x + 2 < 8 and self.y + 2 < 8:
                                if self.board[self.y + 2][self.x + 2] == 0:
                                    if (self.x +2,self.y+2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y + 2))
                                        self.killSpot.append((self.x + 1,self.y + 1))
                                        """
                    if self.x - 1 > -1 and self.y - 1 < 8:#up left
                        if self.board[self.y - 1][self.x - 1] == 0:
                            if (self.x - 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y - 1))
                        elif self.board[self.y - 1][self.x - 1] in BLACKPIECES:
                            if self.x - 2 > -1 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x - 2] == 0:
                                    if (self.x -2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y - 2))
                                        self.killSpot.append((self.x - 1,self.y - 1))
                    
                    if self.x + 1 < 8 and self.y - 1 < 8: #up right
                        if self.board[self.y - 1][self.x + 1] == 0:
                            if (self.x + 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y - 1))
                        elif self.board[self.y - 1][self.x + 1] in BLACKPIECES:
                            if self.x + 2 < 8 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x + 2] == 0:
                                    if (self.x+2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y - 2))
                                        self.killSpot.append((self.x + 1,self.y - 1))
                elif self.type == RK:
                    if self.x - 1 > -1 and self.y + 1 < 8:#down left
                        if self.board[self.y + 1][self.x - 1] == 0:
                            if (self.x - 1,self.y + 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y + 1))
                                
                        elif self.board[self.y + 1][self.x - 1] in BLACKPIECES:
                            if self.x - 2 > -1 and self.y + 2 < 8:
                                if self.board[self.y + 2][self.x - 2] == 0:
                                    if (self.x-2,self.y+2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y + 2))
                                        self.killSpot.append((self.x - 1,self.y + 1))
                    
                    if self.x + 1 < 8 and self.y + 1 < 8: #down right
                        if self.board[self.y + 1][self.x + 1] == 0:
                            if (self.x + 1,self.y + 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y + 1))
                                
                        elif self.board[self.y + 1][self.x + 1] in BLACKPIECES:
                            if self.x + 2 < 8 and self.y + 2 < 8:
                                if self.board[self.y + 2][self.x + 2] == 0:
                                    if (self.x+2,self.y+2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y + 2))
                                        self.killSpot.append((self.x + 1,self.y + 1))
                    
                    if self.x - 1 > -1 and self.y - 1 < 8:#up left
                        if self.board[self.y - 1][self.x - 1] == 0:
                            if (self.x - 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y - 1))

                        elif self.board[self.y - 1][self.x - 1] in BLACKPIECES:
                            if self.x - 2 > -1 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x - 2] == 0:
                                    if (self.x -2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y - 2))
                                        self.killSpot.append((self.x - 1,self.y - 1))
                    
                    if self.x + 1 < 8 and self.y - 1 < 8: #up right
                        if self.board[self.y - 1][self.x + 1] == 0:
                            if (self.x + 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y - 1))
                        elif self.board[self.y - 1][self.x + 1] in BLACKPIECES:
                            if self.x + 2 < 8 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x + 2] == 0:
                                    if (self.x+2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y - 2))
                                        self.killSpot.append((self.x + 1,self.y - 1))
                elif self.type == BP:
                    
                    if self.x - 1 > -1 and self.y - 1 < 8:#up left
                        if self.board[self.y - 1][self.x - 1] == 0:
                            if (self.x - 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y - 1))

                        elif self.board[self.y - 1][self.x - 1] in REDPIECES:
                            if self.x - 2 > -1 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x - 2] == 0:
                                    if (self.x-2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y - 2))
                                        self.killSpot.append((self.x - 1,self.y - 1))
                    
                    if self.x + 1 < 8 and self.y - 1 < 8: #up right
                        if self.board[self.y - 1][self.x + 1] == 0:
                            if (self.x + 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y - 1))

                        elif self.board[self.y - 1][self.x + 1] in REDPIECES:
                            if self.x + 2 < 8 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x + 2] == 0:
                                    if (self.x+2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y - 2))
                                        self.killSpot.append((self.x + 1,self.y - 1))
                                        
                elif self.type == BK:
                    
                    if self.x - 1 > -1 and self.y - 1 < 8:#up left
                        if self.board[self.y - 1][self.x - 1] == 0:
                            if (self.x - 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y - 1))

                        elif self.board[self.y - 1][self.x - 1] in REDPIECES:
                            if self.x - 2 > -1 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x - 2] == 0:
                                    if (self.x-2,self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y - 2))
                                        self.killSpot.append((self.x - 1,self.y - 1))
                    
                    if self.x + 1 < 8 and self.y - 1 < 8: #up right
                        if self.board[self.y - 1][self.x + 1] == 0:
                            if (self.x + 1,self.y - 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y - 1))

                        elif self.board[self.y - 1][self.x + 1] in REDPIECES:
                            if self.x + 2 < 8 and self.y - 2 < 8:
                                if self.board[self.y - 2][self.x + 2] == 0:
                                    if (self.x +2, self.y-2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y - 2))
                                        self.killSpot.append((self.x + 1,self.y - 1))

                    
                    if self.x - 1 > -1 and self.y + 1 < 8:#down left
                        if self.board[self.y + 1][self.x - 1] == 0:
                            if (self.x - 1,self.y + 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x - 1,self.y + 1))
                                
                        elif self.board[self.y + 1][self.x - 1] in REDPIECES:
                            if self.x - 2 > -1 and self.y + 2 < 8:
                                if self.board[self.y + 2][self.x - 2] == 0:
                                    if (self.x-2,self.y+2) not in self.killMoves:
                                        self.killMoves.append((self.x - 2,self.y + 2))
                                        self.killSpot.append((self.x - 1,self.y + 1))
                    
                    if self.x + 1 < 8 and self.y + 1 < 8: #down right
                        if self.board[self.y + 1][self.x + 1] == 0:
                            if (self.x + 1,self.y + 1) not in self.possiblePlayerMoves:
                                self.possiblePlayerMoves.append((self.x + 1,self.y + 1))
                                
                        elif self.board[self.y + 1][self.x + 1] in REDPIECES:
                            if self.x + 2 < 8 and self.y + 2 < 8:
                                if self.board[self.y + 2][self.x + 2] == 0:
                                    if (self.x+2,self.y+2) not in self.killMoves:
                                        self.killMoves.append((self.x + 2,self.y + 2))
                                        self.killSpot.append((self.x + 1,self.y + 1))
    def getMovesBoard(self,color):
        self.possibleNonSelectedMovesRed = []
        self.possibleNonSelectedMovesBlack = []
        for i in range(Checkers.height):
            for j in range(Checkers.width):
                if color == 0:
                    if self.type == RP:
                        if self.x - 1 > -1 and self.y - 1 < 8:#up left
                            if self.board[self.y - 1][self.x - 1] == 0:
                                if (self.x - 1,self.y - 1) not in self.possibleNonSelectedMovesRed:
                                    self.possibleNonSelectedMovesRed.append((self.x - 1,self.y - 1))
                            elif self.board[self.y - 1][self.x - 1] in BLACKPIECES:
                                if self.x - 2 > -1 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x - 2] == 0:
                                        if (self.x -2,self.y-2) not in self.possibleNonSelectedMovesRed:
                                            self.possibleNonSelectedMovesRed.append((self.x - 2,self.y - 2))
                        
                        if self.x + 1 < 8 and self.y - 1 < 8: #up right
                            if self.board[self.y - 1][self.x + 1] == 0:
                                if (self.x + 1,self.y - 1) not in self.possibleNonSelectedMovesRed:
                                    self.possibleNonSelectedMovesRed.append((self.x + 1,self.y - 1))
                            elif self.board[self.y - 1][self.x + 1] in BLACKPIECES:
                                if self.x + 2 < 8 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x + 2] == 0:
                                        if (self.x+2,self.y-2) not in self.possibleNonSelectedMovesRed: 
                                            self.possibleNonSelectedMovesRed.append((self.x + 2,self.y - 2))
                    elif self.type == RK:
                        if self.x - 1 > -1 and self.y + 1 < 8:#down left
                            if self.board[self.y + 1][self.x - 1] == 0:
                                if (self.x - 1,self.y + 1) not in self.possibleNonSelectedMovesRed:
                                    self.possibleNonSelectedMovesRed.append((self.x - 1,self.y + 1))
                                    
                            elif self.board[self.y + 1][self.x - 1] in BLACKPIECES:
                                if self.x - 2 > -1 and self.y + 2 < 8:
                                    if self.board[self.y + 2][self.x - 2] == 0:
                                        if (self.x-2,self.y+2) not in self.possibleNonSelectedMovesRed:
                                            self.possibleNonSelectedMovesRed.append((self.x - 2,self.y + 2))
                        
                        if self.x + 1 < 8 and self.y + 1 < 8: #down right
                            if self.board[self.y + 1][self.x + 1] == 0:
                                if (self.x + 1,self.y + 1) not in self.possibleNonSelectedMovesRed:
                                    self.possibleNonSelectedMovesRed.append((self.x + 1,self.y + 1))
                                    
                            elif self.board[self.y + 1][self.x + 1] in BLACKPIECES:
                                if self.x + 2 < 8 and self.y + 2 < 8:
                                    if self.board[self.y + 2][self.x + 2] == 0:
                                        if (self.x+2,self.y+2) not in self.possibleNonSelectedMovesRed:
                                            self.possibleNonSelectedMovesRed.append((self.x + 2,self.y + 2))
                        
                        if self.x - 1 > -1 and self.y - 1 < 8:#up left
                            if self.board[self.y - 1][self.x - 1] == 0:
                                if (self.x - 1,self.y - 1) not in self.possibleNonSelectedMovesRed:
                                    self.possibleNonSelectedMovesRed.append((self.x - 1,self.y - 1))

                            elif self.board[self.y - 1][self.x - 1] in BLACKPIECES:
                                if self.x - 2 > -1 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x - 2] == 0:
                                        if (self.x -2,self.y-2) not in self.possibleNonSelectedMovesRed:
                                            self.possibleNonSelectedMovesRed.append((self.x - 2,self.y - 2))
                        
                        if self.x + 1 < 8 and self.y - 1 < 8: #up right
                            if self.board[self.y - 1][self.x + 1] == 0:
                                if (self.x + 1,self.y - 1) not in self.possibleNonSelectedMovesRed:
                                    self.possibleNonSelectedMovesRed.append((self.x + 1,self.y - 1))
                            elif self.board[self.y - 1][self.x + 1] in BLACKPIECES:
                                if self.x + 2 < 8 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x + 2] == 0:
                                        if (self.x+2,self.y-2) not in self.possibleNonSelectedMovesRed:
                                            self.possibleNonSelectedMovesRed.append((self.x + 2,self.y - 2))
                    return self.possibleNonSelectedMovesRed
                elif color == 1:
                    if self.type == BP:
                        if self.x - 1 > -1 and self.y - 1 < 8:#up left
                            if self.board[self.y - 1][self.x - 1] == 0:
                                if (self.x - 1,self.y - 1) not in self.possibleNonSelectedMovesBlack:
                                    self.possibleNonSelectedMovesBlack.append((self.x - 1,self.y - 1))

                            elif self.board[self.y - 1][self.x - 1] in REDPIECES:
                                if self.x - 2 > -1 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x - 2] == 0:
                                        if (self.x-2,self.y-2) not in self.possibleNonSelectedMovesBlack:
                                            self.possibleNonSelectedMovesBlack.append((self.x - 2,self.y - 2))
                        
                        if self.x + 1 < 8 and self.y - 1 < 8: #up right
                            if self.board[self.y - 1][self.x + 1] == 0:
                                if (self.x + 1,self.y - 1) not in self.possibleNonSelectedMovesBlack:
                                    self.possibleNonSelectedMovesBlack.append((self.x + 1,self.y - 1))

                            elif self.board[self.y - 1][self.x + 1] in REDPIECES:
                                if self.x + 2 < 8 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x + 2] == 0:
                                        if (self.x+2,self.y-2) not in self.possibleNonSelectedMovesBlack:
                                            self.possibleNonSelectedMovesBlack.append((self.x + 2,self.y - 2))
                    elif self.type == BK:
                        if self.x - 1 > -1 and self.y - 1 < 8:#up left
                            if self.board[self.y - 1][self.x - 1] == 0:
                                if (self.x - 1,self.y - 1) not in self.possibleNonSelectedMovesBlack:
                                    self.possibleNonSelectedMovesBlack.append((self.x - 1,self.y - 1))

                            elif self.board[self.y - 1][self.x - 1] in REDPIECES:
                                if self.x - 2 > -1 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x - 2] == 0:
                                        if (self.x-2,self.y-2) not in self.possibleNonSelectedMovesBlack:
                                            self.possibleNonSelectedMovesBlack.append((self.x - 2,self.y - 2))
                        
                        if self.x + 1 < 8 and self.y - 1 < 8: #up right
                            if self.board[self.y - 1][self.x + 1] == 0:
                                if (self.x + 1,self.y - 1) not in self.possibleNonSelectedMovesBlack:
                                    self.possibleNonSelectedMovesBlack.append((self.x + 1,self.y - 1))

                            elif self.board[self.y - 1][self.x + 1] in REDPIECES:
                                if self.x + 2 < 8 and self.y - 2 < 8:
                                    if self.board[self.y - 2][self.x + 2] == 0:
                                        if (self.x +2, self.y-2) not in self.possibleNonSelectedMovesBlack:
                                            self.possibleNonSelectedMovesBlack.append((self.x + 2,self.y - 2))
                        if self.x - 1 > -1 and self.y + 1 < 8:#down left
                            if self.board[self.y + 1][self.x - 1] == 0:
                                if (self.x - 1,self.y + 1) not in self.possibleNonSelectedMovesBlack:
                                    self.possibleNonSelectedMovesBlack.append((self.x - 1,self.y + 1))
                                    
                            elif self.board[self.y + 1][self.x - 1] in REDPIECES:
                                if self.x - 2 > -1 and self.y + 2 < 8:
                                    if self.board[self.y + 2][self.x - 2] == 0:
                                        if (self.x-2,self.y+2) not in self.possibleNonSelectedMovesBlack:
                                            self.possibleNonSelectedMovesBlack.append((self.x - 2,self.y + 2))
                        
                        if self.x + 1 < 8 and self.y + 1 < 8: #down right
                            if self.board[self.y + 1][self.x + 1] == 0:
                                if (self.x + 1,self.y + 1) not in self.possibleNonSelectedMovesBlack:
                                    self.possibleNonSelectedMovesBlack.append((self.x + 1,self.y + 1))
                                    
                            elif self.board[self.y + 1][self.x + 1] in REDPIECES:
                                if self.x + 2 < 8 and self.y + 2 < 8:
                                    if self.board[self.y + 2][self.x + 2] == 0:
                                        if (self.x+2,self.y+2) not in self.possibleNonSelectedMovesBlack:
                                            self.possibleNonSelectedMovesBlack.append((self.x + 2,self.y + 2))
                    return self.possibleNonSelectedMovesBlack

class Checkers:
    scale = 40
    x = 150
    y = 160
    height = 8
    width = 8
    field = []
    flipField = []
    pieces = []
    redPC = 16
    blackPC = 16
    rWIN = False
    bWIN = False
    BLACKTURN = True
    def __init__(self):
        self.piece = None
        self.pieces = []
        self.field = STARTBOARD
        self.redPC = 16
        self.blackPC = 16
        self.rWIN = False
        self.bWIN = False
        self.movesR = []
        self.movesB = []
        
    def update_board_object(self):
        self.pieces = []
        self.blackPC = 0
        self.redPC = 0
        self.movesR = []
        self.movesB = []
        for i in range(self.height):
            self.pieces.append([])
            for j in range(self.width):
                if self.field[i][j] in BLACKPIECES:
                    self.blackPC += 1
                if self.field[i][j] in REDPIECES:
                    self.redPC += 1
                if self.field[i][j] != 0:
                    self.pieces[i].append(Piece(j,i,self.field[i][j],self.field))
                    if self.pieces[i][j].getMovesBoard(0) != []:
                        self.movesR.append(self.pieces[i][j].getMovesBoard(0))
                    if self.pieces[i][j].getMovesBoard(1) != []:
                        self.movesB.append(self.pieces[i][j].getMovesBoard(1))
                elif self.field[i][j] == 0:
                    self.pieces[i].append(0)
        if self.movesR == [] and self.BLACKTURN == False:
            self.bWIN = True
        if self.movesB == [] and self.BLACKTURN == True:
            self.rWIN = True
                

        
    def currentPiece(self,x,y,type):
        self.piece = self.pieces[y][x]
    def redBoard(self):
        self.flipField = flipVertical(self.field)
        
def positionGetter(pos):
    ex = pos[0]
    ey = pos[1]
    spot = None
    if game.bWIN == False and game.rWIN == False:
        for i in range(game.height):
            for j in range(game.width):
                #some helpful variables for the check
                x = game.x + (game.scale *j) 
                xend = x + game.scale
                y = game.y + (game.scale *i) 
                yend = y + game.scale
                #checks if the event position is within the game
                if (ex >= game.x and ex <= game.x +  (game.scale * game.width)) and (ey >= game.y and ey <= game.y + (game.scale * game.height)):
                    #checks if the event position is within a square and assigns the clicked pos into coords that make sense
                    if (ex > x and ex < xend) and (ey > y and ey < yend):
                        spot = (j,i)
                elif (ex <= game.x or ex >= game.x +  (game.scale * game.width)) or (ey <= game.y or ey >= game.y + (game.scale * game.height)):
                    spot = None
    return spot
def turnToggle():
    game.redBoard()
    if game.BLACKTURN == True:
        game.BLACKTURN = False
    elif game.BLACKTURN == False:
        game.BLACKTURN = True
def flipVertical(a):
    for y in range(len(a)//2):
        temp = a[y]
        a[y] = a[len(a) - 1 - y]
        a[len(a) - 1 - y] = temp
    return a
def draw_star(startx, starty, scale, color):
        heightscaled = (starty + (scale*3))
        pygame.draw.polygon(screen,color,[(startx, starty), (startx - scale, heightscaled), (startx + (scale/2), heightscaled - scale)])
        pygame.draw.polygon(screen,color,[(startx, heightscaled - (scale/1.5)), (startx - (scale*1.5), (starty + scale)), (startx + (scale*1.5), (starty + scale))])
        pygame.draw.polygon(screen, color,[(startx + scale, heightscaled), (startx, heightscaled - (scale/1.5)), (startx + (scale/2), heightscaled - scale)])
#************MAIN*****************
pygame.init()

GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (120, 37, 179)
BLUE = ( 59, 79, 221 )
RED = ( 77, 223, 146 )
ARED = (0,255,255)

size = (600, 800)
screen = pygame.display.set_mode(size)

game = Checkers()

clicked_pos = None

game.BLACKTURN = True

fps = 25
clock = pygame.time.Clock()
pygame.display.set_caption("CHECKERS")

downpressed = False
done = False
while done == False:#main game loop
    game.update_board_object()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if downpressed == True:
                    downpressed = False
                else:
                    downpressed = True
            if event.key == pygame.K_ESCAPE:
                game.__init__()
                game.update_board_object()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = positionGetter(event.pos)
            game.update_board_object()

            if downpressed == True:
                if clicked_pos is not None:
                    if game.field[clicked_pos[1]][clicked_pos[0]] != 0:
                        game.field[clicked_pos[1]][clicked_pos[0]] = 0
            elif downpressed == False:
                if game.piece is not None:
                    if clicked_pos in game.piece.possiblePlayerMoves:
                        old_clicked_pos = (game.piece.y, game.piece.x)
                        game.field[old_clicked_pos[0]][old_clicked_pos[1]] = 0
                        game.field[clicked_pos[1]][clicked_pos[0]] = game.piece.type
                        game.piece = None
                        clicked_pos = None
                        turnToggle()
                    elif game.piece.killMoves != []:
                        if clicked_pos in game.piece.killMoves:
                            old_clicked_pos = (game.piece.y, game.piece.x)
                            game.field[old_clicked_pos[0]][old_clicked_pos[1]] = 0
                            game.field[clicked_pos[1]][clicked_pos[0]] = game.piece.type
                            game.field[game.piece.killSpot[game.piece.killMoves.index(clicked_pos)][1]][game.piece.killSpot[game.piece.killMoves.index(clicked_pos)][0]] = 0
                            game.update_board_object()
                            game.currentPiece(clicked_pos[0],clicked_pos[1],game.field[clicked_pos[1]][clicked_pos[0]])
                            game.piece.getMovesPlayer()
                            
                            if game.piece.killMoves == []:
                                game.piece = None
                                clicked_pos = None
                                turnToggle()
                            elif game.piece.killMoves != []:
                                game.piece.possiblePlayerMoves = []


    screen.fill(WHITE)

    if clicked_pos is not None and downpressed == False:
        if game.BLACKTURN == True:
            if game.field[clicked_pos[1]][clicked_pos[0]] in BLACKPIECES:
                game.currentPiece(clicked_pos[0],clicked_pos[1],game.field[clicked_pos[1]][clicked_pos[0]])
                game.piece.getMovesPlayer()
        elif game.BLACKTURN == False:
            if game.field[clicked_pos[1]][clicked_pos[0]] in REDPIECES:
                game.currentPiece(clicked_pos[0],clicked_pos[1],game.field[clicked_pos[1]][clicked_pos[0]])
                game.piece.getMovesPlayer()
    elif clicked_pos is None:
        game.piece = None
    for j in range(game.width):
        if game.BLACKTURN == True:
            if game.field[0][j] == 3:
                game.field[0][j] = 4
            if game.field[7][j] == 1:
                game.field[7][j] = 2
        elif game.BLACKTURN == False:
            if game.field[0][j] == 1:
                game.field[0][j] = 2
            if game.field[7][j] == 3:
                game.field[7][j] = 4
    font = pygame.font.SysFont('Calibri', 25, True, False)
    #Lose checks
    if game.blackPC == 0:
        game.rWIN = True
    if game.redPC == 0:
        game.bWIN = True
    if game.BLACKTURN == True: #game.Blackturn view/graphics
        count = 0
        for i in range(game.height):
            count += 1
            for j in range(game.width):
                
                count += 1 #this count variable is to give a way to give the traditional board look
                if count % 2 == 0:
                    pygame.draw.rect(screen, GRAY, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2]) #FIELD BUT NOT PIECES
                elif count % 2 == 1:
                    pygame.draw.rect(screen, BLUE, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2]) #FIELD BUT NOT PIECES
                if clicked_pos is not None:
                    if game.BLACKTURN == True:
                        if game.field[clicked_pos[1]][clicked_pos[0]] in BLACKPIECES:
                            pygame.draw.circle(screen,PURPLE, (game.x + (game.scale * clicked_pos[0]) + game.scale //2, game.y + (game.scale * clicked_pos[1]) + game.scale //2),game.scale //4 )
                    elif game.BLACKTURN == False:
                        if game.field[clicked_pos[1]][clicked_pos[0]] in REDPIECES:
                            pygame.draw.circle(screen,PURPLE, (game.x + (game.scale * clicked_pos[0]) + game.scale //2, game.y + (game.scale * clicked_pos[1]) + game.scale //2),game.scale //4 )
                if game.piece is not None:
                    if game.field[i][j] in game.piece.possiblePlayerMoves:
                        pygame.draw.circle(screen,ARED, (game.x + (game.scale * j) + game.scale //2, game.y + (game.scale * i) + game.scale //2),game.scale //4 )
                if game.field[i][j] != 0:
                    if game.field[i][j] in REDPIECES:
                        text = font.render(str(game.field[i][j]), True, RED)
                    elif game.field[i][j] in BLACKPIECES:
                        text = font.render(str(game.field[i][j]),True, BLACK)
                
                    screen.blit(text, [game.x + (game.scale*j), game.y + (game.scale * i)])

        if game.bWIN == True:
            draw_star(game.x+game.scale*game.width//2,game.y,110,BLACK)
            font1 = pygame.font.SysFont('Calibri', 50, True, False)
            text1 = font.render("BLACK WINS",True,RED)
            screen.blit(text1, [game.x+(game.scale*game.width//3.5),game.y+(game.scale*game.height//2)])
        if game.rWIN == True:
            draw_star(game.x+game.scale*game.width//2,game.y,110,RED)
            font1 = pygame.font.SysFont('Calibri', 50, True, False)
            text1 = font.render("RED WINS",True,BLACK)
            screen.blit(text1, [game.x+(game.scale*game.width//3.5),game.y+(game.scale*game.height//2)])
    elif game.BLACKTURN == False: #Redturn view/graphics
        count = 1
        for i in range(game.height):
            count += 1
            for j in range(game.width):
                count += 1 #this count variable is to give a way to give the traditional board look
                if count % 2 == 0:
                    pygame.draw.rect(screen, GRAY, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2]) #FIELD BUT NOT PIECES
                elif count % 2 == 1:
                    pygame.draw.rect(screen, BLUE, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2]) #FIELD BUT NOT PIECES
                if clicked_pos is not None:
                    if game.BLACKTURN == True:
                        if game.flipField[clicked_pos[1]][clicked_pos[0]] in BLACKPIECES:
                            pygame.draw.circle(screen,PURPLE, (game.x + (game.scale * clicked_pos[0]) + game.scale //2, game.y + (game.scale * clicked_pos[1]) + game.scale //2),game.scale //4 )
                    elif game.BLACKTURN == False:
                        if game.flipField[clicked_pos[1]][clicked_pos[0]] in REDPIECES:
                            pygame.draw.circle(screen,PURPLE, (game.x + (game.scale * clicked_pos[0]) + game.scale //2, game.y + (game.scale * clicked_pos[1]) + game.scale //2),game.scale //4 )
                if game.piece is not None:
                    if game.flipField[i][j] in game.piece.possiblePlayerMoves:
                        pygame.draw.circle(screen,ARED, (game.x + (game.scale * j) + game.scale //2, game.y + (game.scale * i) + game.scale //2),game.scale //4 )
                if game.flipField[i][j] != 0:
                    if game.flipField[i][j] in REDPIECES:
                        text = font.render(str(game.flipField[i][j]), True, RED)
                    elif game.flipField[i][j] in BLACKPIECES:
                        text = font.render(str(game.flipField[i][j]),True, BLACK)
                
                    screen.blit(text, [game.x + (game.scale*j), game.y + (game.scale * i)])
        if game.bWIN == True:
            draw_star(game.x+game.scale*game.width//2,game.y,110,BLACK)
            font1 = pygame.font.SysFont('Calibri', 50, True, False)
            text1 = font.render("BLACK WINS",True,RED)
            screen.blit(text1, [game.x+(game.scale*game.width//3.5),game.y+(game.scale*game.height//2)])
        if game.rWIN == True:
            draw_star(game.x+game.scale*game.width//2,game.y,110,RED)
            font1 = pygame.font.SysFont('Calibri', 50, True, False)
            text1 = font.render("RED WINS",True,BLACK)
            screen.blit(text1, [game.x+(game.scale*game.width//3.5),game.y+(game.scale*game.height//2)])
    pygame.draw.rect(screen, BLACK, [game.x , game.y  , game.scale * game.width, game.scale * game.height],5) #BORDER


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()