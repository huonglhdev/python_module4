import pgzrun
import time

start_time = time.time()
time_elapsed = 0

cow = Actor('abc')
cow.pos = 100,500

def draw():
    screen.clear() #xóa screen trước để screen sau chồng lên
    screen.blit('garden',(0,0))
    time_elapsed = int (time.time() - start_time)
    screen.draw.text("Garden happy for: " + str(time_elapsed) +" seconds",
                         topleft=(10,10), color="white")
    cow.draw()

def update():
    pass

pgzrun.go()
