alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 300
HEIGHT = alien.height + 20

def draw():
    screen.fill((128, 0, 0))
    alien.draw()