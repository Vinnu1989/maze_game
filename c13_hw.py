import pygame
import random
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Maze")

FPS = 30
Clock = pygame.time.Clock()

player_SIZE = 20
player_x = 10
player_y = 60
player_color = ("Gold")
player_speed = 5

wall_WIDTH1 = 500
wall_HEIGHT1 = 20
wall_WIDTH2 = 20
wall_HEIGHT2 = 200

portal_WIDTH = 20
portal_HEIGHT = 50

end_WIDTH = 20
end_HEIGHT = 100

gameloop = True
while gameloop:
    player_rect = pygame.draw.rect(display_surface, player_color, (player_x, player_y, player_SIZE, player_SIZE))
    wall1_rect = pygame.draw.rect(display_surface, "black", (0, 0, 600, wall_HEIGHT1))
    wall1_rect1 = pygame.draw.rect(display_surface, "black", (0, 100, wall_WIDTH1, wall_HEIGHT1))
    wall1_rect2 = pygame.draw.rect(display_surface, "black", (100, 200, wall_WIDTH1, wall_HEIGHT1))
    wall1_rect3 = pygame.draw.rect(display_surface, "black", (0, 300, wall_WIDTH1, wall_HEIGHT1))
    wall1_rect4 = pygame.draw.rect(display_surface, "black", (100, 400, wall_WIDTH1, wall_HEIGHT1))
    wall1_rect5 = pygame.draw.rect(display_surface, "black", (0, 500, wall_WIDTH1, wall_HEIGHT1))
    wall1_rect6 = pygame.draw.rect(display_surface, "black", (0, 590, 600, 10))

    wall2_rect = pygame.draw.rect(display_surface, "black", (580, 0, wall_WIDTH2, wall_HEIGHT2))
    wall2_rect1 = pygame.draw.rect(display_surface, "black", (0, 100, wall_WIDTH2, wall_HEIGHT2))
    wall2_rect2 = pygame.draw.rect(display_surface, "black", (580, 200, wall_WIDTH2, wall_HEIGHT2))
    wall2_rect3 = pygame.draw.rect(display_surface, "black", (0, 300, wall_WIDTH2, wall_HEIGHT2))
    wall2_rect4 = pygame.draw.rect(display_surface, "black", (580, 400, wall_WIDTH2, wall_HEIGHT2))

    red_portal = pygame.draw.rect(display_surface, (255, 0, 0), (525, 45, portal_WIDTH, portal_HEIGHT))
    orange_portal = pygame.draw.rect(display_surface, (255, 165, 0), (75, 145, portal_WIDTH, portal_HEIGHT))
    yellow_portal = pygame.draw.rect(display_surface, (255, 255, 0), (525, 245, portal_WIDTH, portal_HEIGHT))
    green_portal = pygame.draw.rect(display_surface, (0, 255, 0), (75, 345, portal_WIDTH, portal_HEIGHT))
    blue_portal = pygame.draw.rect(display_surface, (0, 0, 255), (525, 445, portal_WIDTH, portal_HEIGHT))

    end_wall = pygame.draw.rect(display_surface, (128, 0, 128), (0, 500, end_WIDTH, end_HEIGHT)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
                player_x = player_x - 10
        if event.key == pygame.K_RIGHT:
                player_x = player_x + 10
        if event.key == pygame.K_UP:
                player_y = player_y - 10
        if event.key == pygame.K_DOWN:
                player_y = player_y + 10        

    if player_rect.colliderect((red_portal)):
                player_color = (255, 0, 0)
    if player_rect.colliderect((orange_portal)):
                player_color = (255, 165, 0)
    if player_rect.colliderect((yellow_portal)):
                player_color = (255, 255, 0)
    if player_rect.colliderect((green_portal)):
                player_color = (0, 255, 0)
    if player_rect.colliderect((blue_portal)):
                player_color = (0, 0, 255)

    if player_rect.colliderect((end_wall)):
                pygame.quit()

    if player_rect.collidelistall((wall1_rect, wall1_rect1, wall1_rect2, wall1_rect3, wall1_rect4, wall1_rect5, wall1_rect6)):
                player_x = 10
                player_y = 30
                player_color = "Gold"

    if player_rect.collidelistall((wall2_rect, wall2_rect1, wall2_rect2, wall2_rect3, wall2_rect4)):
                player_x = 10
                player_y = 30
                player_color = "Gold"

    display_surface.fill((255, 255, 255))
    pygame.draw.rect(display_surface, player_color, player_rect)
    pygame.draw.rect(display_surface, "Blue", wall1_rect)
    pygame.draw.rect(display_surface, "orange", wall1_rect1)
    pygame.draw.rect(display_surface, "yellow", wall1_rect2)
    pygame.draw.rect(display_surface, "red", wall1_rect3)
    pygame.draw.rect(display_surface, "pink", wall1_rect4)
    pygame.draw.rect(display_surface, "green", wall1_rect5)
    pygame.draw.rect(display_surface, "orange", wall1_rect6)

    pygame.draw.rect(display_surface, (0, 0, 0), wall2_rect)
    pygame.draw.rect(display_surface, (0, 0, 0), wall2_rect1)
    pygame.draw.rect(display_surface, (0, 0, 0), wall2_rect2)
    pygame.draw.rect(display_surface, (0, 0, 0), wall2_rect3)
    pygame.draw.rect(display_surface, (0, 0, 0), wall2_rect4)

    pygame.draw.rect(display_surface, (255, 0, 0), red_portal)
    pygame.draw.rect(display_surface, (255, 165, 0), orange_portal)
    pygame.draw.rect(display_surface, (255, 255, 0), yellow_portal)
    pygame.draw.rect(display_surface, (0, 255, 0), green_portal)
    pygame.draw.rect(display_surface, (0, 0, 255), blue_portal)

    pygame.draw.rect(display_surface, (128, 0, 128), end_wall)

    Clock.tick(FPS)
    pygame.display.flip()
pygame.quit()    
