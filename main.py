import pygame
import time
from pygame.locals import *
import random

OBSTACLE_DEFAULT_X = 800

class Bird:

    def __init__(self,surface):
        # default position of the bird
        self.surface = surface
        self.bird = pygame.image.load("C:/Users/hamro/Desktop/pygame_snake/floppy_bird/resources/bird.png")
        self.direction = ""
        self.x = 300
        self.y = 150

    def draw_bird(self):
        self.surface.blit(self.bird, (self.x, self.y))
        pygame.display.flip()

    def move(self):

        if self.direction == "up":
            self.y -= 5
        elif self.direction == "down":
            self.y += 5
        elif self.direction == "":
            self.x
            self.y
        else:
            pass

    def move_down(self):
        self.direction = "down"

    def move_up(self):
        self.direction = "up"

    def stop(self):
        self.direction = ""



class Obstacle:

    def __init__(self,surface):
        self.surface = surface
        self.obstacle_down = pygame.image.load("C:/Users/hamro/Desktop/pygame_snake/floppy_bird/resources/obstacle.png")
        self.obstacle_up = pygame.image.load("C:/Users/hamro/Desktop/pygame_snake/floppy_bird/resources/obstacle_up.png")
        self.x_position = OBSTACLE_DEFAULT_X
        self.obstacle_y_up = 300
        self.obstacle_y_down = -300
        self.render_obstacles()
        self.speed = 10
        self.score = 0


    def render_obstacles(self):
        # displaying background from 0 0
        self.surface.blit(self.obstacle_down,(self.x_position, self.obstacle_y_up))
        pygame.display.flip()
        self.surface.blit(self.obstacle_up, (self.x_position, self.obstacle_y_down))
        pygame.display.flip()

    def move_obstacles(self):
        """
        always keep the same gap between the obstacles
        so we randomly generate one obstacle and based on we calculate the position of the second one
        """
        self.x_position -= self.speed
        if self.x_position == 0:
            self.x_position = OBSTACLE_DEFAULT_X
            # it points down
            self.obstacle_y_down = random.randint(-400, -150)
            # it points up 200 is length of the top obstacle and 60 will be always the gap
            self.obstacle_y_up = self.obstacle_y_down + 500 + 100
            self.score += 1
            sound = pygame.mixer.Sound("C:/Users/hamro/Desktop/pygame_snake/floppy_bird/resources/Ding-sound-effect_.mp3")
            pygame.mixer.Sound.play(sound)

class Game:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((900, 500))
        pygame.display.set_caption("Testing out PyGame!")
        self.render_background()
        self.bird = Bird(self.surface)
        self.bird.draw_bird()
        self.obstacles = Obstacle(self.surface)
        pygame.mixer.init()


    def render_background(self):
        bg = pygame.image.load("C:/Users/hamro/Desktop/pygame_snake/floppy_bird/resources/background.jpg").convert()
        # displaying background from 0 0
        self.surface.blit(bg, (0, 0))
        pygame.display.flip()

    def collision(self):
        if self.bird.x == self.obstacles.x_position:
            if self.bird.y >= (self.obstacles.obstacle_y_up -55) or self.bird.y <= (self.obstacles.obstacle_y_down + 495):
                return True
        else:
            return False

    def display_score(self):
        font = pygame.font.SysFont("arial",25, bold=True)
        score = font.render(f"Score: {self.obstacles.score}", True, (255, 255, 0))
        # always to display sth use blit
        self.surface.blit(score,(400,20))


    def game_over(self):
        # first create surface because whatever i have i want to wipe out

        self.surface.fill((55, 55, 55))
        font = pygame.font.SysFont("arial", 40)
        score = font.render("Game Over!", True, (255, 255, 255))
        self.surface.blit(score, (350, 100))
        # always to display sth use blit
        font_2 = pygame.font.SysFont("arial", 17)
        score = font_2.render(f"your score was: {self.obstacles.score}", True, (255, 255, 255))
        self.surface.blit(score, (390, 160))
        font_3 = pygame.font.SysFont("arial", 17)
        score = font_3.render("if you want to return press enter", True, (255, 255, 255))
        self.surface.blit(score, (345, 185))
        pygame.display.flip()
        sound_crush = pygame.mixer.Sound("C:/Users/hamro/Desktop/pygame_snake/floppy_bird/resources/crush.mp3")
        pygame.mixer.Sound.play(sound_crush)

    def reset(self):
        self.obstacles.score = 0
        self.obstacles.x_position = OBSTACLE_DEFAULT_X



    def play(self):
        self.render_background()
        self.bird.move()
        self.bird.draw_bird()
        #self.obstacles.x_position += 10
        self.obstacles.render_obstacles()
        self.obstacles.move_obstacles()
        self.display_score()
        pygame.display.flip()


        #to prevent the bird from flying away off the screen
        if self.bird.y <= 0:
            self.bird.y = 0
        if self.bird.y >= 450:
            self.bird.y = 450
        if self.bird.x <= 0:
            self.bird.x = 0

        # collision check
        if self.collision():
            raise Exception
            # if collison clear the score
        else:
            pass



    def event_loop(self):
        run = True
        pause = False
        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # press escape to quit the game
                    if event.key == K_ESCAPE:
                        run = False
                    # to reset the cycle
                    # if pause is True we cannot loop through
                    if event.key == K_RETURN:
                        pause = False
                        self.reset()

                    if event.key == K_UP:
                        self.bird.move_up()
                    if event.key == K_DOWN:
                        self.bird.move_down()
                    if event.key == K_SPACE:
                        self.bird.stop()
                elif event.type == QUIT:
                    run = False
            try:
                if not pause:
                    self.play()
                    time.sleep(0.04)
            except Exception as e:
                self.game_over()
                pause = True










if __name__ == '__main__':
    game = Game()
    game.event_loop()



