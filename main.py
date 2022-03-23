import pgzrun

WIDTH = 300
HEIGHT = 300
FPS = 30


def draw():
    screen.draw.text('HELLO WORLD', color='white', center=(150, 150), fontsize=50)


def update(dt):
    pass


pgzrun.go()
