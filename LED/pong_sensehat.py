from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

y = 4
ball_position = [randint(2,6), randint(1,6)]
ball_velocity = [1,1]
score = 0

def draw_bat():
    sense.set_pixel(0,y,0,0,255)
    sense.set_pixel(0,y+1,0,0,255)
    sense.set_pixel(0,y-1,0,0,255)
    
R = [255,0,0]
N = [0,0,0]
    
game_over = [
R,R,R,R,R,R,R,R,
R,R,N,N,N,N,R,R,
R,N,R,N,N,R,N,R,
R,N,N,R,R,N,N,R,
R,N,N,R,R,N,N,R,
R,N,R,N,N,R,N,R,
R,R,N,N,N,N,R,R,
R,R,R,R,R,R,R,R,
]
    
    
def move_up(event):
    global y
    # als y (i.e. middelpunt van de bat) groter is dan 1 kunnen we nog omhoog verschuiven
    # zoniet beweegt de bat niet meer
    if y > 1 and event.action == 'pressed':
        y -= 1
        
def move_down(event):
    global y
    # als y kleiner is dan 6 kunnen we nog omlaag verschuiven
    if y < 6 and event.action == 'pressed':
        y += 1
    
    
def draw_ball():
    global score
    global active_game
    sense.set_pixel(ball_position[0], ball_position[1], 0,255,0)
    # verschuiven naar volgende positie
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    
    if ball_position[0] == 7:
        # als de bal het plafond raakt, keren we de velocity om
        ball_velocity[0] = -ball_velocity[0]
        
    if ball_position[1] == 0 or ball_position[1] == 7:
        # als de bal de zijkanten raakt, keren we de velocity om
        ball_velocity[1] = -ball_velocity[1]
        
    if ball_position[0] == 0:
        # game over
        sleep(0.25)
        sense.set_pixels(game_over)
        sleep(1)
        sense.show_message(str(score), text_colour=[0,255,0], scroll_speed=0.5)
        quit()
        
    if ball_position[0] == 1 and y-1 <= ball_position[1] <= y + 1:
        ball_velocity[0] = -ball_velocity[0]
        score += 1
    
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
    
while True:
    sense.clear()
    draw_bat()
    draw_ball()
    sleep(0.5)