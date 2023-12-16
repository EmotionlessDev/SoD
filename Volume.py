import pygame
pygame.init()


class VolumeSlider:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = pygame.mixer.music.get_volume()
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.slider_rect = pygame.Rect(self.rect.left + int(self.value * width) - 5, self.rect.top, 10, self.height)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.update_value(event.pos)

        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            self.update_value(event.pos)

    def update_value(self, mouse_pos):
        x = max(self.rect.left, min(self.rect.right, mouse_pos[0]))
        self.slider_rect.left = x - self.slider_rect.width // 2
        self.value = (x - self.rect.left) / self.width
        pygame.mixer.music.set_volume(self.value)

    def draw(self, screen):
        radius = 40
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=radius)
        pygame.draw.rect(screen, (0, 0, 0), self.slider_rect)
        center_x = self.slider_rect.center[0]

        pygame.gfxdraw.aacircle(screen, center_x, self.y, self.height // 2, (0, 0, 0))
        pygame.gfxdraw.filled_circle(screen, center_x, self.y, self.height // 2, (0, 0, 0))
