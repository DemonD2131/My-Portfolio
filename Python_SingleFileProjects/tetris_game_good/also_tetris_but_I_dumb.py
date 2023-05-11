import pygame
import random

#classes
class Figure:
    x = 0
    y = 0
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.rotation = 0
        self.color = random.randint(1, len(colors) - 1)
    def image(self):
        return self.figures[self.type][self.rotation]
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
class Tetris:
    level = 2
    score = 0
    height = 0
    width = 0
    field = []
    state = "start"
    x = 100
    y = 60
    zoom = 20
    figure = None
    nextfigure = None
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
    def new_figure(self):
        if self.nextfigure is not None:
            self.figure = self.nextfigure
            self.nextfigure = Figure(3, 0)
        else:
            self.figure = Figure(3, 0)
            self.nextfigure = Figure(3, 0)
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.figure.image():
                    if i + self.figure.y > self.height -1 or j + self.figure.x > self.width - 1 or j + self.figure.x < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection
    def break_lines(self):
        lines = 0
        for i in range(1, self.height): #height is 20 
            zeros = 0
            for j in range(self.width): #width is 10 
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1): #lets assume i is 1
                    for j in range(self.width): #0-9
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines **2
    def freeze(self):
        for i in range(4):
            for j in range(4):
                p = i * 4 + j 
                if p in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()
    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()
    def go_side(self,dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x
    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

#variables

pygame.init()

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

game = Tetris(20, 10)
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

done = False
clock = pygame.time.Clock()
fps = 25
counter = 0
pressing_down = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

#main***********************


while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False
    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]], [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i*4 +j
                
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color], [game.x + game.zoom * (j + game.figure.x) +1, game.y + game.zoom * (i + game.figure.y) + 1, game.zoom - 2, game.zoom - 2])
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [(game.x + game.zoom-2  + (game.zoom * game.width)) + game.zoom * j, game.y + game.zoom * i, game.zoom - 2, game.zoom -2],1)
    if game.nextfigure is not None:
        for i in range(4):
            for j in range(4):
                p = i*4 +j
                if p in game.nextfigure.image():
                    pygame.draw.rect(screen, colors[game.nextfigure.color], [(game.x + game.zoom-2  + (game.zoom * game.width)) + game.zoom * j, game.y + game.zoom * i, game.zoom - 2, game.zoom -2])
    
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    
    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()