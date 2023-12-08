import pygame

# initialize pygame
pygame.init()

# set up the display
screen = pygame.display.set_mode((800, 600))

# draw a red building
building_rect = pygame.Rect(100, 100, 200, 300)
pygame.draw.rect(screen, (255, 0, 0), building_rect)

# update the display
pygame.display.flip()

# wait for the user to close the window
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# quit pygame
pygame.quit()
