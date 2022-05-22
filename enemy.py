import pygame       #　インポート
from pygame import sprite, image, Rect
from pygame.locals import *     #　pygameで定義済みの定数
from random import choice

class Enemy(sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x, y, width, height)
        self.setcount(0)
        self.setimage(0)
        self.setspeed(0)
        
    # フレームカウンタの設定
    def setcount(self,count):
        self.count = count
    # 画像の設定
    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])
    #速度の設定
    def setspeed(self,speed):
        self.speed = speed
    #ショットとの関連付け
    def setshot(self,shot):
        self.shot = shot
    #　更新用関数
    def update(self):
        #アニメーション用
        self.count += 1
        if self.count == 20:
            self.setimage(1)
        if self.count == 40:
            self.setimage(0)
            self.setcount(0)
            speed = [-4, +4]
            self.speed = choice(speed)
            if self.shot.rect.y >= 640:
                self.shot.setplace(self.rect.x,self.rect.y)
                self.shot.setimage(1)
                self.shot.setspeed(8)
        #移動処理
        if self.rect.x > 0 and self.speed < 0:
            self.rect.move_ip(self.speed,0)
        if self.rect.x < 576 and self.speed > 0:
            self.rect.move_ip(self.speed,0)
            
            