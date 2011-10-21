import pygame
from pygame.locals import *
from world import *

#resolution of window
size = [800,600]


#some globals variables  (FIX LATER)

posX = 10.0
posY =  12.0

dirX = -1
dirY = 0

planeX = 0
planeY = .66


#color RED
red = (255,0,0)



#map example
testmap =[
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
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




window = None
screen = None

  

def main():
    
    #init pygame on the project
    pygame.init();
    
    
    window = pygame.display.set_mode(size)  # sets the pygame resolution window
    screen   = pygame.display.get_surface() # make a  surface copy  (main buffer)
    pygame.display.set_caption("Raycast  Test Number 1")  #  put a caption on the top od the window
    
    clock = pygame.time.Clock() # stores the cycle of every tick (time of  each tick)
    
    world = World(testmap, 0, 22, 11.5,  dirX, dirY, planeX, planeY) #  create a new world map + camera position
    
    
    done = False  #   the main loop controller, tell if the program still running or is about to close
    
    d = pygame.font.SysFont(pygame.font.get_default_font(), 20)  #  just wrapper to print FPS
    
    
    # MAIN LOOP
    
    while done == False: 
        
        clock.tick(60)  #sets   60 / 1000.0 milliseconds per tick  (or 60 FPS)
        screen.fill((0,0,0))  # erase screen for new tick  render  a new frame
        world.RenderCast(screen)
        text = d.render( str(clock.get_fps()), False, (255,0,0)) # render the text of FPS on screen
        screen.blit(text, text.get_rect(), text.get_rect()) #put on screen
        
        pygame.display.flip()  #gather all render elements put all screen  and clear  backbuffer to put a new render
        
        
        frametime = float(clock.get_time() / 1000.0 )   # get the time of each frame takes long
        
        
        movespeed = frametime * 5.0  # speed of main character
        rotationspeed  = frametime * 3.0  # rotation speed  of character (ok, it's global but i'll fix it later)
        
        
        for event in pygame.event.get():  # main event of the program
            if event.type == pygame.QUIT:  # if the people clicks on "X" or Xed the window it simply closes
                done = True
                
            elif event.type == KEYDOWN:  # checks  a keydown on your keyboard 
                if event.key == K_ESCAPE:   #if  press ESCAPE
                    done = True
            
            elif(event.type == KEYUP ):
                pass
                
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