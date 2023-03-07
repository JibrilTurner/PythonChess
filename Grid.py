import pygame

CELL_SIZE = 80
BOARD_SIZE = CELL_SIZE * 8

BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
LIGHTORANGE = (255, 213, 128)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Chess")

font = pygame.font.SysFont(None, 32)

for i in range(8):
    for j in range(8):
        x = j * CELL_SIZE
        y = i * CELL_SIZE
        color = LIGHTORANGE if (i+j) % 2 == 0 else WHITE
        pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
        if i == 0:
            # label the top row with letters
            label = font.render(chr(ord('a')+j), True, BLUE)
            screen.blit(label, (x + CELL_SIZE/2 - label.get_width()/2, y - 30))
        if j == 0:
            # label the left column with numbers
            label = font.render(str(8-i), True, BLUE)
            screen.blit(label, (x - 30, y + CELL_SIZE/2 - label.get_height()/2))

        # label each tile with its coordinates
        label = font.render(chr(ord('a')+j)+str(8-i), True, GRAY)
        screen.blit(label, (x + CELL_SIZE/2 - label.get_width()/2, y + CELL_SIZE/2 - label.get_height()/2))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
