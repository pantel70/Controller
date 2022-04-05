import pygame


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
wheel_buttons=["Cross","Square","Circle","Triangle","Right Paddle", "Left Paddle", "R2", "L2", "Share", "Option", "R3", "L3", "1st Gear", "2nd Gear", "3rd Gear", "4th Gear", "5th Gear", "6th Gear", "Reverse", "+", "-", "Right", "Left", "Enter", "PS Button"]
wheel_axes=["Steering", "Clutch", "Throttle", "Brake"]
prevAxis=1.0
axis=1.0

# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 40)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 25

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()
first = True
# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        try:
            jid = joystick.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = joystick.get_id()
        textPrint.tprint(screen, "Joystick {}".format(jid))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))

        try:
            guid = joystick.get_guid()
        except AttributeError:
            # get_guid() is an SDL2 method
            pass
        else:
            textPrint.tprint(screen, "GUID: {}".format(guid))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        
        for i in range(axes):
            if i == 2:
                if first:
                    axis = joystick.get_axis(2)
                    prevAxis = axis
                    first = False
                else:
                    axis = joystick.get_axis(2)
                    if axis < prevAxis:
                        print("Throttle Increasing {0:.3f}".format(axis))
                    elif axis > prevAxis:
                        print("Throttle Decreasing {0:.3f}".format(axis))
                    elif axis == prevAxis:
                        if not axis > 0.99:
                            print("Throttle Steady")
            else:
                axis = joystick.get_axis(i)
                if i == 0:
                    if axis < -0.005:
                        print("Steering Wheel Left")
                    elif axis > 0.005:
                        print("Steering Wheel Right")
            textPrint.tprint(screen, "             {} value: {:>6.3f}".format(wheel_axes[i], axis))
            if i == 2:
                prevAxis = axis
        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,
                             "             {} value: {}".format(wheel_buttons[i], button))
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
