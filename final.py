# debug: 地图生成，礼物生成分别放进set_bg, set_gift函数中

# debug: 新地图生成，上下移动的bomb命名为bomb1,左右移动的为bomb2,图相同，但为了判断而重命名
import pgzrun
import time

# 初始化全局变量
WIDTH = 1200
HEIGHT = 600

mario = Actor("mario_big")
mario.bottomleft = 320, 500
vx = 0  # x速度
vy = 0  # y速度
maxv = 6  # 最大速度
g = 0.5  # 重力加速度
jump = 15  # 跳跃初速度
walking = 0  # 是否在走路
direction = "right"
mario_jump=False
jumptimes=0

mario_die = Actor("mario_die")
mario_die.bottomleft = -1200, 550
vy_die = 0  # 死亡图片速度

gd = []  # 所有地面
gifts = []
enemies = []  # 小兵
traps = []  # 陷阱
flags = []
saves = []

life = 5  # 命数
score = 0  # 得分
savepoint = -1
win = False
move_bg = 0
ground_now = 600


class enemy(Actor):
    def __init__(self, **kwargs):
        super().__init__(image="enemy1", **kwargs)
        self.leftlimit = 0
        self.rightlimit = 2000
        self.uplimit = 100
        self.downlimit = 500
        self.v = 3
        self.use = True
        self.direction = "left"
        self.vy = 0

    def update(self):
        if self.direction == "left":
            if self.left >= self.leftlimit + self.v:
                self.left -= self.v
            else:
                if self.image == "turtle_left":
                    self.image = "turtle_right"
                self.direction = "right"
        elif self.direction == "right":
            if self.right <= self.rightlimit + self.v:
                self.right += self.v
            else:
                if self.image == "turtle_right":
                    self.image = "turtle_left"
                self.direction = "left"
        elif self.direction == "up":
            if self.top >= self.uplimit + self.v:
                self.bottom -= self.v
            else:
                self.direction = "down"
        elif self.direction == "down":
            if self.bottom <= self.downlimit - self.v:
                self.bottom += self.v
            else:
                self.direction = "up"
                
    def turtle_recover(self):
        if self.image=='turtle_hide':
            self.image='turtle_left'
            self.v=3


