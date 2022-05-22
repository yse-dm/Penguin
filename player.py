import pygame       #　インポート
from pygame import sprite, image, Rect
from pygame.locals import *     #　pygameで定義済みの定数

class Player(sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64, downscore = 1000):
        super().__init__()
        self.imagelist = imagelist
        self.rect = Rect(x, y, width, height)
        self.setcount(0)
        self.setimage(0)
        self.life = 5
        self.situation = "MUTEKI"
        self.downscore = downscore
        
    # フレームカウンタの設定
    def setcount(self,count):
        self.count = count
    # 画像の設定
    def setimage(self,num):
        self.num = num
        self.image = image.load(self.imagelist[self.num])
    # 動く床との関連付け
    def setfloor(self, floorlist): 
        self.accel = 0 
        self.floorlist = floorlist 
    # ゲームシーンとの関連付け
    def setgame(self,game):
        self.game = game
    # 動く床との当たり判定
    def landcheck(self): 
        for floor in self.floorlist: 
            x, y, width = floor.rect.x, floor.rect.y, floor.rect.width 
            if x - 32 <= self.rect.x <= x + width - 32: 
                if y - 64 <= self.rect.y <= y - 32: 
                    self.rect.y = y - 64
                    if self.game.score > self.downscore:
                        floor.down = "True" 
                    return True 
    
    #プレイヤーの初期化関数
    def setinit(self):
        self.rect.x = 288
        self.rect.y = 0
        self.life = 5

    #　更新用関数
    def update(self):
        #アニメーション用
        self.count += 1
        if self.count == 20:
            self.setimage(1)
        if self.count in [40, 56, 68, 80]:
            self.setimage(0)
        if self.count in [62, 74]:
            self.setimage(2)
        if self.count in [40, 80]:
            self.setcount(0)
        # キー入力に対応する
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and self.rect.x > 8 :
            self.rect.move_ip(-8,0)
        if pressed[K_RIGHT] and self.rect.x < 568:
            self.rect.move_ip(+8,0)
        # 動く床との当たり判定
        if self.landcheck():
            if pressed[K_SPACE]:
                self.accel = -16   # ここの数字を変更することで重力で移動する距離を変更することができる
                self.rect.y += self.accel
            else:
                self.accel = 0      # accelは加速度(重力の大きさ)　　+にすれば落下、-にすればジャンプする
        else:
            self.accel += 1
            self.rect.y += self.accel
            if self.rect.y >= 640:
                self.situation = "MUTEKI"
                self.rect.y = 428
                self.rect.x = 286
                self.accel = 0
                if self.life > 0:
                    self.life -= 1



        