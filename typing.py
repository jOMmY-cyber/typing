import pygame
import time
import random
from pygame import *
from keycap import *
pygame.init()

screen = pygame.display.set_mode([500, 300])
running = True
font = pygame.font.Font('freesansbold.ttf', 16)
#check_key
def check_key(check,cap):
    if cap.text == check:
        if cap.is_key(keys):
            cap.active()
            return True
        else:
            cap.inactive()
            return False
#เอาตัวอักษรใส่แต่ละแถว        
def get_cha_list(long_str):
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for cha in long_str:
        row1.append(cha)
    return row1 #list

row1 = get_cha_list('1234567890[]')
row2 = get_cha_list("',.pyfgcrl/=")
row3 = get_cha_list('aoeuidhtns-')
row4 = get_cha_list(';qjkxbmwvz')
row1_cap = []
row2_cap = []
row3_cap = []
row4_cap = []
i = 0
j = 0.5
h = 1
k = 1.5

for cha in row1:
    row1_cap.append(  Keycap(screen,20+i*25,100,20,20, cha,(255,0,0), font)  )
    i += 1

for cha in row2:
    row2_cap.append( Keycap(screen,20+j*25,125,20,20, cha,(255,0,0), font))
    j += 1

for cha in row3:
    row3_cap.append( Keycap(screen,20+h*25,150,20,20, cha,(255,0,0), font))
    h += 1

for cha in row4:
    row4_cap.append( Keycap(screen,20+k*25,175,20,20, cha,(255,0,0), font))
    k += 1
while running:    
    correct = '6'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    screen.fill((255, 255, 255))#tuple
    keys = pygame.key.get_pressed()
    for cap in row1_cap:
        cap.draw()
        if  check_key(cap.text,cap) and cap.text == correct:
            cap.correct()
        
    for cap in row2_cap:
        cap.draw()
        check_key(cap.text,cap)
    for cap in row3_cap:
        cap.draw()
        check_key(cap.text,cap)
    for cap in row4_cap:
        cap.draw()
        check_key(cap.text,cap)
    

    pygame.display.update()

