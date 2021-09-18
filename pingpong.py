from pygame import*
from GameSprite import GameSprite
from Player import Player
def game():
    back = (200, 255, 255)
    win_width = 600
    win_height = 500
    window = display.set_mode((win_width, win_height))
    window.fill(back)
    run = True
    finish = False
    clock = time.Clock()
    FPS = 60

    racket1 = Player('pixil-frame-0 (1).png', 30, 200, 4, 50, 150, win_width, win_height, window)
    racket2 = Player('pixil-frame-0.png', 520, 200, 4, 50, 150, win_width, win_height, window)


    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
        racket1.reset()       
        racket2.reset()
        display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    game()