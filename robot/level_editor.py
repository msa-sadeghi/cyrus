import pygame
from button import Button
pygame.init()

WIDTH = 1000
HEIGHT = 600
SIDE_MARGIN = 300
BOTTOM_MARGIN = 100
MAX_COLS = 80
TILE_SIZE = 50
ROWS = HEIGHT // TILE_SIZE
scroll = 0
scroll_speed = 1

tile_images = [
    pygame.transform.scale(pygame.image.load(f"tiles/png/Tile/{i}.png"), (TILE_SIZE, TILE_SIZE))
    for i in range(1,17)
]

buttons = []
col = 0
row = 0
for i in range(len(tile_images)):
    btn = Button(tile_images[i],WIDTH + col * 80 + 50, row * 80 + 80)
    buttons.append(btn)
    col += 1
    if col == 3:
        col = 0
        row += 1


def draw_button():
    for btn in buttons:
        screen.blit(btn.image, btn.rect)


scroll_left, scroll_right = False, False
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
pygame.display.set_caption("Level Editor")

bg_image = pygame.image.load("./tiles/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
def draw_bg():
    global bg_width
    bg_width = bg_image.get_width()
    for i in range(4):
        screen.blit(bg_image, (i * bg_width - scroll, 0))

def draw_grid():
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, 'gray', (i * TILE_SIZE - scroll, 0), (i * TILE_SIZE - scroll, HEIGHT))
    for i in range(ROWS + 1):
        pygame.draw.line(screen, 'gray', (0, i *  TILE_SIZE), (WIDTH, i *  TILE_SIZE))
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                scroll_left  = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left  = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed
    
    if scroll_right and scroll < bg_width * 3:
        scroll += 5 * scroll_speed  
    if (scroll_left and scroll < 0) or (scroll_right and scroll > bg_width * 3):
        scroll = 0 
    screen.fill((0, 0, 0))
    draw_bg()
    draw_grid()
    pygame.draw.rect(screen, 'lightpink', (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))  # Main area
    pygame.draw.rect(screen, 'lightpink', (0, HEIGHT, WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))  # Main area
    draw_button()
    pygame.display.flip()   
    clock.tick(FPS)