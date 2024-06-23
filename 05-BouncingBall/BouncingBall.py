import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball:
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.x = random.randint(20, 980)
        self.y = random.randint(20, 580)
        self.speed_x = random.randint(3, 15)
        self.speed_y = random.randint(3, 15)
        self.ball_color1 = random.randint(1, 255)
        self.ball_color2 = random.randint(1, 255)
        self.ball_color3 = random.randint(1, 255)
        self.ball_size_radius = random.randint(5, 30)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x >= 1000:
            self.speed_x *= -1
        if self.y >= 600:
            self.speed_y *= -1
        if self.x <= 0:
            self.speed_x *= -1
        if self.y <= -1:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color(self.ball_color1, self.ball_color2, self.ball_color3)
                           , (self.x, self.y), self.ball_size_radius)



# x, y, size, speed, color, screen
# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Bouncing Ball')
    clock = pygame.time.Clock()
    balls = []
    # TODO: Create an instance of the Ball class called ball1
    for i in range(1, 100):
        ball1 = Ball(screen)
        balls.append(ball1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball
        # ball1.move()
        # ball1.draw()

        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
