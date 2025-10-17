import pygame

pygame.init()

# setting up game window
screen_width=500
screen_height=500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# colors
backgorund = (0, 0, 0)
object_color = (153, 102, 0)
radius = 20

# setup ball
ball_color = object_color
ball_radius = radius
ball_1x = screen_width//2
ball_1y = screen_height//1.05
ball_2x = screen_width//3
ball_2y = screen_height//8

# velocity/speed of ball to move in all directions
ball_1x_speed = 5
ball_1y_speed = 5
ball_2x_speed = 2
ball_2y_speed = 2

# game loop
running=True
clock = pygame.time.Clock()
fps=60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


    # keep updating the position until closed
    ball_1x+=ball_1x_speed
    ball_1y+=ball_1y_speed
    ball_2x+=ball_2x_speed
    ball_2y+=ball_2y_speed

    # ÷detect the boundries
    if ball_1x + ball_radius > screen_width or ball_1x - ball_radius<0:
        ball_1x_speed = -ball_1x_speed
    if ball_1y + ball_radius > screen_height or ball_1y - ball_radius<0:
        ball_1y_speed = -ball_1y_speed

    if ball_2x + ball_radius > screen_width or ball_2x - ball_radius<0:
        ball_2x_speed = -ball_2x_speed
    if ball_2y + ball_radius > screen_height or ball_2y - ball_radius<0:
        ball_2y_speed = -ball_2y_speed


    screen.fill(backgorund)

    # drawing ball
    pygame.draw.circle(screen, ball_color, (int(ball_1x), int(ball_1y)), ball_radius)
    pygame.draw.circle(screen, ball_color, (int(ball_2x), int(ball_2y)), ball_radius)

    pygame.display.flip()

    # control frme rate
    clock.tick(fps)

pygame.quit()
