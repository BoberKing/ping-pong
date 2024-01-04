from pygame import *
font.init()
mw=display.set_mode((850,750))
display.set_caption('ping-pong')
background=transform.scale(image.load('puk.jpg'),(850,750))
font=font.Font(None,70)
player_1_lose=font.render('Player 1 lose!!',True,(255,0,0))
player_2_lose=font.render('PLayer 2 lose!!',True,(255,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,w,h):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(w,h))
        self.speed= player_speed
        self.rect= self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 685:
            self.rect.y += self.speed
    
    def update_l(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 685:
            self.rect.y += self.speed

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

rocket_1=Player('pngwing.com.png',10,370,5,90,135)
rocket_2=Player('pngwing.com.png',740,370,5,90,135)
ball=Enemy('volleyball-2844925_640.png',380,330,5,90,90)
game=True
FPS=60
clock=time.Clock()
speed_x= 3
speed_y=3
finish=False
while game:
    for evente in event.get():
        if evente.type == QUIT:
            game= False
    if finish !=True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        mw.blit(background,(0,0))
        rocket_1.reset()
        rocket_2.reset()
        rocket_1.update_l()
        rocket_2.update_r()
        ball.reset()
    
    if ball.rect.y > 700 or ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(rocket_1, ball) or sprite.collide_rect(rocket_2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish=True
        mw.blit(player_1_lose,(425,385))

    if ball.rect.x >700:
        finish=True
        mw.blit(player_2_lose,(425,385))
    clock.tick(FPS)
    display.update()