#Dominic Rondeau v1.0
#Conways game of life very cool
#Conways game of life made in pygame outputted pretty intuitively, This took me forever to do the "update" function I was being very silly for a while and forgot insert function existed
#Started May 27, 2022
#Ended May 30, 2022
import pygame
LIVE = 1
DEAD = 0
def buildArray(a, row, col):
    a = []
    for i in range(row):
        a.append([])
    for r in range(len(a)):
        for c in range(col):
            a[r].append(0)
    return a
def printIt(a):
    for r in range(len(a)):
        for c in range(len(a[r])):
            print(a[r][c], end=" ")
        print("")
    print("")
class Cell():
    state = LIVE 
    liveNeighbors = 0
    def __init__(self,x,y,state,field):
        self.x = x
        self.y = y
        self.state = state
        self.field = field
        self.height = len(self.field)
        self.width = len(self.field[0])
    def checker(self):
        self.liveNeighbors = 0

        #print("X: " + str(self.x) + " Y: " + str(self.y))
        if self.x+1 < self.width: #totheright
            

            if self.field[self.y][self.x+1] == LIVE:
                self.liveNeighbors += 1
            #print("RIght yes")

        if self.x-1 > -1: #totheleft

            if self.field[self.y][self.x-1] == LIVE:
                self.liveNeighbors += 1
            #print("Left yes")
        
        if self.y+1 < self.height: #tothebottom

            if self.field[self.y+1][self.x] == LIVE:
                self.liveNeighbors += 1
            #print("Down yes")
        
        if self.y-1 > -1: #tothetop

            if self.field[self.y-1][self.x] == LIVE:
                self.liveNeighbors += 1
            #print("Up yes")
        
        if self.y+1 < self.height and self.x+1 < self.width: #tothe bottomright
            if self.field[self.y+1][self.x+1] == LIVE:
                self.liveNeighbors += 1
            #print("down Right yes")
        
        if self.y+1 < self.height and self.x-1 > -1: #tothe bottom left

            if self.field[self.y+1][self.x-1] == LIVE:
                self.liveNeighbors += 1
            #print("Down left ye")
        
        if self.y-1 > -1 and self.x-1 > -1: #tothe top left

            if self.field[self.y-1][self.x-1] == LIVE:
                self.liveNeighbors += 1
            #print("Top left yes")

        if self.y-1 > -1 and self.x+1 < self.width: #tothe top right

            if self.field[self.y-1][self.x+1] == LIVE:
                self.liveNeighbors += 1
            #print("Top right yes")
        #print(self.liveNeighbors)
        
