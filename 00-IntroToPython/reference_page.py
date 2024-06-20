#Boilerplate is used

import pygame
import sys

pygame.init()

pygame.display.set_caption("Hello Gabriel")
# TODO 00: Change the window caption to say your name.


screen = pygame.display.set_mode((640, 480))
# TODO 05: Change the window size, make sure your circle code still works.

while True:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    #  TODO 01: Make the background white by uncommenting the line below
    # screen.fill(pygame.Color("Gray"))
    #
    #  Draw things on the screen
    #
    #  TODO 02: Try to draw a circle (any size, any color, anywhere)
    # pygame.draw.circle(screen, pygame.Color("Orange"), (50,50), 25)
    #
    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    # pygame.draw.circle(screen, pygame.Color("Red"), (320, 240), 100)
    #
    #  TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    # pygame.draw.circle(screen, pygame.Color("Yellow"), (10, 470), 10)
    #
    # pygame.display.update()




# clock stuff
#  clock = pygame.time.Clock()
# clock.tick(60)

# drawling
# pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
#         pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline
#
#         pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
#         pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
#         pygame.draw.circle(screen, (0, 0, 0), (242 + eye_delta_x, 162 + eye_delta_y), 7)  # black pupil
#
#         pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
#         pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
#         pygame.draw.circle(screen, (0, 0, 0), (398 + eye_delta_x, 162 + eye_delta_y), 7)  # black pupil
# # rectangle
#         pygame.draw.rect(screen, pygame.Color(0, 0, 0), (230, 320, 180, 30))

# load image
# image1 = pygame.image.load("2dogs.JPG")
# blit image
# screen.blit(image1, (0, 0))

# text
# font1 = pygame.font.SysFont("comicsansms", 28)
# caption1 = font1.render("Two Dogs", True, pygame.Color(BLACK))
# screen.blit(caption1, (screen.get_width() / 2 - caption1.get_width() / 2, image1.get_height() - 4))

#sound effects
#dog_bark = pygame.mixer.Sound("bark.wav")
#  while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             # TODO 9: Play the music (bark) if there's a mouse click.
#             if event.type == pygame.MOUSEBUTTONUP:
#                 dog_bark.play()
#                 print("dog bark")
# see at bottom part
