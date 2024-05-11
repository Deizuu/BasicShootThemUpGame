# Importing modules.
import pygame as pg

# Setting up the window.
pg.init()
screen = pg.display.set_mode((1280,720)) # Assigns the window resolution.
clock = pg.time.Clock() # Creates a clock which will be used to limit the framerate.
running = True # If this value is False, the window will close.
dt = 0 # This is the delta time value, which is the difference in seconds between the last frame and the current frame.
playerPos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2) # Assigns the base player position.

while running:
    # Poll for events.
    for event in pg.event.get():
        # If the pg.QUIT event (pressing the 'X' button) got triggered, then the window will close.
        if(event.type == pg.QUIT):
            running = False
            pg.quit()

    # Filling the screen with a background color.
    screen.fill("#3c4c7d")

    # Rendering the game.
    pg.draw.circle(screen, "red", playerPos, 20)
    
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

    # Putting the render on the screen.
    pg.display.flip()

    dt = clock.tick(60) / 1000 # Limits framerate to 60 FPS.