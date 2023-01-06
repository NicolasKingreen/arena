import pygame as pg

import state_machine


class GameStateMachine(state_machine.StateMachine):
    
    def __init__(self, game_instance):
        super().__init__()

        main_menu_game_state = MainMenuGameState(game_instance)
        playing_game_state = PlayingGameState(game_instance)
        pause_game_state = PauseGameState(game_instance)

        self.add_state(main_menu_game_state)
        self.add_state(playing_game_state)
        self.add_state(pause_game_state)


class GameState(state_machine.State):

    def __init__(self, name, game_instance):
        self.name = name
        self.game_instance = game_instance

    def do_actions(self):
        dt = self.game_instance.clock.tick_busy_loop(60)
        self._handle_events()
        self._update_gui(dt)
        self._update_world(dt)
        self._update_screen()
        fps = self.game_instance.clock.get_fps()
        print(f"fps: {fps}\r", end="")

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_instance.close()
            elif event.type == pg.KEYDOWN:
                self._handle_keydown_event(event)
            elif event.type == pg.KEYUP:
                self._handle_keyup_event(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                self._handle_mousedown_event(event)

    def _handle_keydown_event(self, event):
        if event.key == pg.K_ESCAPE:
            self.game_instance.close()

    def _handle_keyup_event(self, event):
        pass

    def _handle_mousedown_event(self, event):
        pass

    def _update_gui(self, dt):
        pass

    def _update_world(self, dt):
        pass

    def _update_screen(self):
        pass

    def check_conditions(self):
        pass

    def entry_actions(self):
        pass

    def exit_actions(self):
        pass


class MainMenuGameState(GameState):

    def __init__(self, game_instance):
        super().__init__("main_menu", game_instance)
        self.is_changing = False

    def _handle_mousedown_event(self, event):
        if self.game_instance.play_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game_instance.play_sound.play()
            self.is_changing = True

    def _update_gui(self, dt):
        self.game_instance.title.update(dt)

    def _update_screen(self):
        self.game_instance.background.draw(self.game_instance.screen)
        self.game_instance.title.draw(self.game_instance.screen)
        self.game_instance.play_button.draw(self.game_instance.screen)
        # self.game_instance.screen.blit(self.game_instance.cursor_image, self.game_instance.cursor_rect)
        pg.display.update()

    def check_conditions(self):
        if self.is_changing:
            return "playing"
        
        return None

    def entry_actions(self):
        pg.mixer.music.play(loops=-1, fade_ms=10000)

    def exit_actions(self):
        pg.mixer.music.stop()
        self.is_changing = False


class PlayingGameState(GameState):

    def __init__(self, game_instance):
        super().__init__("playing", game_instance)
        self.is_changing = False

    def _handle_keydown_event(self, event):
        if event.key == pg.K_ESCAPE:
            self.game_instance.close()
        elif event.key == pg.K_SPACE:
            self.is_changing = True
        elif event.key == pg.K_d:
            self.game_instance.world.player.movement_direction[0] += 1
        elif event.key == pg.K_a:
            self.game_instance.world.player.movement_direction[0] -= 1
        elif event.key == pg.K_s:
            self.game_instance.world.player.movement_direction[1] += 1
        elif event.key == pg.K_w:
            self.game_instance.world.player.movement_direction[1] -= 1

    def _handle_keyup_event(self, event):
        if event.key == pg.K_d:
            self.game_instance.world.player.movement_direction[0] -= 1
        elif event.key == pg.K_a:
            self.game_instance.world.player.movement_direction[0] += 1
        elif event.key == pg.K_s:
            self.game_instance.world.player.movement_direction[1] -= 1
        elif event.key == pg.K_w:
            self.game_instance.world.player.movement_direction[1] += 1

    def _update_world(self, dt):
        self.game_instance.world.update(dt)

    def _update_screen(self):
        self.game_instance.screen.fill((135, 194, 137))
        self.game_instance.world.draw(self.game_instance.screen)
        # self.game_instance.screen.blit(self.game_instance.cursor_image, self.game_instance.cursor_rect)
        pg.display.update()

    def check_conditions(self):
        if self.is_changing:
            return "pause"

        return None

    def exit_actions(self):
        self.is_changing = False


class PauseGameState(GameState):

    def __init__(self, game_instance):
        super().__init__("pause", game_instance)
        self.is_changing = False

    def _handle_keydown_event(self, event):
        super()._handle_keydown_event(event)
        if event.key == pg.K_SPACE:
            self.is_changing = True

    def _update_screen(self):
        self.game_instance.screen.fill((135, 194, 137))
        self.game_instance.world.draw(self.game_instance.screen)
        # self.game_instance.screen.blit(self.game_instance.cursor_image, self.game_instance.cursor_rect)
        # TODO: screen blurring and pause text
        pg.display.update()

    def check_conditions(self):
        if self.is_changing:
            return "playing"

        return None

    def entry_actions(self):
        pg.display.set_caption("Arena [Paused]")
        self.game_instance.world.player.movement_direction = [0, 0]

    def exit_actions(self):
        self.is_changing = False
        pg.display.set_caption("Arena")