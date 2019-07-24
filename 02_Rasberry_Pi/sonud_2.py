import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("a.wav")
pygame.mixer.music.play()
time.sleep(100)
