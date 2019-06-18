import turtle
import animations
import os

screen = turtle.Screen()
screen.tracer(0)

sprites = os.getcwd() + '/sprites'
os.chdir(sprites + '/left')
screen.addshape('duck_down_l.gif')
screen.addshape('duck_up_l.gif')
screen.addshape('idle_l.gif')
screen.addshape('jump_l.gif')
screen.addshape('move_right_l.gif')
screen.addshape('punch_l.gif')

states = {
    'idle' : {
        'delay' : 100,
        'shapes' : ['duck_down_l.gif', 'duck_up_l.gif', 'idle_l.gif']
    },
    'attack' : {
        'delay' : 100,
        'shapes' : ['duck_down_l.gif', 'duck_up_l.gif', 'idle_l.gif']
    },
}

shelly = animations.Sprite(states)
shelly.set_state('idle')

while True:
    animations.update()
    screen.update()