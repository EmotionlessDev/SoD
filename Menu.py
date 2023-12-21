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
        self.continue_button = Button(self.surface.get_width() // 2 - width_btn // 2, 150,
                                      width_btn, height_btn,
                                      "Продолжить", r"menu/button_img.png",
                                      r"menu/hovered_button.jpg", r"sounds/button_click.mp3")
        self.volume_slider = VolumeSlider(self.surface.get_width() // 2, 250, 250, 40)

    def fade(self):
        running = True
        fade_alpha = 0
        while running:

            fade_surface = pg.Surface(self.surface.get_size())
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(fade_alpha)
            self.surface.blit(fade_surface, (0, 0))

            fade_alpha += 5
            if fade_alpha >= 105:
                fade_alpha = 255
                running = False

            pg.display.flip()
            pg.time.Clock().tick(60)

    def start_menu(self):
        text_surface = self.menu_font.render("Shadow of Desolation", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.surface.get_width() // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        keys = pg.mouse.get_pressed()
        if keys[0] and self.start_button.is_hovered:
            self.fade()
            self.playing = True
            self.current_window = "Pause"

        if keys[0] and self.settings_button.is_hovered:
            self.fade()
            self.current_window = "Settings"

        if keys[0] and self.exit_button.is_hovered:
            self.fade()
            sys.exit()

        for btn in [self.start_button, self.settings_button, self.exit_button]:
            btn.handle_event(keys[0])

        for btn in [self.start_button, self.settings_button, self.exit_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def settings_menu(self):
        text_surface = self.menu_font.render("Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.surface.get_width() // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        keys = pg.mouse.get_pressed()
        if keys[0] and self.audio_button.is_hovered:
            self.fade()
            self.current_window = "Audio"

        if keys[0] and self.back_button.is_hovered:
            self.fade()
            self.current_window = "Start"

        for btn in [self.audio_button, self.back_button]:
            btn.handle_event(keys[0])

        for btn in [self.audio_button, self.back_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def audio_menu(self):
        text_surface = self.menu_font.render("Audio Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.surface.get_width() // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        self.volume_slider.draw(self.surface)

        keys = pg.mouse.get_pressed()
        if keys[0] and self.back_button.is_hovered:
            self.fade()
            self.current_window = "Settings"

        for btn in [self.audio_music_button, self.audio_sound_button, self.back_button]:
            btn.handle_event(keys[0])

        self.volume_slider.handle_event(keys[0], pg.mouse.get_pos())

        for btn in [self.audio_button, self.back_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def pause_menu(self):
        text_surface = self.menu_font.render("Pause", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.surface.get_width() // 2, self.text_y))
        self.surface.blit(text_surface, text_rect)

        keys = pg.mouse.get_pressed()
        if keys[0] and self.continue_button.is_hovered:
            self.fade()
            self.playing = True

        if keys[0] and self.exit_button.is_hovered:
            self.fade()
            sys.exit()

        for btn in [self.continue_button, self.exit_button]:
            btn.handle_event(keys[0])

        for btn in [self.continue_button, self.exit_button]:
            btn.check_hover(pg.mouse.get_pos())
            btn.draw(self.surface)

    def menu_selection(self):
        if self.current_window == "Start":
            self.start_menu()

        if self.current_window == "Settings":
            self.settings_menu()

        if self.current_window == "Audio":
            self.audio_menu()

        if self.current_window == "Pause":
            self.pause_menu()

    def draw(self):
        self.surface.blit(self.bg_image, (0, 0))
        self.menu_selection()
