from random import randint
import pgzrun
import time

WIDTH = 800
HEIGHT = 600
start_time = time.time()
time_elapsed = 0

game_over = False #kiểm tra game đã kết thúc chưa

flower_list = []
wilted_list = []

cow = Actor("cow")
cow.pos = 100,500

def draw():
    global game_over
    if not game_over:
        screen.clear() #xóa screen trước để screen sau chồng lên
        screen.blit("garden",(0,0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        time_elapsed = int (time.time() - start_time)
        screen.draw.text("Garden happy for: " + str(time_elapsed) +" seconds",
                             topleft=(10,10), color="white")

def new_flower():
    global flower_list, wilted_list
    flower_new = Actor("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    flower_list.append(flower_new)
    wilted_list.append("happy")
    return

def add_flowers():
    global game_over
    if not game_over:
        new_flower()
        clock.schedule(add_flowers, 4)
    return

def wilt_flower():
    global flower_list, wilted_list, game_over
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list)-1)
            if flower_list[rand_flower].image == "flower":
                flower_list[rand_flower].image = "flower-wilt"
                wilted_list[rand_flower] = time.time()
        clock.schedule(wilt_flower, 3)
    return

add_flowers()
wilt_flower()

#để chương trình game cập nhật liên tục, nghĩa là gọi hàm draw liên tục
def update():
    pass

pgzrun.go()
