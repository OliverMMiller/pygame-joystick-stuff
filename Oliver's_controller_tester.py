import pygame
from pygame.locals import *
import pygame._sdl2
from pygame._sdl2.controller import Controller
import time

# Ignore all of the orange squigglies under '_sdl2'. It's because of the underscore. It's annoying, but there's nothing
# I can do about it

# Initialize all the the pygame modules
pygame.init()

# initialize the _sdl2 modules
pygame._sdl2.controller.init()

# Initialize the controller and assign to 'con'. This assumes once controller is connected and was given index 0
con = pygame._sdl2.controller.Controller(0)

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

def main():
    # Set the width and height of the screen (width, height), and name the window.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    text_print = TextPrint()

    done = False
    while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

        screen.fill((255, 255, 255))
        text_print.reset()


        # Print D-pad
        text_print.tprint(screen, "d-Pad: ")
        text_print.tprint(screen,  f"{con.get_button(CONTROLLER_BUTTON_DPAD_UP)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_DPAD_RIGHT)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_DPAD_DOWN)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_DPAD_LEFT)}")
        # Print joysticks 
        text_print.tprint(screen, "joysticks: ")
        text_print.tprint(screen, f"{con.get_axis(CONTROLLER_AXIS_LEFTX)}")
        text_print.tprint(screen, f"{con.get_axis(CONTROLLER_AXIS_LEFTY)}")
        text_print.tprint(screen, f"{con.get_axis(CONTROLLER_AXIS_RIGHTX)}")
        text_print.tprint(screen, f"{con.get_axis(CONTROLLER_AXIS_RIGHTY)}")
        # Print triggers
        text_print.tprint(screen, "triggers: ")
        text_print.tprint(screen, f"{con.get_axis(CONTROLLER_AXIS_TRIGGERLEFT)}")
        text_print.tprint(screen, f"{con.get_axis(CONTROLLER_AXIS_TRIGGERRIGHT)}")
        # Print bumpers and buttons
        text_print.tprint(screen, "bumbers/buttons: ")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_LEFTSHOULDER)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_RIGHTSHOULDER)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_A)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_B)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_X)}")
        text_print.tprint(screen, f"{con.get_button(CONTROLLER_BUTTON_Y)}")
        text_print.tprint(screen, "\n")

        for i in range(con.as_joystick().get_numaxes()):
            text_print.tprint(screen, f"{round(con.as_joystick().get_axis(i), 6)}")
            #text_print.tprint(screen, f"{con.as_joystick().get_axis(i)}")

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 30 frames per second.
        clock.tick(30)


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
