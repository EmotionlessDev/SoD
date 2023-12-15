import pygame
from sys import exit
from hero.Player import Player
from ground.Ground import Ground
from canvas import load_image
from enemies.Skeleton import Skeleton
from import_sprite import import_sprite

# Initialize Pygame
pygame.init()
# main screen
width_screen, height_screen = 1280, 720  # размер экрана
screen = pygame.display.set_mode(
    (width_screen, height_screen), pygame.RESIZABLE
)  # создание окна
screen_size = screen.get_size()

virtual_surface = pygame.Surface(
    (width_screen, height_screen)
)  # вертуальное пространство

pygame.display.set_caption("Shadow of Desolation")  # создание заголовка окна
stone_wall = load_image(
    r"images/imgonline-com-ua-Resize-4mpm1BvVfOwb16l.jpg"
)  # задний фон
# FPS
FPS = 60
clock = pygame.time.Clock()
# Ground
ground_sprite = Ground("./sprites/ground.png", 0, height_screen)
ground_sprite2 = Ground("./sprites/ground.png", 300, height_screen / 2)
ground_group = pygame.sprite.Group()
ground_group.add(ground_sprite)
ground_group.add(ground_sprite2)
# Player
player = pygame.sprite.GroupSingle()
player.add(Player("./sprites/character.png", width_screen, height_screen - 200))
# Skeleton
skeleton_group = pygame.sprite.Group()
skeleton1 = Skeleton(
    import_sprite("./sprites/Skeleton/Idle"),
    import_sprite("./sprites/Skeleton/Attack/"),
    import_sprite("./sprites/Skeleton/Move/"),
    50,
    50,
    player,
)
skeleton_group.add(skeleton1)

# Start the main loop
while True:
    # Check for events
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            exit()
        # resize window
        if event.type == pygame.VIDEORESIZE:
            screen_size = event.size
        # Check for the fullscreen toggle event
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            # Toggle fullscreen mode
            pygame.display.toggle_fullscreen()
    # background
    stone_wall = pygame.transform.scale(
        stone_wall, virtual_surface.get_size()
    )  # установление соответсвия размеров фона и окна
    virtual_surface.blit(
        stone_wall, [0, 0, width_screen, height_screen]
    )  # установка заднего фона

    # ground
    ground_collisions = pygame.sprite.spritecollide(player.sprite, ground_group, False)
    ground_group.draw(virtual_surface)
    # player
    player.draw(virtual_surface)
    player.update(ground_collisions)
    # Skeleton test
    skeleton_group.draw(virtual_surface)
    skeleton_group.update()
    # update display
    scaled_surface = pygame.transform.scale(
        virtual_surface, screen_size
    )  # адаптация вертуального пространства под размер окна
    pygame.display.flip()
    screen.blit(scaled_surface, (0, 0))
    # Set ticks (fps)
    clock.tick(FPS)
