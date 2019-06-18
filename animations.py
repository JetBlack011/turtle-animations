import turtle
from threading import Timer

sprites = []

class State:
    def __init__(self, delay, shapes):
        self.delay = delay
        self.shapes = shapes
        self.index = 0
        self.current_shape = self.shapes[self.index]
    
    def next(self):
        if self.index == len(self.shapes) - 1:
            self.index = 0
        else:
            self.index += 1
        self.current_shape = self.shapes[self.index]
  
    def run(self):
        def func_wrapper():
            self.run()
            self.next()
        self.timer = Timer(self.delay, func_wrapper)
        self.timer.start()
  
    def stop(self):
        if self.timer:
            self.timer.cancel()

class Sprite(turtle.Turtle):
    def __init__(self, states=None):
        super(Sprite, self).__init__()

        sprites.append(self)
    
        self.states = {}
        for key,state in states.iteritems():
            self.states[key] = State(state["delay"] / 1000.0, state["shapes"])
      
        self.current_state = None
    
    def set_state(self, identifier):
        if self.current_state:
            self.current_state.stop()
        self.current_state = self.states[identifier]
        self.current_state.run()
    
    def update(self):
        self.shape(self.current_state.current_shape)

def update():
    for sprite in sprites:
        sprite.update()

if __name__ == "main":
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

    shelly = Sprite(states)
    shelly.set_state('idle')

    while True:
        update()
        screen.update()