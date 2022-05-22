#　インポート処理
import sys                      #　システムモジュール
import pygame                   #　pygameのモジュール
from pygame.locals import *     #　pygameで定義済みの定数
from pygame import display
from pygame import sprite
from pygame import mixer
from game import Game
from player import Player
from floor import Floor   
from enemy import Enemy
from item import Item
from shot import Shot
from goal import Goal
from random import randrange 
from floor2 import Floor2
from player2 import Player2 

# メインプログラム
def main():
    #　pygameの初期化
    pygame.init()
    surface = display.set_mode((640, 640))
    display.set_caption("Flying Penguin")

    # 音声ファイルの取得
    sound1 = mixer.Sound("./sound/pop.wav")
    sound2 = mixer.Sound("./sound/crunch.wav")

    # 画像データの取得 
    game = Game("./image/game.png") 
    playerfile = [ 
        "./image/blue01.png", "./image/blue02.png", 
        "./image/space.png",
    ] 
    player = Player(playerfile, 288, 128) 

    enemyfile = [
        "./image/wood01.png", "./image/wood02.png", 
    ]
    enemylist = []
    enemylist.append(Enemy(enemyfile,128,64))
    enemylist.append(Enemy(enemyfile,448,64))

    shotfile = [
        "./image/space.png", "./image/spear.png", 
    ]
    shotlist = []
    shotlist.append(Shot(shotfile,128,640))
    shotlist.append(Shot(shotfile,448,640))

    floorfile = [
        "./image/space.png", "./image/floor.png", 
    ]

    floorlist = []
    for i in range(8):
        speed = -2 * (i % 2) -2
        floor = Floor(floorfile, 0, 128)
        floor.setimage(1)
        floor.setspeed(speed)
        floorlist.append(floor)
    floor = Floor(floorfile, 272, 528)
    floor.setimage(1)
    floorlist.append(floor)

    itemfile = [
        "./image/space.png","./image/potion.png",
        ]
    itemlist = []
    for i in range(3):
        x = randrange(0, 576, 96)
        y = randrange(128, 448, 96)
        item = Item(itemfile, x, y)
        item.setimage(1)
        itemlist.append(item)
    # スプライトをグループに登録 
    group_bg = sprite.Group()
    group_pl = sprite.Group()
    group_fl = sprite.Group()
    group_it = sprite.Group()
    group_en = sprite.Group()
    group_bg.add(game) 
    group_pl.add(player)
    group_fl.add(floorlist)
    group_it.add(itemlist)
    group_en.add(shotlist)
    group_en.add(enemylist)      

    # プレイヤーと動く床の関連付け
    player.setfloor(floorlist)

    enemylist[0].setshot(shotlist[0])
    enemylist[1].setshot(shotlist[1])

    player.setgame(game)

    # 動く床とプレイヤーの関連付け
    for i in floorlist:
        i.setplayer(player)  

    # フォントオブジェクトの作成
    font = pygame.font.SysFont("Verdana", 30, bold=True)
    font2 = pygame.font.SysFont("msgothicmsuigothicmspgothic", 40, bold=False)
    font3 = pygame.font.SysFont("msgothicmsuigothicmspgothic", 30, bold=False)
    font4 = pygame.font.SysFont("msgothicmsuigothicmspgothic", 30, bold=True)

    goalfile = [ 
        "./image/space.png","./image/goal.png",
    ] 
    goal = Goal(goalfile, 0, -4604, 64, 64) 

    floorgoalfile = [
        "./image/space.png", "./image/floor.png", 
    ]
    floorgoal = Goal(floorgoalfile, 0, -4540, 96, 32)
    group_gl = sprite.Group()
    group_gl.add(goal)
    group_gl.add(floorgoal)

    group_fl2 = sprite.Group()
    group_pl2 = sprite.Group() 
    player2 = Player2(playerfile, 32, 490)
    group_pl2.add(player2)
    
    list_x = [
        0,96,192,288,384,480,576,0,96,192,288,384,480,576,
        0, 300, 300, 456, 555, 150, 32, 325, 125, 325,
        325, 125, 325, 32, 150, 555, 456, 300, 300, 0,
        0, 300, 300, 456, 555, 150, 32, 325, 125, 325,
        0, 300, 300, 456, 555, 150, 32, 325, 125, 325,
        325, 125, 325, 32, 150, 555, 456, 300, 300, 0,
        325, 125, 325, 32, 150, 555, 456, 300, 300, 0,
        0, 300, 300, 456, 555, 150, 32, 325, 125, 325,
        325, 125, 325, 32, 150, 555, 456, 300, 300, 0, 
    ]
    list_y = [
        608,608,608,608,608,608,608,640,640,640,640,640,640,640,
        560,480,400,400,320,280,160,80,40,0,
        -80,-160,-240,-320,-400,-440,-480,-560,-600,-640,
        -720,-800,-880,-960,-1000,-1040,-1120,-1200,-1240,-1280,
        -1360,-1440,-1520,-1560,-1600,-1680,-1760,-1840,-1880,-1920,
        -2000,-2080,-2160,-2280,-2320,-2400,-2400,-2480,-2520,-2560,
        -2640,-2720,-2800,-2880,-2960,-3000,-3040,-3120,-3160,-3200,
        -3280,-3360,-3440,-3520,-3560,-3600,-3680,-3760,-3800,-3840,
        -3920,-4000,-4080,-4160,-4280,-4320,-4400,-4400,-4440,-4480,
    ]

    floorfile2 = [
        "./image/space.png", "./image/floor.png", 
    ]
    floorlist2 = []
    for i, j in zip(list_x, list_y):
        floor2 = Floor2(floorfile2, i, j)
        floor2.setimage(1)
        floor2.setspeed(0)
        floorlist2.append(floor2)
    group_fl2.add(floorlist2)

    player2.setfloor2(floorlist2)
    player2.setfloorgoal2(floorgoal)

    time_at = 0
    score_count = 0
    score_count2 = 0
    time_list = []
    nomber = 0
    score_y = 200
    clear = False

    system = pygame.image.load("./image/image_se.png")
    close = pygame.image.load("./image/close.png")
    menu = pygame.image.load("./image/menuimage.png")
    button = pygame.image.load("./image/button.png")
    menu1 = True
    menu2 = False
    scorejudge = True
    bgmjudge = True
    leveljudge = 1
    levellist = ["easy", "normal", "hard"]
    enemyscore = 1000
    enemycount = 0
    muteki = 0


    #　ループ処理
    while(True):

        if game.scene == "TITLE":


            #if bgmjudge == True:
            #    sound3.play()

            # 背景表示
            group_bg.update()
            group_bg.draw(surface)

            # タイトル
            titletext = font2.render("Flying Penguin",True, "white")
            surface.blit(titletext, (192, 32))

            # メニュー
            if menu1 == True:
                menutext = font.render("Backspace : GameStart",True, "white")
                surface.blit(menutext, (160, 280))
                menu2text = font.render("ESCAPE : TimeAtack",True, "white")
                surface.blit(menu2text, (160, 340))
                menu3text = font.render("1 : Ranking",True, "white")
                surface.blit(menu3text, (160, 400))
                surface.blit(system,(550,550))

                # キー入力に対応する
                pressed = pygame.key.get_pressed()
                if pressed[K_BACKSPACE]: 
                    game.scene = "PLAY"
                pressed = pygame.key.get_pressed()
                if pressed[K_ESCAPE]: 
                    game.scene = "TIMEATACK"
                if pressed[K_1]:
                    game.scene = "RANKING"

            if menu2 == True:
                offtext = font3.render("OFF",True, "black")
                ontext = font3.render("ON",True, "black")
                level1text = font3.render("Easy",True, "black")
                level2text = font3.render("Normal",True, "black")
                level3text = font3.render("Hard",True, "black")
                surface.blit(menu,(64,150))
                menu2text_1 = font3.render("BGM",True, "black")
                surface.blit(menu2text_1, (110, 240))
                surface.blit(button,(320,240))
                if bgmjudge == True:
                    surface.blit(ontext, (350, 247))
                elif bgmjudge == False:
                    surface.blit(offtext, (350, 247))
                menu2text_2 = font3.render("score記録",True, "black")
                surface.blit(menu2text_2, (110, 340))
                surface.blit(button,(320,340))
                if scorejudge == True:
                    surface.blit(ontext, (350, 347))
                elif scorejudge == False:
                    surface.blit(offtext, (350, 347))
                menu2text_3 = font3.render("難易度",True, "black")
                surface.blit(menu2text_3, (110, 440))
                surface.blit(button,(320,440))
                if levellist[leveljudge] == "normal":
                    surface.blit(level2text, (326, 447))
                elif levellist[leveljudge] == "easy":
                    surface.blit(level1text, (335, 447))
                    player = Player(playerfile, 288, 128, 64, 64, 1000) 
                    group_pl.empty()
                    group_pl.add(player)
                    player.setfloor(floorlist)
                    player.setgame(game)
                    for i in floorlist:
                        i.setplayer(player)
                    enemyscore = 1500
                if levellist[leveljudge] == "hard":
                    surface.blit(level3text, (335, 447))
                    player = Player(playerfile, 288, 128, 64, 64, 500) 
                    group_pl.empty()
                    group_pl.add(player)
                    player.setfloor(floorlist)
                    player.setgame(game)
                    for i in floorlist:
                        i.setplayer(player)
                    enemyscore = 1000

            display.update()
            pygame.time.wait(25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #マウスの位置情報の取得
                if event.type == MOUSEBUTTONDOWN:
                    m_x,m_y = event.pos
                    print(m_x,m_y)
                    if menu1 == True:
                        if  570 <= m_x <= 634:
                            if 570 <= m_y <= 634:
                                menu1 = False
                                menu2 = True
                    if menu2 == True:
                        if  325 <= m_x <= 408:
                            if 244 <= m_y <= 288:
                                if bgmjudge == True:
                                    bgmjudge = False
                                else:
                                    bgmjudge = True
                        if  325 <= m_x <= 408:
                            if 344 <= m_y <= 380:
                                if scorejudge == True:
                                    scorejudge = False
                                else:
                                    scorejudge = True
                        if  325 <= m_x <= 408:
                            if 444 <= m_y <= 480:
                                leveljudge += 1
                                if leveljudge >= 3:
                                    leveljudge = 0
                        if  495 <= m_x <= 560:
                            if 160 <= m_y <= 225:
                                menu2 = False
                                menu1 = True
        
        if game.scene == "PLAY" or game.scene == "OVER":
            if levellist[leveljudge] == "easy":
                player.downscore = 10000
            muteki += 1
            # 描画処理と更新処理
            if game.score < enemyscore:
                group_bg.update() 
                group_pl.update() 
                group_fl.update() 
                group_it.update() 
                group_bg.draw(surface)
                group_pl.draw(surface)
                group_fl.draw(surface)
                group_it.draw(surface)

            if game.score >= enemyscore or enemycount >= 1:
                enemycount += 1
                for shot in shotlist:
                    if pygame.sprite.collide_rect(player, shot):
                        shot.setplace(640, 640)
                        player.setimage(2)
                        player.setcount(50)
                        if player.life > 0 and game.scene == "PLAY":
                            player.life -= 1
                            if bgmjudge == True:
                                sound2.play()
                if levellist[leveljudge] == "hard" and muteki >= 60:
                    for z in enemylist:
                        if pygame.sprite.collide_rect(player, z):
                            player.setimage(2)
                            player.setcount(50)
                            player.life -= 1
                            game.score -= 50
                            muteki = 0
                            if bgmjudge == True:
                                sound2.play()

                group_bg.update() 
                group_pl.update() 
                group_fl.update()
                group_it.update() 
                group_en.update()  
                group_bg.draw(surface)
                group_pl.draw(surface)
                group_fl.draw(surface)
                group_it.draw(surface)
                group_en.draw(surface)
                
                # 当たり判定処理
            if game.scene == "PLAY":
                for item in itemlist:
                    if pygame.sprite.collide_rect(player, item):
                        item.setplace(640, 640)
                        game.score += 100
                        if bgmjudge == True:
                            sound1.play()
                
                if player.rect.y >= 640:
                    game.score -= 50

            if player.life <= 0:
                game.scene = "OVER"

            # ゲーム時間の表示処理
            timetext = font.render(f"TIME:{game.time:>5.0f}",True, "white")
            surface.blit(timetext, (32,16))

            # ゲームスコアの表示処理
            scoretext = font.render(f"SCORE:{game.score:>5.0f}",True, "white")
            surface.blit(scoretext, (416,16))

            # ゲームオーバーの表示処理
            if game.scene == "OVER" and player.life <= 0:
                overtext = font.render("GAME OVER",True, "white")
                surface.blit(overtext, (220,240))
                menuetext1 = font.render("1 : Continue",True, "white")
                surface.blit(menuetext1, (220,280))
                menuetext2 = font.render("2 : Title",True, "white")
                surface.blit(menuetext2, (220,320))
            # 時間切れの表示処理
            if game.scene == "OVER" and game.time <= 0.025 and player.life > 0:
                overtext = font.render("Times Up",True, "white")
                surface.blit(overtext, (220,240))
                menuetext1 = font.render("1 : Continue",True, "white")
                surface.blit(menuetext1, (220,280))
                menuetext2 = font.render("2 : Title",True, "white")
                surface.blit(menuetext2, (220,320))

            # ライフの表示処理
            scoretext = font.render(f"LIFE:{player.life:>5}",True, "white")
            surface.blit(scoretext, (230,16))

            #　更新処理
            display.update()               
            pygame.time.wait(25)

            pressed = pygame.key.get_pressed()
            if game.scene == "OVER"and pressed[K_1]:
                if scorejudge == True:
                    file = open("./score2.txt","a")
                    file.write(str(game.score) + '\n')
                    file.close()
                for i in range(8):
                    floorlist[i].rect.y = 128
                for item in itemlist:
                    item.setinit()
                player.setinit()
                game.setinit()
                enemycount = 0
                muteki = 0
            if game.scene == "OVER"and pressed[K_2]:
                if scorejudge == True:
                    file = open("./score2.txt","a")
                    file.write(str(game.score) + '\n')
                    file.close()
                for i in range(8):
                    floorlist[i].rect.y = 128
                for item in itemlist:
                    item.setinit()
                player.setinit()
                game.setinit()
                enemycount = 0
                muteki = 0
                game.scene = "TITLE"

            #　全てのイベントを取得する
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
        if game.scene == "TIMEATACK":
            
            group_bg.update() 
            group_pl2.update() 
            group_fl2.update() 
            group_bg.draw(surface)
            group_pl2.draw(surface)
            group_fl2.draw(surface)

            group_gl.update() 
            group_gl.draw(surface)
             
            
            if player2.rect.y < 256:
                for i in floorlist2:
                    i.rect.y += (600 - player2.rect.y) // 100
                goal.rect.y += (600 - player2.rect.y) // 100
                floorgoal.rect.y += (600 - player2.rect.y) // 100
            else:    
                for i in floorlist2:
                    i.rect.y += -(player2.accel)
                goal.rect.y += -(player2.accel)
                floorgoal.rect.y += -(player2.accel)

            if clear == False:
                time_at += 0.025
            # ゲーム時間の表示処理
            if clear == False:
                timetext = font.render(f"TIME:{time_at:>5.3f}",True, "white")
                surface.blit(timetext, (400,16))

            if pygame.sprite.collide_rect(player2, goal) and player2.landcheck() == True:
                clear = True
            
            if player2.rect.y > 640:
                group_pl2.empty()
                group_fl2.empty()
                group_gl.empty() 
                goal = Goal(goalfile, 0, -4604, 64, 64) 
                floorgoal = Goal(floorgoalfile, 0, -4540, 96, 32)
                group_gl.add(goal)
                group_gl.add(floorgoal)

                player2 = Player2(playerfile, 32, 490)
                group_pl2.add(player2)
                floorlist2 = []
                for i, j in zip(list_x, list_y):
                    floor2 = Floor2(floorfile2, i, j)
                    floor2.setimage(1)
                    floor2.setspeed(0)
                    floorlist2.append(floor2)
                group_fl2.add(floorlist2)
                player2.setfloor2(floorlist2)
                player2.setfloorgoal2(floorgoal)
            
            if clear == True:
                cleartimetext = font4.render(f"ClearTime:{time_at:>5.3f}",True, "white")
                surface.blit(cleartimetext, (300,16))
                cleartitletext = font4.render("Delete:タイトルへ",True, "white")
                surface.blit(cleartitletext, (300,50))

            #　更新処理
            display.update()               
            pygame.time.wait(25)
                   
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                for i in floorlist2:
                    i.rect.y -= player2.accel
                goal.rect.y -= player2.accel
                floorgoal.rect.y -= player2.accel
                if clear == True and pressed[K_DELETE]:
                    if scorejudge == True:
                        file = open("./score.txt","a")
                        file.write(str(time_at) + '\n')
                        file.close()
                    time_at = 0 
                    group_pl2.empty()
                    group_fl2.empty()
                    group_gl.empty() 
                    goal = Goal(goalfile, 0, -4604, 64, 64) 
                    floorgoal = Goal(floorgoalfile, 0, -4540, 96, 32)
                    group_gl.add(goal)
                    group_gl.add(floorgoal)

                    player2 = Player2(playerfile, 32, 490)
                    group_pl2.add(player2)
                    floorlist2 = []
                    for i, j in zip(list_x, list_y):
                        floor2 = Floor2(floorfile2, i, j)
                        floor2.setimage(1)
                        floor2.setspeed(0)
                        floorlist2.append(floor2)
                    group_fl2.add(floorlist2)
                    player2.setfloor2(floorlist2)
                    player2.setfloorgoal2(floorgoal)
                    clear = False
                    game.scene = "TITLE"
        
        if game.scene == "RANKING":
            # 背景表示
            group_bg.update()
            group_bg.draw(surface)

            scoretext1 = font.render("TIMEATACK",True, "white")
            surface.blit(scoretext1, (48,32))

            scoretext2 = font.render("MAINSTAGE",True, "white")
            surface.blit(scoretext2, (400,32))

            file01 = open("./score.txt", "r")   #読み取り専用
            list = file01.readlines()         #リストとして読み込む
            for i in list:
                i = i.strip()
                i = float(i)
                time_list.append(i)
            list = sorted(time_list,reverse=False)
            for data in list:
                score_count += 1
            for data in list:
                nomber += 1
                if data != " ":
                    score_tx = "No." + str(nomber) + "  " + f"{data:.3f}"
                if score_count2 < 5:
                    score_tx = font2.render(score_tx,True, "white")
                    surface.blit(score_tx, (48,score_y))
                score_y += 64
                score_count2 += 1
            file01.close()
            time_list = []
            score_y = 200
            score_count2 = 0
            nomber = 0

            file02 = open("./score2.txt", "r")   #読み取り専用
            list = file02.readlines()         #リストとして読み込む
            for i in list:
                i = i.strip()
                i = int(i)
                time_list.append(i)
            list = sorted(time_list,reverse=True)
            for data in list:
                score_count += 1
            for data in list:
                nomber += 1
                if data != " ":
                    score_tx = "No." + str(nomber) + "  " + str(data)
                if score_count2 < 5:
                    score_tx = font2.render(score_tx,True, "white")
                    surface.blit(score_tx, (400,score_y))
                score_y += 64
                score_count2 += 1
            file02.close()
            time_list = []
            score_y = 200
            score_count2 = 0
            nomber = 0

            pressed = pygame.key.get_pressed()
            if pressed[K_SPACE]:
                game.scene = "TITLE"      
                
            #　更新処理
            display.update()               
            pygame.time.wait(25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()