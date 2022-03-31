import pygame
import random

bombArray = []
clickedBomb = False
running = True 
color = (255,0,0)
blankCount = 100
tileCount = 0

# Renders all images
pygame.init()
pygame.display.set_caption("Minesweeper")
TILE = pygame.transform.scale(pygame.image.load('tile.png'), (50, 50))
EMPTY = pygame.transform.scale(pygame.image.load('empty.png'), (50, 50))
BOMB = pygame.transform.scale(pygame.image.load('bomb.png'), (50, 50))
FLAG = pygame.transform.scale(pygame.image.load('flag.png'), (50, 50))
ONE = pygame.transform.scale(pygame.image.load('1.png'), (50, 50))
TWO = pygame.transform.scale(pygame.image.load('2.png'), (50, 50))
THREE = pygame.transform.scale(pygame.image.load('3.png'), (50, 50))
FOUR = pygame.transform.scale(pygame.image.load('4.png'), (50, 50))
FIVE = pygame.transform.scale(pygame.image.load('5.png'), (50, 50))
SIX = pygame.transform.scale(pygame.image.load('6.png'), (50, 50))
SEVEN = pygame.transform.scale(pygame.image.load('7.png'), (50, 50))
EIGHT = pygame.transform.scale(pygame.image.load('8.png'), (50, 50))

# Creates a 10 x 10 game board... ONLY 10x10 WORKS!
size = 10
screen = pygame.display.set_mode([50 * size, 50 * size])
screen.fill((255, 255, 255))
board = []
for row in range(size):
    row = []
    for col in range(size):
        tile = random.choices((0,9),((0.9,0.1)))
        if tile[0] == 9:
            blankCount -= 1
        row.append(tile)
    board.append(row)

# This counts the number of bombs around each tile
def neighborCount():
    rowCount = 0
    for row in board:
        colCount = 0
        for tile in row:
            if tile == [9] and colCount < 9:
                if board[rowCount][colCount + 1][0] < 9:
                    board[rowCount][colCount + 1][0] += 1
            if tile == [9] and rowCount < 9:
                if board[rowCount + 1][colCount][0] < 9:
                    board[rowCount + 1][colCount][0] += 1
            if tile == [9] and colCount > 0:
                if board[rowCount][colCount - 1][0] < 9:
                    board[rowCount][colCount - 1][0] += 1
            if tile == [9] and rowCount > 0:
                if board[rowCount - 1][colCount][0] < 9:
                    board[rowCount - 1][colCount][0] += 1
            if tile == [9] and colCount < 9 and rowCount < 9:
                if board[rowCount + 1][colCount + 1][0] < 9:
                    board[rowCount + 1][colCount + 1][0] += 1
            if tile == [9] and rowCount > 0 and colCount > 0:
                if board[rowCount - 1][colCount - 1][0] < 9:
                    board[rowCount - 1][colCount - 1][0] += 1
            if tile == [9] and rowCount > 0 and colCount < 9:
                if board[rowCount - 1][colCount + 1][0] < 9:
                    board[rowCount - 1][colCount + 1][0] += 1
            if tile == [9] and rowCount < 9 and colCount > 0:
                if board[rowCount + 1][colCount - 1][0] < 9:
                    board[rowCount + 1][colCount - 1][0] += 1
            colCount += 1
        rowCount += 1

