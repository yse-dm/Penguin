import pygame                   #　pygameのインポート
from pygame.locals import *     #　pygameで定義済みの定数
from random import randint      #乱数の生成用
from random import choice
from pygame import sprite, image, Rect

class Enemy01(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64, speed = -8):
        super().__init__()
        self.imagelist = imagelist 
        self.rect = Rect(x, y, width, height) 
        self.setimage(0)
        self.speed = 4 

    # 画像の設定 
    def setimage(self, num): 
        self.num = num 
        self.image = image.load(self.imagelist[self.num]) 

    #　更新用関数
    def update(self):
        speedlist = [4, 6]
        x = [-192, -256, -320] 
        y = [576, 512, 448, 384, 320, 256, 192, 128] 
        self.rect.move_ip(self.speed, 0)
        if self.rect.x > 640:
            self.rect.x = choice(x) 
            self.rect.y = choice(y)
            self.speed = choice(speedlist)
            
            