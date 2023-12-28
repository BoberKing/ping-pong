from pygame import *
mw=display.set_mode((850,750))
display.set_caption('ping-pong')

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65, 65))
        self.speed= player_speed
        self.rect= self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 685:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 785:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        #self.direction= 'left'
        if self.rect.x <= 600:
            self.direction = 'right'
        if self.rect.x >= 800:
            self.direction = 'left'
        if self.direction =='left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

game=True
FPS=60
clock=time.Clock()
while game:
    for evente in event.get():
        if evente.type == QUIT:
            game= False
    clock.tick(FPS)
    display.update()