# This is the board displayer when a the board doesn't have the blank recursion happening and records the click
def displayBoard():
    rowCount = 0
    for row in board:
        colCount = 0
        for tile in row:
            if tile[0] < 10:
                screen.blit(TILE, (colCount * 50, rowCount * 50))
            elif tile == [10]:
                screen.blit(EMPTY, (colCount * 50, rowCount * 50))
            elif tile == [11]:
                screen.blit(ONE, (colCount * 50, rowCount * 50))
            elif tile == [12]:
                screen.blit(TWO, (colCount * 50, rowCount * 50))
            elif tile == [13]:
                screen.blit(THREE, (colCount * 50, rowCount * 50))
            elif tile == [14]:
                screen.blit(FOUR, (colCount * 50, rowCount * 50))
            elif tile == [15]:
                screen.blit(FIVE, (colCount * 50, rowCount * 50))
            elif tile == [16]:
                screen.blit(SIX, (colCount * 50, rowCount * 50))
            elif tile == [17]:
                screen.blit(SEVEN, (colCount * 50, rowCount * 50))
            elif tile == [18]:
                screen.blit(EIGHT, (colCount * 50, rowCount * 50))
            elif tile == [29]:
                screen.blit(EMPTY, (colCount * 50, rowCount * 50))
                screen.blit(BOMB, (colCount * 50, rowCount * 50))
            elif tile == [19]:
                screen.blit(EMPTY, (colCount * 50, rowCount * 50))
                pygame.draw.rect(screen, color, pygame.Rect(colCount * 50, rowCount * 50, 50, 50))
                screen.blit(BOMB, (colCount * 50, rowCount * 50))
            elif tile == [20]:
                screen.blit(FLAG, (colCount * 50, rowCount * 50))
            else:
                screen.blit(EMPTY, (colCount * 50, rowCount * 50))
            colCount += 1
        rowCount += 1

# This updates the board based on the click location
def updateBoard(clickX, clickY):
    global tileCount
    if board[clickY][clickX][0] < 10:
        board[clickY][clickX][0] += 10
    if board[clickY][clickX][0] == 10:
        blankRecursion(clickX, clickY)
    tileCount += 1
    displayBoard()


# This starts when you click a blank tile and will keep clicking all surrounding blank tiles until it runs into a number and counts the number of clicks
def blankRecursion(clickX, clickY):
    global tileCount
    if clickX < 9 and clickX > 0 and clickY < 9 and clickY > 0:
        if board[clickY + 1][clickX][0] < 9:
            board[clickY + 1][clickX][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX][0] == 10:
                blankRecursion(clickX, clickY + 1)
        if board[clickY][clickX + 1][0] < 9:
            board[clickY][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY)
        if board[clickY - 1][clickX][0] < 9:
            board[clickY - 1][clickX][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX][0] == 10:
                blankRecursion(clickX, clickY - 1)
        if board[clickY][clickX - 1][0] < 9:
            board[clickY][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY)
        if board[clickY + 1][clickX + 1][0] < 9:
            board[clickY + 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY + 1)
        if board[clickY + 1][clickX - 1][0] < 9:
            board[clickY + 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY + 1)
        if board[clickY - 1][clickX + 1][0] < 9:
            board[clickY - 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY - 1)
        if board[clickY - 1][clickX - 1][0] < 9:
            board[clickY - 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY - 1)
    elif clickX == 9 and clickY == 9:
        if board[clickY - 1][clickX][0] < 9:
            board[clickY - 1][clickX][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX][0] == 10:
                blankRecursion(clickX, clickY - 1)
        if board[clickY][clickX - 1][0] < 9:
            board[clickY][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY)
        if board[clickY - 1][clickX - 1][0] < 9:
            board[clickY - 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY - 1)
    elif clickX == 9 and clickY == 0:
        if board[clickY + 1][clickX][0] < 9:
            board[clickY + 1][clickX][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX][0] == 10:
                blankRecursion(clickX, clickY + 1)

        if board[clickY][clickX - 1][0] < 9:
            board[clickY][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY)
        if board[clickY + 1][clickX - 1][0] < 9:
            board[clickY + 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY + 1)
    elif clickX == 0 and clickY == 9:
        if board[clickY][clickX + 1][0] < 9:
            board[clickY][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY)
        if board[clickY - 1][clickX][0] < 9:
            board[clickY - 1][clickX][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX][0] == 10:
                blankRecursion(clickX, clickY - 1)
        if board[clickY - 1][clickX + 1][0] < 9:
            board[clickY - 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY - 1)
    elif clickX == 0 and clickY == 0:
        if board[clickY + 1][clickX][0] < 9:
            board[clickY + 1][clickX][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX][0] == 10:
                blankRecursion(clickX, clickY + 1)
        if board[clickY][clickX + 1][0] < 9:
            board[clickY][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY)
        if board[clickY + 1][clickX + 1][0] < 9:
            board[clickY + 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY + 1)
    elif clickY == 9:
        if board[clickY][clickX + 1][0] < 9:
            board[clickY][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY)
        if board[clickY - 1][clickX][0] < 9:
            board[clickY - 1][clickX][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX][0] == 10:
                blankRecursion(clickX, clickY - 1)
        if board[clickY][clickX - 1][0] < 9:
            board[clickY][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY)
        if board[clickY - 1][clickX + 1][0] < 9:
            board[clickY - 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY - 1)
        if board[clickY - 1][clickX - 1][0] < 9:
            board[clickY - 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY - 1)
    elif clickX == 9:
        if board[clickY + 1][clickX][0] < 9:
            board[clickY + 1][clickX][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX][0] == 10:
                blankRecursion(clickX, clickY + 1)
        if board[clickY - 1][clickX][0] < 9:
            board[clickY - 1][clickX][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX][0] == 10:
                blankRecursion(clickX, clickY - 1)
        if board[clickY][clickX - 1][0] < 9:
            board[clickY][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY)
        if board[clickY + 1][clickX - 1][0] < 9:
            board[clickY + 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY + 1)
        if board[clickY - 1][clickX - 1][0] < 9:
            board[clickY - 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY - 1)
    elif clickY == 0:
        if board[clickY + 1][clickX][0] < 9:
            board[clickY + 1][clickX][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX][0] == 10:
                blankRecursion(clickX, clickY + 1)
        if board[clickY][clickX + 1][0] < 9:
            board[clickY][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY)
        if board[clickY][clickX - 1][0] < 9:
            board[clickY][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY)
        if board[clickY + 1][clickX + 1][0] < 9:
            board[clickY + 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY + 1)
        if board[clickY + 1][clickX - 1][0] < 9:
            board[clickY + 1][clickX - 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX - 1][0] == 10:
                blankRecursion(clickX - 1, clickY + 1)
    elif clickX == 0:        
        if board[clickY + 1][clickX][0] < 9:
            board[clickY + 1][clickX][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX][0] == 10:
                blankRecursion(clickX, clickY + 1)
        if board[clickY][clickX + 1][0] < 9:
            board[clickY][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY)
        if board[clickY - 1][clickX][0] < 9:
            board[clickY - 1][clickX][0] += 10
            tileCount += 1
            if board[clickY - 1][clickX][0] == 10:
                blankRecursion(clickX, clickY - 1)
        if board[clickY + 1][clickX + 1][0] < 9:
            board[clickY + 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY + 1)
        if board[clickY - 1][clickX + 1][0] < 9:
            board[clickY - 1][clickX + 1][0] += 10
            tileCount += 1
            if board[clickY + 1][clickX + 1][0] == 10:
                blankRecursion(clickX + 1, clickY - 1)

