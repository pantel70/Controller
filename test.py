from pyPS4Controller.controller import Controller
import pygame

# class MyController(Controller):

#     def __init__(self, **kwargs):
#         Controller.__init__(self, **kwargs)


# controller = MyController(interface="/dev/input/js1", connecting_using_ds4drv=False)

# done = False

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
done = False
print(joystick.get_name())
print(joystick.get_numaxes())

while True:
	for event in pygame.event.get():
		if event.type == pygame.JOYBUTTONUP:
			print("Button Released")
			done = True
		elif event.type == pygame.JOYBUTTONDOWN:
			print("Button pressed")
			done = True
		elif event.type == pygame.JOYAXISMOTION:
			print("Axis Moved")

# while not done:

# 	for event in pygame.event.get():
# 		if event.type == pygame.JOYAXISMOTION:
# 			print("Steering Wheel moved")
# 			done = True
# 		elif event.type == pygame.JOYBUTTONDOWN:
# 			print("Button pressed")
# 			done = True