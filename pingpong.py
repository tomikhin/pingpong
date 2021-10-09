from pygame import*
import time as t

from GameSprite import GameSprite
from Player import Player
def game():
    back = "background.png"
    start_time = t.time()
    win_width = 600
    win_height = 500
    window = display.set_mode((win_width, win_height))
    
    run = True
    finish = False
    clock = time.Clock()
    FPS = 60
    background = transform.scale(image.load(back), (win_width, win_height))

    racket1 = Player('pixil-frame-0 (1).png', 30, 200, 4, 20, 150, win_width, win_height, window)
    racket2 = Player('pixil-frame-0.png', 520, 200, 4, 20, 150, win_width, win_height, window)
    racket1.suit_load_l()
    racket2.suit_load_r()
    ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50, win_width, win_height, window)
    font.init()
    font1 = font.SysFont('Arial', 35)
    font2 = font.SysFont('Tahoma', 14)
    lose1 = font1.render('Player 1 WINS!:)', True, (0, 190, 255))
    lose2 = font1.render('Player 2 WINS!:)', True, (255, 255, 0))
    speed_x = 7
    speed_y = 7
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
        if finish != True:
            text_time = font2.render("Длительность игры: " + str(round(t.time() - start_time, 1)) + ' сек', True, (0, 255, 0))

            window.blit(background, (0, 0))
            window.blit(text_time, (380, 25))
            racket1.reset()       
            racket2.reset()
            ball.reset()
            if sprite.collide_rect(racket1, ball):
                racket1.suit_change()
                speed_x *= -1
            if sprite.collide_rect(racket2, ball):
                racket2.suit_change()
                speed_x *= -1
            if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed_y *= -1
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            racket2.update_r()
            racket1.update_l()
            if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (190, 100))
            if ball.rect.x > win_width:
                finish = True
                window.blit(lose2, (220, 100))
        display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    game()
