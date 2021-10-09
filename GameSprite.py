from pygame import*
class GameSprite(sprite.Sprite): 
#конструктор класса 
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y, width, height, window): 
        super().__init__()
        self.window = window
        self.win_width = width
        self.win_height = height
        #вызываем конструктор класса (Sprite): 
        #sprite.Sprite.__init__(self) 
        #каждый спрайт должен хранить свойство image - изображение 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
        
#метод, отрисовывающий героя на окне 
    def reset(self): 
        self.window.blit(self.image, (self.rect.x, self.rect.y)) 
    def suit_load_l(self):
        self.suit = 0
        self.suits = []
        for i in range(1,8):
            self.suits.append(transform.scale(image.load('pixil-frame-' + str(i) + '.png'), (self.size_x, self.size_y)))
    def suit_load_r(self):
        self.suit = 0
        self.suits = []
        for i in range(7,0,-1):
            self.suits.append(transform.scale(image.load('pixil-frame-' + str(i) + '.png'), (self.size_x, self.size_y)))
    def suit_change(self):
        self.image = self.suits[self.suit]
        if self.suit < len(self.suits) - 1:
            self.suit += 1
        else:
            self.suit = 0
