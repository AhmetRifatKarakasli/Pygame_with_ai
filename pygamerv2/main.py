import numpy as np
import pygame
import mediapipe as mp
import cv2
import random

webcam=cv2.VideoCapture(0)
webcam.set(3,1280)
webcam.set(4,720)

pygame.init()
en,boy=1280,720
pencere=pygame.display.set_mode(((en,boy)))
zaman=pygame.time.Clock()
fps=30

mario=pygame.image.load("F:/projeler/pytion/pygamer/mario.png")
mario=pygame.transform.scale(mario,(80,80))
mario_konum=mario.get_rect()

altin=pygame.image.load("F:/projeler/pytion/pygamer/coin.png")
altin=pygame.transform.scale(altin,(50,50))
altin_konum=altin.get_rect()
altin_konum.center=(100,100)

font=pygame.font.Font(None, 60)

x, y = 500, 500
puan = 0
model = mp.solutions.hands

dongu=True

with model.Hands(min_tracking_confidence=0.5,min_detection_confidence=0.5) as el:
    while dongu:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                dongu=False

        _,frame=webcam.read()
        frame=cv2.flip(frame,1)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        result=el.process(rgb)
        if result.multi_hand_landmarks:
            for elkoordinatlari in result.multi_hand_landmarks:
                konum=elkoordinatlari.landmark[8]
                x=int(konum.x*en)
                y=int(konum.y*boy)
        mario_konum.center=(x,y)
        rgb=np.rot90(rgb)
        img=pygame.surfarray.make_surface(rgb).convert()
        img=pygame.transform.flip(img,True,False)
        pencere.blit(img,(0,0))
        pencere.blit(mario,mario_konum)
        pencere.blit(altin,altin_konum)
        yazi=font.render("Puan: "+str(puan),True,(0,0,255),(0,0,0))
        yazi_konum=yazi.get_rect()
        yazi_konum.topleft=(20,20)
        pencere.blit(yazi,yazi_konum)

        if mario_konum.colliderect(altin_konum):
            altin_konum.x = random.randint(0,en-50)
            altin_konum.y = random.randint(0, boy - 50)
            puan+=1

        pygame.display.update()
        zaman.tick(fps)

pygame.quit()






