import pygame       #　インポート
from pygame import sprite, image, Rect
from pygame.locals import *
from random import choice    # 任意の要素を選択する

class Floor(sprite.Sprite): 
    # コンストラクタ 
    def __init__(self, imagelist, x = 0, y = 0, width = 96, height = 32): 
        super().__init__()
        self.imagelist = imagelist 
        self.rect = Rect(x, y, width, height) 
        self.setimage(0)
        self.setspeed(0)  
        self.down = "False"
    # プレイヤーとの関連付け
    def setplayer(self, player): 
        self.player = player 
    # 画像の設定 
    def setimage(self, num): 
        self.num = num 
        self.image = image.load(self.imagelist[self.num]) 
    # 速度の設定
    def setspeed(self,speed):
        self.speed = speed
    # 更新用関数 
    def update(self): 
        # 動かない床
        if self.speed == 0:
            return
        x = [ 16, 144, 272, 400, 528] 
        y = [640, 720, 800, 880, 960] 
        if self.rect.y <= 128: 
            self.rect.x = choice(x) 
            self.rect.y = choice(y) 
        if self.down == "False":
            self.rect.move_ip(0, self.speed) 
        if self.down == "True":
            self.rect.move_ip(0, -(self.speed))
            if self.rect.y >= 720:
                self.down = "False"
                self.rect.x = choice(x) 
                self.rect.y = choice(y)
