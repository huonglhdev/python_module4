
import pgzrun
import random

WIDTH = 800
HEIGHT = 550
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

say_dance = False
show_countdown = False
moves_complete = False
game_over = False

move_list = []
display_list = []

score = 0
count = 4
current_move = 0
dance_length = 4

dancer = Actor('dancer-start')
dancer.pos = (CENTER_X + 5,CENTER_Y - 20)
up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170
midoriya = Actor('midoriya')
midoriya.pos = CENTER_X - 150, CENTER_Y + 20
def draw():
    global game_over, say_dance, show_countdown
    global score, count
    if not game_over:
        screen.clear()
        screen.blit('stage', (0,0))
        screen.draw.text('Score: '+ str(score), color='black', topleft=(10,10))
        dancer.draw()
        up.draw()
        right.draw()
        left.draw()
        down.draw()
        midoriya.draw()
        if say_dance:
            screen.draw.text('Dance!!', color = 'black', topleft=(CENTER_X - 70, CENTER_Y - 40), fontsize = 60)
        if show_countdown:
            screen.draw.text(str(count), color = 'black', topleft=(CENTER_X - 5,CENTER_Y - 80),fontsize = 40)
    else:
        screen.clear()
        screen.blit('stage',(0,0))
        screen.draw.text('Score: '+ str(score), color='black', topleft=(10,10))
        screen.draw.text('Game Over!', color='black',topleft=(CENTER_X - 95,CENTER_Y - 20), fontsize=50)
    return


def update_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            dancer.image = 'dancer-up'
            midoriya.image = 'midoriya2'
            up.image = 'up-lit'
            clock.schedule(reset_game,0.5)
        elif move == 1:
            dancer.image = 'dancer-right'
            midoriya.image = 'midoriya3'
            right.image = 'right-lit'
            clock.schedule(reset_game,0.5)
        elif move == 2:
            dancer.image = 'dancer-left'
            midoriya.image = 'midoriya4'
            left.image = 'left-lit'
            clock.schedule(reset_game,0.5)
        else:
            dancer.image = 'dancer-down'
            midoriya.image = 'midoriya5'
            down.image = 'down-lit'    
            clock.schedule(reset_game,0.5)
    return

def reset_game():
    global game_over
    if not game_over:
        midoriya.image = 'midoriya'
        dancer.image = 'dancer-start'
        up.image = 'up'
        right.image = 'right'
        left.image = 'left'
        down.image = 'down'
    return

def on_key_up(key):
    global game_over, score
    if key == keys.UP:
        update_dancer(0)
        if move_list[current_move] == 0:
            score += 1
            next_move()
    elif key == keys.RIGHT:
        update_dancer(1)
        if move_list[current_move] == 1:
            score += 1
            next_move()
    elif key == keys.LEFT:
        update_dancer(2)
        if move_list[current_move] == 2:
            score += 1
            next_move()
    elif key == keys.DOWN:
        update_dancer(3)
        if move_list[current_move] == 3:
            score += 1
            next_move()
    return

#music.play('vanishing-horizon')
sounds.rap.play()

def display_moves():
    global display_list
    global say_dance, show_countdown
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves,1)
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves,1)
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves,1)
        elif this_move == 3:
            update_dancer(3)
            clock.schedule(display_moves,1)
    else:    
        say_dance = True
        show_countdown = False
    return

def countdown():
    global show_countdown, count
    if count > 1:
        count = count - 1
        clock.schedule(countdown,1)
    else:
        show_countdown = False
        display_moves()
    return



def generate_moves():
    global display_list, move_list
    global dance_length, show_countdown
    
    move_list = []
    for i in range(dance_length):
        random_move = random.randint(0,3)
        display_list.append(random_move)
        move_list.append(random_move)
    show_countdown = True
    countdown()
    return

generate_moves()    

def next_move():
    global current_move, dance_length, moves_complete
    if current_move < dance_length - 1:
        current_move += 1
    else:
        moves_complete = True
    return 


def update():
    global game_over, moves_complete, current_move
    if not game_over:
        if moves_complete:
            generate_moves()
            current_move = 0
            moves_complete = False
    else:
        #music.stop()
        sounds.rap.stop()




pgzrun.go()

