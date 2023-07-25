import pgzrun

WIDTH = 700
HEIGHT = 700
FPS = 30


def draw():
    screen.draw.text('HELLO WORLD', color='red', center=(350, 350), fontsize=50)


def update(dt):
    pass


pgzrun.go()
