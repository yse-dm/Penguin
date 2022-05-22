import pygame # pygame のモジュール 
from pygame.locals import * # pygame で定義済みの定数 
from pygame import sprite, image, Rect 

class Shot(sprite.Sprite): 
    # コンストラクタ 
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64): 
        super().__init__() 
        self.imagelist = imagelist 
        self.rect = Rect(x, y, width, height) 
        self.setimage(0) 
        self.setspeed(0)
        # 画像の設定 
    def setimage(self, num): 
        self.num = num 
        self.image = image.load(self.imagelist[self.num]) 
    #速度の設定
    def setspeed(self,speed):
        self.speed = speed
        # 表示場所の設定 
    def setplace(self, x, y): 
        self.rect.x = x 
        self.rect.y = y 
        # 更新用関数 
    def update(self): 
        if self.rect.y < 640:
            self.rect.move_ip(0,self.speed)