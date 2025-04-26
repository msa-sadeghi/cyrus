import pygame
from button import Button
import pickle
import os
pygame.init()

WIDTH = 1000
HEIGHT = 600
SIDE_MARGIN = 400
BOTTOM_MARGIN = 150
MAX_COLS = 80
TILE_SIZE = 50
ROWS = HEIGHT // TILE_SIZE
scroll = 0
scroll_speed = 1
current_tile = 0
level  = 1

font = pygame.font.Font(None, 30)
text = font.render(f"Level {level}", True, (255, 255, 255))  




tile_images = [
    pygame.transform.scale(pygame.image.load(f"tiles/png/Tile/{i}.png"), (TILE_SIZE, TILE_SIZE))
    for i in range(1,17)
]
tile_images .extend( [
    pygame.transform.scale(pygame.image.load(f"tiles/png/Objects/{img}"), (TILE_SIZE, TILE_SIZE))
    for img in os.listdir("tiles/png/Objects")
])

buttons = []
col = 0
row = 0
for i in range(len(tile_images)):
    btn = Button(tile_images[i],WIDTH + col * 80 + 50, row * 80 + 80)
    buttons.append(btn)
    col += 1
    if col == 4:
        col = 0
        row += 1


world_data = []
for i in range(ROWS):
    d = [-1] * MAX_COLS
    world_data.append(d)


def draw_world():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:
                screen.blit(tile_images[world_data[i][j]], (j * TILE_SIZE - scroll, i * TILE_SIZE) )



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
save_button = Button(pygame.image.load("tiles/png/save.png"), WIDTH//2 - 150, HEIGHT + 10)
load_button = Button(pygame.image.load("tiles/png/load.png"), WIDTH//2 + 150, HEIGHT + 10)



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
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN:
                level -= 1
                if level < 1:
                    level = 1
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
    text = font.render(f"Level {level}", True, (255, 255, 255))  
    draw_bg()
    draw_grid()
    draw_world()
    pygame.draw.rect(screen, 'lightpink', (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))  # Main area
    pygame.draw.rect(screen, 'lightpink', (0, HEIGHT, WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))  # Main area
    screen.blit(text, (WIDTH + 50, 10))  # Level text
  
    for i,btn in enumerate(buttons):
        if btn.update(screen)[0]:
            current_tile = i
    pygame.draw.rect(screen, 'red', buttons[current_tile].rect, 3)
    if save_button.update(screen)[0]:
        with open(f"level{level}.dat", "wb") as f:
            pickle.dump(world_data, f)
    if load_button.update(screen)[0]:
        try:
            with open(f"level{level}.dat", "rb") as f:
                world_data = pickle.load(f)
        except FileNotFoundError:
            print("File not found")
    mouse_pos = pygame.mouse.get_pos()
    x = (mouse_pos[0] + scroll) // TILE_SIZE
    y = mouse_pos[1] // TILE_SIZE
    if pygame.mouse.get_pressed()[0] and (mouse_pos[0] < WIDTH and mouse_pos[1] < HEIGHT):
        print(x,y)
        world_data[y][x] = current_tile

    if pygame.mouse.get_pressed()[2]:
        world_data[y][x] = -1

    pygame.display.flip()   
    clock.tick(FPS)