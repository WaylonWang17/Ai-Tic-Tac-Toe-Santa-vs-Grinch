import pygame

pygame.init()

#screen dimensions
width = 550
height = 720

#display screen and caption
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("wordle infinite trainer")

#set fps and timer
fps = 60
timer = pygame.time.Clock()
turn = 0
letter = pygame.font.SysFont("timesnewroman", 56)

#set rgb colours
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

board = [["1"," "," "," "," "], ["2"," "," "," "," "], [" "," ","3"," "," "], [" "," "," ","4"," "], [" "," "," "," ","6"], [" "," "," "," "," "]]

def drawboard():
    global turn
    global board
    for i in range(len(board)-1):
        for j in range(len(board)):
            pygame.draw.rect(screen, white, [i*100+40, j*100+30, 75, 75], 3)
            text = letter.render(board[j][i], True, white)
            screen.blit(text, (i*100+65, j*100+40))

    pygame.draw.rect(screen, green, [5, turn*100 + 20,  width - 10, 90], 3, 5)

#start the program
running = True
while running:
    timer.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawboard()
    pygame.display.update()

pygame.quit()

