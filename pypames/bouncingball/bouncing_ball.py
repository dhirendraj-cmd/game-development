import pygame

pygame.init()

# setting up  window for ball
screen_width=500
screen_height=500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# colors adding
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

# speed of ball to move in all directions
ball_1x_speed = 200
ball_1y_speed = 200
ball_2x_speed = 100
ball_2y_speed = 100

# game loop
running=True
clock = pygame.time.Clock()
fps=120
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # control frme rate
    delta_time = clock.tick(fps)/1000.0


    # keep updating the position until closed
    ball_1x+=ball_1x_speed * delta_time
    ball_1y+=ball_1y_speed * delta_time
    ball_2x+=ball_2x_speed * delta_time
    ball_2y+=ball_2y_speed * delta_time

    # ÷detect the boundries
    if ball_1x + ball_radius > screen_width or ball_1x - ball_radius<0:
        ball_1x_speed = -ball_1x_speed
    if ball_1y + ball_radius > screen_height or ball_1y - ball_radius<0:
        ball_1y_speed = -ball_1y_speed

    if ball_2x + ball_radius > screen_width or ball_2x - ball_radius<0:
        ball_2x_speed = -ball_2x_speed
    if ball_2y + ball_radius > screen_height or ball_2y - ball_radius<0:
        ball_2y_speed = -ball_2y_speed

    # ball_radius+=0.01
    ball_1x_speed+=10
    ball_1y_speed+=10
    ball_2x_speed+=10
    ball_2y_speed+=10


    screen.fill(backgorund)

    # drawing ball
    pygame.draw.circle(screen, ball_color, (int(ball_1x), int(ball_1y)), ball_radius)
    pygame.draw.circle(screen, ball_color, (int(ball_2x), int(ball_2y)), ball_radius)

    pygame.display.flip()

    

pygame.quit()
