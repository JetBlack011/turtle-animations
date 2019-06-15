import turtle
from threading import Timer

class State:
    def __init__(self, delay, shapes, controller):
        self.delay = delay
        self.shapes = shapes
        self.controller = controller
        self.index = 0
        self.current_shape = self.shapes[self.index]
    
    def next(self):
        if self.index == len(self.shapes) - 1:
            self.index = 0
        else:
            self.index += 1
        self.current_shape = self.shapes[self.index]
        self.controller.shape(self.current_shape)
  
    def run(self):
        def func_wrapper():
            self.run()
            self.next()
        self.timer = Timer(self.delay, func_wrapper)
        self.timer.start()
  
    def stop(self):
        if self.timer:
            self.timer.cancel()

class Controller(turtle.Turtle):
    def __init__(self, states):
        super(Controller, self).__init__()
    
        self.states = {}
        for key,state in states.iteritems():
            self.states[key] = State(state["delay"] / 1000.0, state["shapes"], self)
      
        self.current_state = None
    
    def set_state(self, identifier):
        if self.current_state:
            self.current_state.stop()
        self.current_state = self.states[identifier]
        self.current_state.run()

def set_sprite(self, sprite):
    self.sprite = sprite

setattr(turtle.Turtle, 'set_sprite', set_sprite)