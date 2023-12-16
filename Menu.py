import pygame as pg
from Button import Button
from Volume import VolumeSlider
import sys
pg.init()


class Menu:
    def __init__(self, bg_image, menu_font, surface, text_y):
        self.bg_image = pg.image.load(bg_image)
        self.menu_font = menu_font
        self.surface = surface
        self.text_y = text_y

    def fade(self):
        fade_alpha = 0

        fade_surface = pg.Surface((self.surface.get_width(), self.surface.get_height()))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        self.surface.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255


class MainMenu(Menu):
    def __init__(self, bg_image, menu_font, surface, text_y, width_btn, height_btn, menu_windows):
        super().__init__(bg_image, menu_font, surface, text_y)
        self.width_btn = width_btn
        self.menu_windows = menu_windows

        self.start_button = Button(self.surface.get_width() // 2 - width_btn // 2, 150, width_btn, height_btn,
                                   "Новая игра", r"menu/button_img.png",
                                   r"menu/button_img.png", r"sounds/button_click.mp3")
        self.settings_button = Button(self.surface.get_width() // 2 - width_btn // 2, 250, width_btn, height_btn,
                                      "Настройки", r"menu/button_img.png",
                                      r"menu/button_img.png", r"sounds/button_click.mp3")
        self.exit_button = Button(self.surface.get_width() // 2 - width_btn, 350, width_btn, height_btn,
                                  "Выйти", r"menu/button_img.png",
                                  r"menu/button_img.png", r"sounds/button_click.mp3")

        self.text_surface = menu_font.render("MENU", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(width_btn // 2, self.text_y))

    def controls(self):
        buttons = [self.start_button,  self.settings_button, self.exit_button]

        for event in pg.event.get():
            if event.type == pg.USEREVENT and event.button == self.start_button:
                self.fade()
                #opening

            if event.type == pg.USEREVENT and event.button == self.settings_button:
                self.fade()
                self.menu_windows.draw()

            if event.type == pg.USEREVENT and event.button == self.exit_button:
                sys.exit()

            for btn in buttons:
                btn.handle_event(event)

    def draw(self):
        self.surface.blit(self.bg_image, (0, 0))
        self.surface.blit(self.text_surface, self.text_rect)
        self.controls()


class SettingsMenu(Menu):
    def __init__(self, bg_image, menu_font, surface, text_y, width_btn, height_btn, menu_windows):
        super().__init__(bg_image, menu_font, surface, text_y)
        self.width_btn = width_btn
        self.main_menu, self.audio_menu = menu_windows

        self.audio_button = Button(self.surface.get_width() // 2 - width_btn // 2, 150, width_btn, height_btn,
                                   " Аудио", r"menu/button_img.png",
                                   r"menu/button_img.png", r"sounds/button_click.mp3")
        self.back_button = Button(self.surface.get_width() // 2 - width_btn // 2, 350, width_btn, height_btn,
                                  "Выход", r"menu/button_img.png",
                                  r"menu/button_img.png", r"sounds/button_click.mp3")

        self.text_surface = menu_font.render("Settings", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(width_btn // 2, self.text_y))

    def controls(self):
        buttons = [self.audio_button, self.back_button]

        for event in pg.event.get():
            if event.type == pg.USEREVENT and event.button == self.audio_button:
                self.fade()
                self.audio_menu.draw()

            if event.type == pg.USEREVENT and event.button == self.back_button:
                self.fade()
                self.main_menu.draw()

            for btn in buttons:
                btn.handle_event(event)

    def draw(self):
        self.surface.blit(self.bg_image, (0, 0))
        self.surface.blit(self.text_surface, self.text_rect)
        self.controls()


class AudioMenu(Menu):
    def __init__(self, bg_image, menu_font, surface, text_y, width_btn, height_btn, menu_windows):
        super().__init__(bg_image, menu_font, surface, text_y)
        self.width_btn = width_btn
        self.settings_menu = menu_windows

        self.audio_music_button = Button(self.surface.get_width() // 2 - width_btn // 2, 150, width_btn, height_btn,
                                         "Настройки музыки", r"menu/button_img.png",
                                         r"menu/button_img.png", r"sounds/button_click.mp3")
        self.audio_sound_button = Button(self.surface.get_width() // 2 - width_btn // 2, 250, width_btn, height_btn,
                                         "Настройки звуковых эффектов", r"menu/button_img.png",
                                         r"menu/button_img.png", r"sounds/button_click.mp3")
        self.back_button = Button(self.surface.get_width() // 2 - width_btn // 2, 350, width_btn, height_btn,
                                  "Назад", r"menu/button_img.png",
                                  r"menu/button_img.png", r"sounds/button_click.mp3")

        self.volume_slider = VolumeSlider(self.surface.get_width() // 2, 250, 250, 40)

        self.text_surface = menu_font.render("Audio Settings", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(width_btn // 2, self.text_y))

    def controls(self):
        buttons = [self.audio_music_button, self.back_button]

        for event in pg.event.get():
            if event.type == pg.USEREVENT and event.button == self.back_button:
                self.fade()
                self.settings_menu.draw()

            self.volume_slider.handle_event(event)

            for btn in buttons:
                btn.handle_event(event)

        for btn in buttons:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)
        self.volume_slider.draw(self.surface)

            # if event.type == pygame.USEREVENT and event.button == Audio_music_button:

                # running = False

            # if event.type == pygame.USEREVENT and event.button == Audio_sounds_button:

                # running = False

    def draw(self):
        self.surface.blit(self.bg_image, (0, 0))
        self.surface.blit(self.text_surface, self.text_rect)
        self.controls()
