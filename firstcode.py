#!/usr/bin/env python
import pygame 
import sys
from pygame.locals import *

CLOCK_TICK = pygame.USEREVENT
 
class CApp:
    def __init__(self):
        self._running = True
        self._surf_display = None
        self.MoveBullet = False
 
    def OnInit(self):
        self.size = self.width, self.height = 640, 400
        self.speed_down =[0, 2]
        self.speed_right = [2, 0]
        self.speed_up = [0, -2]
        self.speed_left = [-2, 0]
        self.black = 0, 0, 0

        pygame.init()
        self._display_surf = pygame.display.set_mode((640,400),\
                               pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('this is the first programme!')
        self._running = True

        #Fill background 
        self.background = pygame.Surface(self._display_surf.get_size())
        self.background = self.background.convert()
        self.background.fill((255, 235, 205))
        self._display_surf.blit(self.background, (0, 0))

        # add a plane
        self.plane = pygame.image.load("plane.bmp")
        self.planerect = self.plane.get_rect()

        # add a bullet image
        self.bullet = pygame.image.load("apple.png")

        # add a bullet list
        self.bullets = []

        pygame.time.set_timer(CLOCK_TICK, 20)
 
    def OnEvent(self, event):
        if event.type == QUIT:
            self._running = False
            sys.exit()
        elif event.type == CLOCK_TICK:
           for rect in self.bullets:
                self.bullets.remove(rect)
                rect = rect.move(self.speed_down)
                if rect.left < 0 or rect.right > self.width or \
                     rect.top < 0 or rect.bottom > self.height:
                    pass
                else:
                    self.bullets.append(rect)
        elif event.type == KEYUP:
            if event.key == pygame.K_SPACE:
                self.bulletrect = self.bullet.get_rect()
                self.bulletrect = self.bulletrect.move(self.planerect.center)
                self.bullets.append(self.bulletrect)
    
    def OnLoop(self):
        pass
    def OnRender(self):
        pass
   
    def BallMoveBykey(self):
        """
        move the plane by the way
        """
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_UP]:
            self.planerect = self.planerect.move(self.speed_up)
            self.BorderHandle()
        elif pressed_keys[pygame.K_DOWN]:
            self.planerect = self.planerect.move(self.speed_down)
            self.BorderHandle()
        elif pressed_keys[pygame.K_LEFT]:
            self.planerect = self.planerect.move(self.speed_left)
            self.BorderHandle()
        elif pressed_keys[pygame.K_RIGHT]:
            self.planerect = self.planerect.move(self.speed_right)
            self.BorderHandle()

    def BorderHandle(self):
        """
        prevent the plane out of the border
        """
        if self.planerect.left < 0: 
            self.planerect = self.planerect.move(self.speed_right)
        elif self.planerect.right > self.width:
            self.planerect = self.planerect.move(self.speed_left)
        elif self.planerect.top < 0:
            self.planerect = self.planerect.move(self.speed_down)
        elif self.planerect.bottom > self.height:
            self.planerect = self.planerect.move(self.speed_up)

    def DrawBullet(self):
        """
        make the plane move auto
        """
        self._display_surf.blit(self.bullet, self.bulletrect)
        self._display_surf.blit(self.plane, self.planerect)
        self.bulletrect = self.bulletrect.move(self.speed_down)

    def BulletMove(self):
        """
        the moving bullet launched by flighter
        """
 
    def Blit(self):
        """
        draw the picture
        """
        pygame.display.flip()
        self._display_surf.blit(self.background, (0, 0))
        self._display_surf.blit(self.plane, self.planerect)
        for rect in self.bullets:
            self._display_surf.blit(self.bullet, rect)

    def OnCleanup(self):
        pygame.quit()
 
    def OnExecute(self):
        if self.OnInit() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.OnEvent(event)
            self.OnLoop()
            self.OnRender()
            self.BallMoveBykey()
            self.Blit()
 
if __name__ == "__main__" :
    theApp = CApp()
    theApp.OnExecute()