# Toggles the flagged tiles (Flagging a tile will lock it)  
def flag(clickX, clickY):
    if board[clickY][clickX][0] < 10:
        board[clickY][clickX][0] = 20
    elif board[clickY][clickX][0] == 20:
        board[clickY][clickX][0] = 0
    displayBoard()
# Initializes the board on screen and gets the initial bomb counts around each tile
neighborCount()     
displayBoard()

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or clickedBomb or blankCount == tileCount:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # LEFT CLICK
            if event.button == 1:
                updateBoard(int(pos[0] / 50), int(pos[1] / 50))
                if board[int(pos[1] / 50)][int(pos[0] / 50)][0] == 19:
                    clickedBomb = True
                    # RIGHT CLICK
            if event.button == 3:
                flag(int(pos[0] / 50), int(pos[1] / 50))
    pygame.display.flip()

# Ends the game with a GAME OVER message
if clickedBomb:
    TEXT = "GAME OVER"
    for row in board:
        for tile in row:
            if tile[0] == 9:
                tile[0] += 20
    displayBoard()
    pygame.display.flip()
    pygame.time.delay(2000)
# Ends the game with a WINNER message
else:
    TEXT = "WINNER"
myfont = pygame.font.SysFont('Helvetica', 40, bold=True)
TEXT_ONE = myfont.render(TEXT, True, (255,0,0), (255,255,255,))
TEXT_ONERect = TEXT_ONE.get_rect()
TEXT_ONERect.center = (250, 250)
screen.blit(TEXT_ONE, TEXT_ONERect)
pygame.display.flip()
pygame.time.delay(2000)