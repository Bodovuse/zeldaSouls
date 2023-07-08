base files created
main.py created
level.py created

- calls settings.py
    - holds map
        -location of Rocks and Player

- calls tile.py
    - holds Rock image to place on map
    - holds rock characteristics

- calls player.py
    -holds player chatacteristics
        - speed
        -direction


01-07-23 16:14----------------------------------------------

Collisions work

    - apply horizontal movement 
        - check horizontal (x) collisions
    - apply vertical movement
        - check vertical (y) collisions
    (49:46)

*Bugs

    - issues with corners in collisions
        - player clipping
    - issues with both vertical and horizontal collisions

02-07-23--------------------------------------------------

Camera

    - screen now follows player character

Hitboxes

    - player now appears infront/behind sprites with overlap

BUG FIX

    - fixed collisions bug
        - player was clipping through walls

(1:11:24)