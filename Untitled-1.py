from pygame import *
from random import randint

back = (200, 255, 255)
window = display.set_mode((500, 500))
display.set_caption("pon")
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update_ri(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_le(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed


ball = GameSprite ("ball.png", 100, 200, 10, 10, 3)
racket_l = Player("racket.png", 30, 200, 100, 30, 7)
racket_r = Player("racket.png", 30, 200, 100, 30, 7)

speed_x = 3
speed_y = 3


game = True
finish = False
FSP = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket_l.update_le()
        racket_r.update_ri()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_y *= 1
            speed_x *= -1
        
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit()

        if move_right:
            platform.rect.x += 3
        if move_left:   
            platform.rect.x -= 3

        #if ball.rect.y > 350:
            #time_text = Label(150, 150, 50, 50, back)
            #time_text.set_text("YOU LOSE", 60, (250,0,0))
            #time_text.draw(10, 10)
            #game_over = True

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        
    display.update()