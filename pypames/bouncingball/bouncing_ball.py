import pygame

pygame.init()

# setting up game window
screen_width=500
screen_height=500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# colors
backgorund = (0, 0, 0)
object_color = (0, 102, 0)
radius = 20

# setup ball
ball_color = object_color
ball_radius = radius
ball_x = screen_width//2
ball_y = screen_height//2



# game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill(backgorund)

    # drawing ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

pygame.quit()
