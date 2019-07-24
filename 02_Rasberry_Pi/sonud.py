import pygame
import time

pygame.mixer.init()
bang = pygame.mixer.Sound("a.wav")
while True:
    bang.play()
    time.sleep(2)
