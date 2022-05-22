import pygame # pygame のモジュール 
from pygame.locals import * # pygame で定義済みの定数 
from pygame import sprite, image, Rect 
from random import randint, randrange # 正の乱数を生成する 
class Item(sprite.Sprite): 
    # コンストラクタ 
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64): 
        super().__init__() 
        self.imagelist = imagelist 
        self.rect = Rect(x, y, width, height) 
        self.setimage(0) 
        self.settimer() 
        # 表示時間の設定 
    def settimer(self): 
        self.time = randint(5, 9) 
        # 画像の設定 
    def setimage(self, num): 
        self.num = num 
        self.image = image.load(self.imagelist[self.num]) 
        # 表示場所の設定 
    def setplace(self, x, y): 
        self.rect.x = x 
        self.rect.y = y 
    # 初期化用関数
    def setinit(self):
        x = randrange(0, 576, 64) 
        y = randrange(128, 448, 64) 
        self.setplace(x, y) 
        self.settimer() 
        # 更新用関数 
    def update(self): 
        if self.time == 3: 
            self.setplace(640, 640)
        if self.time > 0.025: 
            self.time -= 0.025 
        else: 
            x = randrange(0, 576, 64) 
            y = randrange(128, 448, 64) 
            self.setplace(x, y) 
            self.settimer() 
