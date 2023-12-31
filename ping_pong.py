from pygame import *

window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Пинг-понг')
window.fill([0, 125, 0])

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image ,x_size , y_size, x_cor, y_cor, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y 
        if keys_pressed[K_s] and self.rect.y <= 440:
            self.rect.y += self.speed_y
    def update_r(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= 480:
            self.speed_y *= -1
        if ball.rect.colliderect(rocket_l.rect) or ball.rect.colliderect(rocket_r.rect):
            self.speed_x *= -1
            self.speed_y *= -1
        

rocket_l = Player('rocket.png', 40, 90, 5, 30, 0, 5)  
rocket_r = Player('rocket.png', 40, 90, 655, 30, 0, 5)
ball = Ball('301904415255211.png', 100, 100, 250, 300, 3, 4)
game = True
FPS = 60
clock = time.Clock()
finish = False

font.init()
fontmy = font.SysFont('Arial', 70)

player1 = fontmy.render("one player wins", True,(255, 215, 0))
player2 = fontmy.render('two player wins', True,(255, 215, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        rocket_l.update_l()
        rocket_r.update_r()
        ball.update()

        window.fill([0, 125, 0])
        rocket_l.reset()
        rocket_r.reset()
        ball.reset()




    display.update()
    clock.tick(FPS)
    rocket_r.reset()

    if ball.rect.x <= -60:
        window.blit(player2, (130,150))
        finish = True

    if ball.rect.x >= 650:
        window.blit(player1, (130,150))
        finish = True

    display.update()
    clock.tick(FPS)