def set_bg():
    for i in range(0, 1500, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(1700, 2200, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(2400, 3000, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(3100, 3400, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(5000, 5600, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(5800, 6100, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(6200, 6400, 50):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    for i in range(6400, 8850, 600):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)
    ground = Actor("ground1")
    ground.bottomleft = 8850, 600
    gd.append(ground)
    for i in range(6700, 9000, 600):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 300
        gd.append(ground)
    for i in range(6550, 8800, 600):  # 设置关卡
        ground = Actor("ground1")
        ground.bottomleft = i, 450
        gd.append(ground)
    for i in range(9100,9300):
        ground = Actor("ground1")
        ground.bottomleft = i, 300
        gd.append(ground)
    
    for i in range(450, 800, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 400
        gd.append(ground)

    for i in range(450, 600, 50):
        ground = Actor("block2")
        ground.bottomleft = 500, i
        gd.append(ground)

    for i in range(400, 600, 50):
        ground = Actor("block2")
        ground.bottomleft = 1800, i
        gd.append(ground)
    for i in range(350, 600, 50):
        ground = Actor("block2")
        ground.bottomleft = 2300, i
        gd.append(ground)

    for i in range(3450, 3600, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 500
        gd.append(ground)
    for i in range(3650, 3800, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 400
        gd.append(ground)
    for i in range(3850, 4000, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 500
        gd.append(ground)
    for i in range(3850, 4000, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 200
        gd.append(ground)
    for i in range(4050, 4400, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 400
        gd.append(ground)
    for i in range(4550, 4900, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 200
        gd.append(ground)
    for i in range(5000, 5300, 50):
        ground = Actor("block2")
        ground.bottomleft = i, 400
        gd.append(ground)
    for i in range(9300,10800,50):
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)
    for i in range(10800,11000,50):
        ground = Actor("ground1")
        ground.bottomleft = i, 450
        gd.append(ground)
    for i in range(11550,12000,50):
        ground = Actor("ground1")
        ground.bottomleft = i, 600
        gd.append(ground)

    ground = Actor("block2")
    ground.bottomleft = 2200, 500
    gd.append(ground)
    ground = Actor("block2")
    ground.bottomleft = -1200, 600
    gd.append(ground)


def set_gift(savepoint_x=320):
    # 设置礼物
    gift = Actor("block1")
    gift.bottomleft = 920 - savepoint_x, 400
    gifts.append(gift)

    gift = Actor("block1")
    gift.bottomleft = 1020 - savepoint_x, 400
    gifts.append(gift)

    gift = Actor("block1")
    gift.bottomleft = 4170 - savepoint_x, 200
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 4220 - savepoint_x, 200
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 5320 - savepoint_x, 400
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 5370 - savepoint_x, 400
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 5420 - savepoint_x, 400
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 5470 - savepoint_x, 400
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 5520 - savepoint_x, 400
    gifts.append(gift)
    
    gift = Actor("block1")
    gift.bottomleft = 5570 - savepoint_x, 400
    gifts.append(gift)
    
    for i in range(2200,2500,50):
        for j in range(300,550,50):
            gift = Actor("coin")
            gift.bottomleft = i - savepoint_x, j
            gifts.append(gift)
            
    gift = Actor("coin")
    gift.bottomleft = 4170 - savepoint_x, 250
    gifts.append(gift)
    
    gift = Actor("coin")
    gift.bottomleft = 4220 - savepoint_x, 250
    gifts.append(gift)
    
    gift = Actor("coin")
    gift.bottomleft = 4170 - savepoint_x, 300
    gifts.append(gift)
    
    gift = Actor("coin")
    gift.bottomleft = 4220 - savepoint_x, 300
    gifts.append(gift)
    
    gift = Actor("coin")
    gift.bottomleft = 4170 - savepoint_x, 350
    gifts.append(gift)
    
    gift = Actor("coin")
    gift.bottomleft = 4220 - savepoint_x, 350
    gifts.append(gift)


def set_enemy(savepoint_x=320):
    # 设置小兵
    aenemy = enemy()
    aenemy.bottomleft = 1120 - savepoint_x, 550
    aenemy.leftlimit = 870 - savepoint_x
    aenemy.rightlimit = 1520 - savepoint_x
    enemies.append(aenemy)

    aenemy = enemy()
    aenemy.bottomleft = 2220 - savepoint_x, 550
    aenemy.leftlimit = 2170 - savepoint_x
    aenemy.rightlimit = 2520 - savepoint_x
    enemies.append(aenemy)

    aenemy = enemy()
    aenemy.image = "turtle_left"
    aenemy.bottomleft = 2720 - savepoint_x, 550
    aenemy.leftlimit = 2670 - savepoint_x
    aenemy.rightlimit = 3320 - savepoint_x
    enemies.append(aenemy)

    aenemy = enemy()
    aenemy.v=3
    aenemy.bottomleft = 5400 - savepoint_x, 350
    aenemy.leftlimit = 5300 - savepoint_x
    aenemy.rightlimit = 5600 - savepoint_x
    enemies.append(aenemy)

    aenemy = enemy()
    aenemy.v=0
    aenemy.bottomleft = 7320 - savepoint_x, 550
    aenemy.leftlimit = 7320 - savepoint_x
    aenemy.rightlimit = 7320 - savepoint_x
    enemies.append(aenemy)
    
    aenemy = enemy()
    aenemy.image = "turtle_left"
    aenemy.bottomleft = 9200 - savepoint_x, 550
    aenemy.leftlimit = 9100 - savepoint_x
    aenemy.rightlimit = 9250 - savepoint_x
    enemies.append(aenemy)
    
    for i in range(10):
        aenemy = enemy()
        aenemy.image = "turtle_left"
        aenemy.bottomleft = 9650 - savepoint_x + i*300, 550
        aenemy.v=2+0.5*i
        if i//2:
            aenemy.direvtion='left'
        else:
            aenemy.direvtion='right'
        aenemy.leftlimit = 9620 - savepoint_x
        aenemy.rightlimit = 11120 - savepoint_x
        enemies.append(aenemy)
    


def set_trap(savepoint_x=320):
    # 设置陷阱
    aenemy = enemy()
    aenemy.image = "bomb1"
    aenemy.bottomleft = 970 - savepoint_x, 350
    aenemy.uplimit = 100
    aenemy.downlimit = 500
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    # right left
    aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 2450 - savepoint_x, 450
    aenemy.leftlimit = 2200 - savepoint_x
    aenemy.rightlimit = 2500 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    
    aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 3720 - savepoint_x, 550
    aenemy.leftlimit = 3220 - savepoint_x
    aenemy.rightlimit = 3820 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    # up down
    aenemy = enemy()
    aenemy.image = "bomb1"
    aenemy.bottomleft = 3920 - savepoint_x, 350
    aenemy.leftlimit = 3920 - savepoint_x
    aenemy.rightlimit = 3920 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    # unvisible block * 3
    aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 4270 - savepoint_x, 480
    aenemy.leftlimit = 4220 - savepoint_x
    aenemy.rightlimit = 4320 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 4270 - savepoint_x, 380
    aenemy.leftlimit = 4220 - savepoint_x
    aenemy.rightlimit = 4320 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 4270 - savepoint_x, 280
    aenemy.leftlimit = 4220 - savepoint_x
    aenemy.rightlimit = 4320 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    
    aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 5400 - savepoint_x, 450
    aenemy.leftlimit = 5300 - savepoint_x
    aenemy.rightlimit = 5800 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    
    aenemy = enemy()
    aenemy.image = "bomb1"
    aenemy.bottomleft = 8010 - savepoint_x, 370
    aenemy.leftlimit = 8010 - savepoint_x
    aenemy.rightlimit = 8010 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)
    
    '''aenemy = enemy()
    aenemy.image = "bomb2"
    aenemy.bottomleft = 8610 - savepoint_x, 370
    aenemy.leftlimit = 8400 - savepoint_x
    aenemy.rightlimit = 8900 - savepoint_x
    aenemy.v = 0
    aenemy.vy = 0
    aenemy.use = False
    traps.append(aenemy)'''
    
    for i in range(5):
        aenemy = enemy()
        aenemy.image = "bomb2"
        aenemy.bottomleft = 9600+i*300 - savepoint_x, 550-i*80
        aenemy.leftlimit = 9500- savepoint_x
        aenemy.rightlimit = 11150 - savepoint_x
        aenemy.v = 0
        aenemy.vy = 0
        aenemy.use = False
        traps.append(aenemy)


def set_save():
    save0 = Actor("save")
    save0.bottomleft = 320, 550
    saves.append(save0)

    save1 = Actor("save")
    save1.bottomleft = 3700, 350
    saves.append(save1)
    
    save2 = Actor("save")
    save2.bottomleft = 6400, 550
    saves.append(save2)
    
    save3 = Actor("save")
    save3.bottomleft = 9100, 250
    saves.append(save3)
    
    save4 = Actor("save")
    save4.bottomleft = 10900, 400
    saves.append(save4)



def set_flag():
    flag = Actor("flag")
    flag.bottomleft = 11900, 550
    flags.append(flag)


def set_all():  # 设置地图
    set_bg()
    set_gift()
    set_enemy()
    set_trap()
    set_flag()
    set_save()
    sounds.theme.stop()
    sounds.theme.play(-1)


def reset_lives(savepoint_x):  # 重新设置活动对象
    gifts.clear()
    set_gift(savepoint_x)
    enemies.clear()
    set_enemy(savepoint_x)
    traps.clear()
    set_trap(savepoint_x)


def on_ground():  # 判断是否在地面
    global gd, mario, jumptimes
    for i in gd:
        if (
            i.collidepoint(mario.midbottom)
            and i.bottom > mario.bottom > i.top > mario.top
            and last_bottom <= i.top
        ):
            jumptimes=0
            return True
        # if i.colliderect(mario.midbottom) and mario.bottom==i.top+1:
        #    return True
    return False


def top_collide():  # 判断上部碰撞
    global gd, mario
    for i in gd:
        if mario.colliderect(i) and i.top < mario.top <= i.bottom < mario.bottom:
            return True
    return False


def left_collide():  # 判断左边碰撞
    global gd, mario
    for i in gd:
        if (
            mario.colliderect(i)
            and i.left < mario.left <= i.right < mario.right
            and not last_bottom <= i.top + 1
        ):
            mario.left += 7
            return True
    return False


def right_collide():  # 判断右边碰撞
    global gd, mario
    for i in gd:
        if (
            mario.colliderect(i)
            and i.right > mario.right >= i.left > mario.left
            and not last_bottom <= i.top + 1
        ):
            mario.left -= 7
            return True
    return False


def die():  # 死亡
    global vx, vy, vy_die
    mario.image = "mario_die"
    mario_die.bottomleft = mario.left, mario.bottom
    a = gd[0].left
    mario.bottomleft = a - 1200, 550
    vy_die = -20
    vx = 0
    vy = 0
    stop_move()
    walking = 0
    clock.unschedule(walk)
    sounds.theme.stop()
    sounds.die.play()


def death_animation():  # 死亡动画
    global vy_die
    if life > 0:
        vy_die += 0.5
        mario_die.bottom += vy_die
        if mario_die.bottom >= 700:
            refresh()
            return


def refresh():  # 复活
    global life, vx, vy, vy_die, score, savepoint
    life -= 1
    if life > 0:
        vx = 0
        vy = 0
        vy_die = 0
        distance_back = 320 - saves[savepoint].left
        savepoint_height = saves[savepoint].bottom
        savepoint_x = saves[savepoint].left - gd[0].left
        for i in gd + flags + saves:
            i.left += distance_back
        score = 0
        walking = 0
        reset_lives(savepoint_x)
        mario.image = "mario_big"
        mario.bottomleft = 320, savepoint_height
        mario_die.bottomleft = gd[0].left - 1200, 550
        sounds.theme.play(-1)
    
    else:
        sounds.fail.play()

def set_mario_normal():
    global mario_jump
    mario_jump=False

def move_mario():  # 控制mario运动
    global vx, vy, maxv, g, jump, last_bottom, jumptimes, mario_jump
    if mario.image == "mario_die":  # 死亡动画
        death_animation()
    # 左右移动
    else:
        if keyboard.left and keyboard.right:
            vx = 0
        elif keyboard.left:  # 向左运动
            if left_collide():
                vx = 0
            elif mario.left <= 0:
                vx = 0
            elif vx > -maxv:
                vx -= 1
            mario.left += vx
        elif keyboard.right:  # 向右运动
            if right_collide():
                vx = 0
            elif vx < maxv:
                vx += 1
            mario.left += vx
        else:  # 停止
            if on_ground():
                vx = 0
        # 上下移动
        if (on_ground() or (mario.left-gd[0].left>10900 and jumptimes<2 and mario_jump==False)) and keyboard.a:  # 只有落地可以跳跃
            vy = -jump
            mario_jump=True
            jumptimes+=1
            last_bottom = mario.bottom
            mario.bottom += vy
            clock.schedule_unique(set_mario_normal,1)
        elif not on_ground():
            if vy < 14.5:
                vy += g
            last_bottom = mario.bottom
            mario.bottom += vy
            if mario.top <= 0:
                vy = 0
        else:
            vy = 0
        if top_collide():
            vy = abs(vy)


def check_underground():  # 检查是否低于地面
    global gd, mario, ground_now
    for i in gd:
        if (
            mario.colliderect(i)
            and i.bottom > mario.bottom > i.top > mario.top
            and last_bottom <= i.top
        ):
            ground_now = i.top
            return True
        if mario.colliderect(i) and mario.bottom == i.top + 1:
            ground_now = i.top
            return True
    return False


# 判断是否触发
def nearby():
    global mario
    for i in traps:
        if i.image == "bomb1" and mario.distance_to(i) <= 150 and i.use == False:
            i.v = 3
            i.direction = "up"
            i.use = True
        if i.image == "bomb2" and mario.distance_to(i) <= 150 and i.use == False:
            if (
                i.bottomleft[1] == 280
                or i.bottomleft[1] == 380
                or i.bottomleft[1] == 480
            ):
                i.v = 0
                i.direction = "left"
                i.use = True
            else:
                i.v = 2
                i.direction = "left"
                i.use = True
    return True


def judge_trap_used():
    for i in traps:
        pass
        """
        if i.image == 'bomb' and i.bottomleft[0] <= i.leftlimit + 5 or i.image == 'bomb' and i.bottomleft[0] >= i.rightlimit - 5:
            i.v = 0
        """
        # if i.image == 'bomb' and i.bottomleft[0] >= i.rightlimit - 100 or i.image == 'bomb' and i.bottom <= i.uplimit:
        # i.v = 0
        # i.vy = 0
    return False


# 处理移动时的动画
def set_stop():
    if direction == "right":
        mario.image = "mario_big"
    else:
        mario.image = "mario_left"
    clock.unschedule(walk)


def walk():
    if mario.image == "mario_big":
        mario.image = "mario_walk"
    elif mario.image == "mario_walk":
        mario.image = "mario_big"
    elif mario.image == "mario_walkleft":
        mario.image = "mario_left"
    elif mario.image == "mario_left":
        mario.image = "mario_walkleft"


# 获取金币
def get_gift():
    global score,life
    for i in gifts:
        if i.image == "block1":
            if (
                mario.colliderect(i) and i.top < mario.top <= i.bottom < mario.bottom
            ):  # 只有从下面接触才会产生金币
                i.image = "coin"
                i.top -= 50
        elif i.image == "coin":
            if mario.colliderect(i):
                score += 1
                if score>=50 and score%50==0:
                    life+=1
                gifts.remove(i)


def hurt():  # 受到伤害
    global life, score, vy,life
    for i in enemies + traps:
        if i.image == "enemy3" or i.image == "turtle_died":
            i.v = 0
            i.vy += 0.5
            i.bottom += i.vy
            if i.bottom >= 700:
                enemies.remove(i)
        elif mario.colliderect(i):
            if mario.bottom <= i.top + 15:
                if i.image == "enemy1":
                    # 敌人死亡
                    i.image = "enemy3"
                    score += 1
                    if score>=50 and score%50==0:
                        life+=1
                elif i.image == "turtle_left" or i.image == "turtle_right":
                    i.image = "turtle_hide"
                    v0 = i.v
                    i.v = 0
                    vy = -15
                    mario.bottom-=15
                    clock.schedule_unique(i.turtle_recover, 5)
                elif i.image == "turtle_hide":
                    vy = -15
                    i.image = "turtle_died"
                    mario.bottom-=15
                    score += 2
                    if score>=50 and score%50==0:
                        life+=1
                else:
                    die()
            else:
                die()


def fall():  # 失足坠落
    global life
    if mario.bottom >= 700 and life > 0:
        die()


# 控制背景的移动
def move_all():
    global mario, move_bg
    if mario.left > 900 and mario.image != "mario_die":
        move_bg = 1
        clock.schedule(stop_move, 1)
    elif mario.left < 300 and mario.image != "mario_die":
        move_bg = 2
        clock.schedule(stop_move, 1)
    if move_bg == 1:
        mario.left -= 10
        for i in gd + gifts + enemies + traps + flags + saves:
            i.left -= 10
        for i in enemies + traps:
            i.leftlimit -= 10
            i.rightlimit -= 10
    elif move_bg == 2:
        mario.left += 10
        for i in gd + gifts + enemies + traps + flags + saves:
            i.left += 10
        for i in enemies + traps:
            i.leftlimit += 10
            i.rightlimit += 10


def stop_move():
    global move_bg
    move_bg = 0


def clear_all():
    screen.clear()
    gd.clear()
    gifts.clear()
    enemies.clear()
    traps.clear()
    flags.clear()
    saves.clear()


def game_over():
    clear_all()
    sounds.duel.play()
    screen.blit(images.trap_card, (200, 30))
    screen.draw.text("GAME OVER!", (400, 300), color="red", fontsize=96)
    screen.draw.text("Press R to RESTART", (950, 10), color="white", fontsize=36)
    if keyboard.r:
        sounds.duel.stop()
        reset_all()


def game_win():
    screen.draw.text("YOU WIN!", (400, 300), color="red", fontsize=96)
    screen.draw.text("Press R to RESTART", (950, 50), color="white", fontsize=36)
    if keyboard.r:
        clear_all()
        reset_all()


def reset_all():
    global life, score, direction, move_bg, ground_now, win, savepoint, mario_jump, jumptimes
    screen.draw.text("GAME RESTART!", (400, 300), color="red", fontsize=96)
    life = 5  # 命数
    score = 0  # 得分
    walking = 0  # 是否在走路
    direction = "right"
    move_bg = 0
    ground_now = 600
    mario_jump=False
    jumptimes=0
    set_all()
    mario.image = "mario_big"
    mario.bottomleft = 320, 550
    mario_die.bottomleft = -1200, 550
    savepoint = -1
    win = False


def draw():
    global life, score, direction, move_bg, ground_now, win, savepoint
    if life > 0:
        screen.clear()
        screen.fill((0, 200, 255))
        screen.draw.text("LIFE:%d" % life, (800, 10), fontsize=48)
        screen.draw.text("SCORE:%d" % score, (1000, 10), fontsize=48)
        screen.draw.text("press 'left' and 'right' keys",(80+gd[0].left, 70),fontsize=45)
        screen.draw.text("to control the direction,",(80+gd[0].left, 150),fontsize=45)
        screen.draw.text("press 'a' to jump",(80+gd[0].left, 230),fontsize=45)
        screen.draw.text("jump on top of enemies to kill them",(700+gd[0].left, 150),fontsize=45)
        screen.draw.text("now you can jump twice!!",(10900+gd[0].left, 150),fontsize=45)
        for i in gd + gifts + enemies + flags + saves:
            i.draw()
        for i in traps:
            if i.use:
                i.draw()

        mario.draw()
        mario_die.draw()
    else:
        game_over()

    if win:
        game_win()


def update():
    global move_bg, life, ground_now, win, savepoint
    if win:
        return
    left_collide()
    right_collide()
    nearby()
    judge_trap_used()
    for i in enemies + traps:
        i.update()
    move_mario()
    if check_underground():
        mario.bottom = ground_now + 1

    move_all()

    for i in flags:
        if mario.collidepoint(i.midbottom):
            win = True
            print("you win")
    for i in saves:
        if mario.collidepoint(i.midbottom) and i.image == "save":
            i.image = "load"
            savepoint += 1
    get_gift()
    hurt()
    fall()


def on_key_down(key):
    global walking, direction
    if key == keys.LEFT:
        walking += 1
        direction = "left"
        if mario.image != "mario_die":
            mario.image = "mario_left"
            clock.schedule_interval(walk, 0.1)
    if key == keys.RIGHT:
        walking += 1
        direction = "right"
        if mario.image != "mario_die":
            mario.image = "mario_big"
            clock.schedule_interval(walk, 0.1)
    if walking >= 2:
        clock.unschedule(walk)


def on_key_up(key):
    global walking
    if key == keys.LEFT:
        walking -= 1
        if mario.image != "mario_die":
            set_stop()
    if key == keys.RIGHT:
        walking -= 1
        if mario.image != "mario_die":
            set_stop()
    if walking == 1:
        clock.schedule_interval(walk, 0.1)


set_all()


pgzrun.go()
