import pygame       #　インポート
from pygame import sprite, image, Rect
from pygame.locals import *

class Game(sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagefile, x = 0, y = 0, width = 640, height = 640):
        super().__init__()
        self.image = image.load(imagefile)
        self.rect = Rect(x, y, width, height)
        self.before = False
        self.score = 0
        self.scene = "TITLE"
        self.time = 100
     #ゲームの初期化関数
    def setinit(self):
        self.score = 0
        self.scene = "PLAY"
        self.time = 100
    
    #　更新用関数
    def update(self):
        if self.time > 0.025 and self.scene in ["PLAY","OVER"] :
            self.time -= 0.025
        elif self.scene in ["TITLE","TIMEATACK","RANKING"]:
            return
        else:
            self.scene = "OVER"