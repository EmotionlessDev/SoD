import pygame as pg
from Button import Button
from Volume import VolumeSlider
import sys
pg.init()


class Menu:
    def __init__(self, bg_image, menu_font, surface, text_y, width_btn, height_btn):
        self.surface = surface
        self.bg_image = pg.image.load(bg_image)
        self.bg_image = pg.transform.scale(self.bg_image, self.surface.get_size())
        self.menu_font = menu_font
        self.text_y = text_y
        self.width_btn = width_btn
        self.height_btn = height_btn

        self.playing = False
        self.current_window = "Start"

        self.start_button = Button(self.surface.get_width() // 2 - self.width_btn // 2, 150,
                                   self.width_btn, self.height_btn,
                                   "Новая игра", r"menu/button_img.png",
                                   r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.settings_button = Button(self.surface.get_width() // 2 - self.width_btn // 2, 250,
                                      self.width_btn, self.height_btn,
                                      "Настройки", r"menu/button_img.png",
                                      r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.exit_button = Button(self.surface.get_width() // 2 - self.width_btn // 2, 350,
                                  self.width_btn, self.height_btn,
                                  "Выйти", r"menu/button_img.png",
                                  r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.audio_button = Button(self.surface.get_width() // 2 - width_btn // 2, 150,
                                   width_btn, height_btn,
                                   " Аудио", r"menu/button_img.png",
                                   r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.back_button = Button(self.surface.get_width() // 2 - width_btn // 2, 350,
                                  width_btn, height_btn,
                                  "Назад", r"menu/button_img.png",
                                  r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.audio_music_button = Button(self.surface.get_width() // 2 - width_btn // 2, 150,
                                         width_btn, height_btn,
                                         "Настройки музыки", r"menu/button_img.png",
                                         r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.audio_sound_button = Button(self.surface.get_width() // 2 - width_btn // 2, 250,
                                         width_btn, height_btn,
                                         "Настройки звуковых эффектов", r"menu/button_img.png",
                                         r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.volume_slider = VolumeSlider(self.surface.get_width() // 2, 250, 250, 40)

    def start_menu(self):
        text_surface = self.menu_font.render("Shadow of Desolation", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.surface.get_width() // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        for event in pg.event.get():
            if self.start_button.is_hovered and \
                    event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.playing = True

            if self.settings_button.is_hovered and \
               event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.current_window = "Settings"

            if self.exit_button.is_hovered and \
                    event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                sys.exit()

            for btn in [self.start_button, self.settings_button, self.exit_button]:
                btn.handle_event(event)

        for btn in [self.start_button, self.settings_button, self.exit_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def settings_menu(self):
        text_surface = self.menu_font.render("Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width_btn // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        for event in pg.event.get():
            if self.audio_button.is_hovered and \
                    event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.current_window = "Audio"

            if self.back_button.is_hovered and \
                    event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.current_window = "Start"

            for btn in [self.audio_button, self.back_button]:
                btn.handle_event(event)

        for btn in [self.audio_button, self.back_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def audio_menu(self):
        text_surface = self.menu_font.render("Audio Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width_btn // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        self.volume_slider.draw(self.surface)

        for event in pg.event.get():
            if self.back_button.is_hovered and \
                    event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.current_window = "Settings"

            for btn in [self.audio_music_button, self.audio_sound_button, self.back_button, self.volume_slider]:
                btn.handle_event(event)

        for btn in [self.audio_button, self.back_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def menu_selection(self):
        if self.current_window == "Start":
            self.start_menu()

        if self.current_window == "Settings":
            self.settings_menu()

        if self.current_window == "Audio":
            self.audio_menu()

    def draw(self):
        self.surface.blit(self.bg_image, (0, 0))
        self.menu_selection()