class Life():
    board = []
    scale = 40
    x = 20
    y = 20
    highestx = 0
    highesty = 0
    
    height = 0
    width = 0
    steps = 0
    def __init__(self,startingList,steps): #list will be tuples of coordinates
        self.steps = steps
        self.startingList = []
        self.lowestx = startingList[0][0]
        self.lowesty = startingList[0][1]
        #find which x and which y is the highest so we know how many rows and collumns we need to build and initialize
        for i in range(len(startingList)):
            if startingList[i][0] >= self.highestx:
                self.highestx = startingList[i][0]
            if startingList[i][1] >= self.highesty:
                self.highesty = startingList[i][1]
        for i in range(len(startingList)):
            if startingList[i][0] <= self.lowestx:
                self.lowestx = startingList[i][0]
            if startingList[i][1] <= self.lowesty:
                self.lowesty = startingList[i][1]
        self.highestx -= self.lowestx
        self.highesty -= self.lowesty
        for e in range(len(startingList)):
            self.startingList.append((startingList[e][0]-self.lowestx,startingList[e][1]-self.lowesty))
        self.board = buildArray(self.board,self.highesty+1,self.highestx+1)
        for e in range(len(self.startingList)):
            self.board[self.startingList[e][1]][self.startingList[e][0]] = LIVE
        #use that information after basic board is setup to get some basic values
        self.height = len(self.board)
        self.width = len(self.board[0])
    def update(self):
        valid = False
        while valid == False:
            self.leftLive = False
            self.rightLive = False
            self.topLive = False
            self.bottomLive = False
            self.topDead = True

            self.height = len(self.board)
            self.width = len(self.board[0])

            for i in range(self.height):
                if self.board[i][0] == LIVE:
                    self.leftLive = True
                if self.board[i][self.width-1] == LIVE:
                    self.rightLive = True
                for j in range(self.width):
                    if self.board[0][j] == LIVE:
                        self.topLive = True
                    if self.board[self.height-1][j] == LIVE:
                        self.bottomLive = True
                    if self.board[1][j] == LIVE or self.board[0][j] == LIVE:
                        self.topDead = False
            
            if self.leftLive == True:
                for i in range(self.height):
                    self.board[i].insert(0, 0)
                self.width = len(self.board[0])
            if self.rightLive == True:
                for i in range(self.height):
                    self.board[i].append(0)
                self.width = len(self.board[0])
            if self.topLive == True:
                dummyList = []
                for j in range(self.width):
                    dummyList.append(0)
                self.board.insert(0,dummyList)
                self.height = len(self.board)
            if self.bottomLive == True:
                dummyList = []
                for j in range(self.width):
                    dummyList.append(0)
                self.board.append(dummyList)
                self.height = len(self.board)
            if self.topDead == True:
                dummyList = []
                for j in range(self.width):
                    dummyList.append(0)
                self.board.remove(dummyList)
                self.height = len(self.board)
                
            
            if self.topDead == False and self.bottomLive == False and self.topLive == False and self.rightLive == False and self.leftLive == False:
                valid = True
            
            

        self.cells = []
        self.fakeBoard = self.board.copy()
        for i in range(self.height):
            self.cells.append([])
            
            for j in range(self.width):
                self.cells[i].append(Cell(j,i,self.fakeBoard[i][j],self.fakeBoard))
                self.cells[i][j].checker()






    def progress(self):
        
        for i in range(len(self.cells)):
            
            for j in range(len(self.cells[i])):
                if self.cells[i][j].state == DEAD:
                    if self.cells[i][j].liveNeighbors == 3:
                        self.board[i][j] = LIVE
                elif self.cells[i][j].state == LIVE:
                    if self.cells[i][j].liveNeighbors < 2 or self.cells[i][j].liveNeighbors > 3:
                        self.board[i][j] = DEAD
                
        
        
        self.steps -= 1

def positionGetter(pos):
    ex = pos[0]
    ey = pos[1]
    spot = None
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

pygame.init()


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
size = (800, 800)
screen = pygame.display.set_mode(size)

startList = [(5,30),(4,30),(3,29),(6,30),(7,30),(2,27),(4,29),(1,28)]
game = Life(startList, 30)

clock = pygame.time.Clock()
pygame.display.set_caption("Game of life simulation :)")
done = False
clicked_pos = None
while done is False:
    game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = positionGetter(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.steps > 0:
                    game.progress()
    
    if clicked_pos is not None:
        game.board[clicked_pos[1]][clicked_pos[0]] = 1
        clicked_pos = None
    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', game.scale, True, False)
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, BLACK, [game.x + (game.scale * j), game.y + (game.scale * i), game.scale -2, game.scale -2])#Game tiles
            if i < len(game.cells) and j < len(game.cells[0]):
                textD = font.render(str(game.cells[i][j].liveNeighbors), True, BLUE)
                screen.blit(textD, [game.x + (game.scale*j) + (game.scale//5), game.y + (game.scale * i)+(game.scale//5)])
            if game.board[i][j] == 1:
                text = font.render("*", True, WHITE)
            elif game.board[i][j] == 0:
                text = font.render(".", True, WHITE)
            screen.blit(text, [game.x + (game.scale*j), game.y + (game.scale * i)])
    pygame.display.flip()
    clock.tick(fps)

pygame.quit