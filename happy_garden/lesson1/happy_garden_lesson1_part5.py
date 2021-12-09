import pgzrun
import time

start_time = time.time()
time_elapsed = 0

game_over = False #kiểm tra game đã kết thúc chưa

cow = Actor("cow")
cow.pos = 100,500
def draw():
    global game_over
    if not game_over:
        screen.clear() #xóa screen trước để screen sau chồng lên
        screen.blit("garden",(0,0))
        cow.draw()
        time_elapsed = int (time.time() - start_time)
        screen.draw.text("Garden happy for: " + str(time_elapsed) +" seconds",
                             topleft=(10,10), color="white")

def

def add_flowers():
    global game_over
    if not game_over:
        new_flower()
        clock.schedule(add_flowers,4)
    return
    

#để chương trình game cập nhật liên tục, nghĩa là gọi hàm draw liên tục
def update():
    pass

pgzrun.go()
