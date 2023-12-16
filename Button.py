import pygame as pg
pg.init()


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pg.image.load(hover_image_path).convert_alpha()
            self.hover_image = pg.transform.scale(self.hover_image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)
        else:
            self.sound = None

        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect)

        font = pg.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))
