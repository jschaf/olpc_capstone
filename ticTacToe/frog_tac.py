import os
import sys
import pygame
import pygame.locals as pygl


class Game(object):
    
    SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
    BG_COLOR = 150, 150, 80

    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        
    
    def run():
        '''
        '''

        pygame.init()
        
        clock = pygame.time.Clock()

        pygame.display.set_caption('Frog Tac')

        dispatch = {pygame.QUIT: exit_game,
                    pygame.KEYDOWN: 
                    }

        while 1:
            # Limit frame speed to 30 FPS
            clock.tick(30)

            for event in pygame.event.get():
                action = dispatch.get(event.type)
                if action is None: pass
                else: action()

            screen.fill(BG_COLOR)

            pygame.display.flip()

    def exit_game(self):
        sys.exit()

if __name__ == '__main__':
    main()
