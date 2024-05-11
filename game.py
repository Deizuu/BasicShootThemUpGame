# Importing modules.
import pygame as pg, time


# Setting up the window.
pg.init()
screen = pg.display.set_mode((1280,720)) # Assigns the window resolution.
clock = pg.time.Clock() # Creates a clock which will be used to limit the framerate.
running = True # If this value is False, the window will close.
dt = 0 # This is the delta-time value, which is the difference in seconds between the last frame and the current frame.
playerPos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2) # Assigns the base player position.
bulletList = [] # Creates a list for the bullets of the player.

def bulletCreation(x, y, bulletList):
    # Creating the bullets in the list of bullets.
    bulletList.append([x, y-28])
    return bulletList

def bulletMovement(bulletList):
    # Making the bullets move and deleting them when they're out of view.
    for bullet in bulletList:
        bullet[1] -= 1
        if bullet[1] < -8: 
            bulletList.remove(bullet)
    return bulletList

while running:
    # Poll for events.
    for event in pg.event.get():
        # If the pg.QUIT event (pressing the 'X' button) got triggered, then the window will close.
        if(event.type == pg.QUIT):
            running = False
            pg.quit()
        if(event.type == pg.KEYUP):
            if(event.key == pg.K_SPACE):
                bulletCreation(playerPos.x, playerPos.y, bulletList)


    # Filling the screen with a background color.
    screen.fill("#3c4c7d")

    # Rendering the game.
    pg.draw.circle(screen, "red", playerPos, 20)
    for bullet in bulletList:
        pg.draw.rect(screen, "yellow", ((bullet[0] - 1), bullet[1], 2, 4))
    # Making the movement of the player.
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        playerPos.y -= 300 * dt
    if keys[pg.K_a]:
        playerPos.x -= 300 * dt
    if keys[pg.K_s]:
        playerPos.y += 300 * dt
    if keys[pg.K_d]:
        playerPos.x += 300 * dt

    # Applying the bullet movement function.
    bulletMovement(bulletList)
    # Putting the render on the screen.
    pg.display.flip()
    
    dt = clock.tick(60) / 1000 # Limits framerate to 60 FPS and assigns the delta-time value.