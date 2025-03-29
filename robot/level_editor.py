import pygame

WIDTH = 1000
HEIGHT = 640
SIDE_MARGIN = 300
BOTTOM_MARGIN = 100
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
pygame.display.set_caption("Level Editor")

bg_image = pygame.image.load("./tiles/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
def draw_bg():
    bg_width = bg_image.get_width()
    for i in range(4):
        screen.blit(bg_image, (i * bg_width, 0))


clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    draw_bg()
    pygame.draw.rect(screen, 'lightpink', (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))  # Main area
    pygame.draw.rect(screen, 'lightpink', (0, HEIGHT, WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))  # Main area
    pygame.display.flip()   
    clock.tick(FPS)