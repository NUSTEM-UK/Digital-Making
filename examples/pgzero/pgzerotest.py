"""PyGame Zero test script.

Run using:

    pgzrun pgzerotest.py

Will pop up a window with a dark red background and an alien graphic. Note that PyGameZero is broken on Macs as of Summer 2019.
"""

import pgzrun

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 300
HEIGHT = alien.height + 20

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        print("You missed me!")

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'

def draw():
    screen.fill((128, 0, 0))
    alien.draw()


pgzrun.go()