import pygame       #　インポート
from pygame import sprite, image, Rect
from pygame.locals import *
from random import choice

class Goal(sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagefile, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.imagelist = imagefile
        self.rect = Rect(x, y, width, height)
        self.setimage(1)
        self.setspeed(8)
        self.move = "RIGHT"  
    # プレイヤーとの関連付け
    def setplayer(self, player): 
        self.player = player 
    # 画像の設定 
    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])
    # 速度の設定
    def setspeed(self,speed):
        self.speed = speed
    #ゲームの初期化関数
    def setinit(self):
        pass
    # 更新用関数 
    def update(self): 
        if self.move == "RIGHT":
            self.rect.move_ip(self.speed, 0) 
            if self.rect.x >= 544:
                self.move = "LEFT"
        if self.move == "LEFT":
            self.rect.move_ip(-(self.speed), 0)
            if self.rect.x <= 0:
                self.move = "RIGHT"
     