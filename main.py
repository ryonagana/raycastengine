import pygame
from world import *

pygame.init();
size = [640,480]


posX = 22.0
posY =  12.0

dirX = -1
dirY = 0

planeX = 0
planeY = 0.66



red = (255,0,0)




testmap =[
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];




window = pygame.display.set_mode(size)
screen = pygame.display.get_surface()

pygame.display.set_caption("Teste")



clock = pygame.time.Clock()




world = World(testmap, 0, 22, 11.5,  dirX, dirY, planeX, planeY)
            
            
            
            
        

def main():
    
    done = False
    
    d = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    
    while done == False:
        
        clock.tick(60)
        world.RenderCast(screen)
        text = d.render( str(clock.get_fps()), False, (255,255,255))
        screen.blit(text, text.get_rect(), text.get_rect())
        
        pygame.display.flip()
        
        
        frametime = float(clock.get_time() / 1000.0 )
        
        
        movespeed = frametime * 5.0
        rotationspeed  = frametime * 3.0
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if(event.type == KEYUP ):
                
                key = pygame.key.get_pressed()
                
                if( key[K_UP]):
                    moveX = world.camera.x + world.camera.dirx * movespeed
                    if( testmap[int(moveX)][int(world.camera.y)] == 0 and  testmap[int(moveX + 0.1)][int( world.camera.y)] == 0):  
                            world.camera.x += world.camera.dirx * movespeed
                    
                    moveY = world.camera.y * world.camera.dirx * movespeed
                    
                    if( testmap[int(world.camera.x)][int(moveY)] == 0 and  testmap[int(world.camera.x)][int(moveY + 0.1)] == 0):
                        world.camera.y += world.camera.diry * movespeed
                    
                    
                      
                    
                
                
                
                
            
    pygame.quit()
    

if __name__ == '__main__':
    main()  