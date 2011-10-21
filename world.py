import pygame
from pygame.locals import *
import math


textureWidth = 64
textureHeight = 64

class World(object):
        
    
    def __init__(self, worldmap,  sprite_positions, x,y,dirx,diry,planex,planey):
        self.background = None
        self.camera  = Camera(x,y,dirx,diry,planex,planey)
        self.world = worldmap
        
        self.walls = [
                      [
                      LoadImage( pygame.image.load("data/redbrick.png").convert(),  True),
                       LoadImage( pygame.image.load("data/redbrick.png").convert(), True) 
                      ]]
        
        
       
        
        
        
    def  RenderCast(self, surface):
    
        w = surface.get_width()
        h = surface.get_height()
        
        
        if self.background == None:
            self.background = pygame.transform.scale(pygame.image.load("data/bg.png").convert(), (w,h))
            
        surface.blit(self.background, (0,0))
        
        
        zbuffer = []
            
        
    
        for x in range(w):
            cameraX = float(2 * x / float(w) - 1)
            rayPosX = self.camera.x
            rayPosY = self.camera.y
            rayDirX = self.camera.dirx +  self.camera.planex * cameraX
            rayDirY = self.camera.diry +  self.camera.diry  *  cameraX
            mapX = int(rayPosX)
            mapY = int(rayPosY)
        

        
            deltaDistX = math.sqrt(1 + (rayDirY * rayDirY) ) / (rayDirX * rayDirX )
            if rayDirY == 0: rayDirY = 0.00001
            deltaDistY = math.sqrt(1 + (rayDirX * rayDirX) ) / (rayDirY * rayDirY )
        
            stepX = 0
            stepY = 0
            
            sideDistX = 0.
            sideDistY = 0.
                
            hit = 0
            side = 0
        
            if rayDirX < 0:
                stepX = -1
                sideDistX = (rayPosX - mapX) * deltaDistX
            else:
                stepX = 1
                sideDistX = (mapX + 1.0 - rayPosX ) * deltaDistX
            
            if rayDirY < 0:
                stepY = -1
                sideDistY = (rayPosY - mapY) * deltaDistY
            else:
                stepY = 1
                sideDistY = (mapY + 1.0 - rayPosY) * deltaDistY
            
            
        
        while hit == 0:
            if( sideDistX < sideDistY):
                sideDistX += stepX
                side = 0
            else:
                sideDistY += deltaDistY
                mapY += stepY
                side = 1
            
            if( self.world[mapX][mapY] > 0 ):
                hit = 1
                
                
        
        
        if side == 0:
            perpWallDist = (abs((mapX - rayPosX + ( 1 - stepX) / 2  ) / rayDirX))
        else:
            perpWallDist = (abs((mapY - rayPosY + ( 1 - stepY) / 2  ) / rayDirY))
            
            
        if( perpWallDist == 0): perpWallDist = 0.00001
            
        
        lineheight = abs(int(h / perpWallDist))
        
        drawstart = - lineheight / 2 + h / 2
        
        drawend = lineheight / 2 + h / 2
        
        if( drawstart < 0 ): drawstart = 0
        
        
        
        if( drawend >= h ): drawend = w - 1
        
        
        texNum = self.world[mapX][mapY] - 1
        wallX = 0
        
        if( side == 1): wallX = rayPosX + (( mapY + rayPosY + (1 - stepY) / 2) / rayDirY) * rayDirX
        else: wallX = rayPosX + (( mapX + rayPosX + (1 - stepX) / 2) / rayDirX) * rayDirY
        
        wallX -= math.floor(wallX)
        
        textureX = int(wallX * float(textureWidth))
        
        if( side == 0  and rayDirX > 0 ):
            textureX =  textureWidth - textureX - 1
            
        if( side == 1 and rayDirY < 0):
            textureX = textureWidth - textureX - 1
            
        if side == 1:
            texNum += 8
            
        if lineheight > 10000:
            lineheight = 10000
            drawstart =  -10000 / 2 + h / 2
            
        #apenas para teste
        surface.blit( pygame.transform.scale( pygame.image.load("data/redbrick.png").convert()   , (1,lineheight)), (x, drawstart))
        
        
        zbuffer.append(perpWallDist)
        
        
            
        
        
        #pygame.draw.line(surface, color, (0, drawstart + h), (drawstart,drawend))

    
            
        
        
    
    

class Camera(object):
    def __init__(self,x,y,dirx,diry,planex,planey):
        self.x =  float(x)
        self.y = float(y)
        self.dirx = float(dirx)
        self.diry = float(diry)
        self.planex = float(planex)
        self.planey = float(planey)

    
def LoadImage(image,dark,colorkey = None):
    ret = []
    
    if( colorkey is not None):
        image.set_colorkey( colorkey)
        
    if dark:
        image.set_alpha(127)
        
    for i in range(image.get_width()):
        surface = pygame.Surface((1, image.get_height())).convert()
        
        surface.blit(image,(-i,0))
        
        if colorkey is not None:
            surface.set_colorkey(colorkey)
            ret.append(surface)
            
        return ret
    
    
        
    
    