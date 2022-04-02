import spencerMain as main
import pygame

# Initializes the board on screen and gets the initial bomb counts around each tile
main.neighborCount()
main.displayBoard()

# Game loop
while main.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or main.clickedBomb or main.blankCount == main.tileCount:
            main.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # LEFT CLICK
            if event.button == 1:
                main.updateBoard(int(pos[0] / 50), int(pos[1] / 50))
                if main.board[int(pos[1] / 50)][int(pos[0] / 50)][0] == 19:
                    main.clickedBomb = True
                    # RIGHT CLICK
            if event.button == 3:
                main.flag(int(pos[0] / 50), int(pos[1] / 50))
    pygame.display.flip()

# Ends the game with a GAME OVER message
if main.clickedBomb:
    TEXT = "GAME OVER"
    for row in main.board:
        for tile in row:
            if tile[0] == 9:
                tile[0] += 20
    main.displayBoard()
    pygame.display.flip()
    pygame.time.delay(2000)
    0
# Ends the game with a WINNER message
else:
    TEXT = "WINNER"
myfont = pygame.font.SysFont('Helvetica', 40, bold=True)
TEXT_ONE = myfont.render(TEXT, True, (255,0,0), (255,255,255,))
TEXT_ONERect = TEXT_ONE.get_rect()
TEXT_ONERect.center = (250, 250)
main.screen.blit(TEXT_ONE, TEXT_ONERect)
pygame.display.flip()
pygame.time.delay(2000)
