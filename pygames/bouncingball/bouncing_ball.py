import threading
import pygame
import time


class BouncingBall(threading.Thread):

    def __init__(self, color, radius, position, speed, screen_width, screen_height):
        super().__init__(daemon=True)
        self.color=color
        self.radius=radius
        self.position=list(position)
        self.speed=list(speed)
        # self.delta_time=delta_time
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.running=True
        self.paused=True

    def run(self):
        self.move_ball()

    def move_ball(self):
        print("INside move ball")
        while self.running:
            if not self.paused:
                # position update
                self.position[0]+=self.speed[0]
                self.position[1]+=self.speed[1]

                # detect boundry
                if self.position[0] + self.radius > self.screen_width or self.position[0] - self.radius<=0:
                    self.speed[0] = -self.speed[0]
                if self.position[1] + self.radius > self.screen_height or self.position[1] - self.radius<=0:
                    self.speed[1] = -self.speed[1]

            pygame.time.wait(10)

    def start_ball(self):
        self.paused=False

    def stop_ball(self):
        self.running=False
    
    def pause_ball(self):
        self.paused=True


def main_screen():
    pygame.init()

    screen_width=600
    screen_height=600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Ball multithreaded")

    backgorund = (0, 0, 0)
    TEXT_COLOR = (255, 255, 255)
    RED = (200,0,0)
    GREEN = (0,200,0)
    BLUE = (0,0,200)

    running = True
    clock = pygame.time.Clock()
    fps=60

    # calling ball object from here
    balls = [
        BouncingBall((153, 0, 0), 20, [screen_width//2, screen_height//2], [1, 2], screen_width=screen_width, screen_height=screen_height),
        BouncingBall((0, 123, 0), 15, [screen_width//3, screen_height//3], [3, 1], screen_width=screen_width, screen_height=screen_height)
        ]

    for b in balls:
        b.start()
        # b.join()₹

    # Buttons of rectangle
    start_btn1 = pygame.Rect(30, screen_height-50, 80, 30)
    pause_btn1 = pygame.Rect(130, screen_height-50, 80, 30)
    start_btn2 = pygame.Rect(400, screen_height-50, 80, 30)
    pause_btn2 = pygame.Rect(500, screen_height-50, 80, 30)
    # stop_btn = pygame.Rect(250, screen_height-50, 80, 30)

    while running:
        # control frame rate
        # delta_time = clock.tick(fps)/1000.0

        screen.fill(backgorund)
            

        pygame.draw.rect(screen, GREEN, start_btn1)
        pygame.draw.rect(screen, BLUE, pause_btn1)
        pygame.draw.rect(screen, GREEN, start_btn2)
        pygame.draw.rect(screen, BLUE, pause_btn2)
        # pygame.draw.rect(screen, RED, stop_btn)

        # Button labels
        font = pygame.font.SysFont(None, 24)
        screen.blit(font.render("Start1", True, TEXT_COLOR), (start_btn1.x+15, start_btn1.y+5))
        screen.blit(font.render("Pause1", True, TEXT_COLOR), (pause_btn1.x+15, pause_btn1.y+5))
        screen.blit(font.render("Start2", True, TEXT_COLOR), (start_btn2.x+15, start_btn2.y+5))
        screen.blit(font.render("Pause2", True, TEXT_COLOR), (pause_btn2.x+15, pause_btn2.y+5))
        # screen.blit(font.render("Stop", True, TEXT_COLOR), (stop_btn.x+15, stop_btn.y+5))

        for b in balls:
            pygame.draw.circle(screen, b.color, (int(b.position[0]), int(b.position[1])), b.radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                for b in balls:
                    b.stop_ball()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn1.collidepoint(event.pos):
                    balls[0].start_ball()
                elif pause_btn1.collidepoint(event.pos):
                    balls[0].pause_ball()
                elif start_btn2.collidepoint(event.pos):
                    balls[1].start_ball()
                elif pause_btn2.collidepoint(event.pos):
                    balls[1].pause_ball()

                    
        pygame.display.flip()
        clock.tick(fps)



    pygame.quit()


if __name__=="__main__":
    main_screen()
