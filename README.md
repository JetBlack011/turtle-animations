# turtle-animations

A very simple wrapper enabling animations in the turtle library. Works via a collection of state machines working on separate threads to manipulate the current shape as which a turtle appears.

## Usage

Normally, to create a turtle object on the screen and change its shape, one would do as such:
```
shelly = turtle.Turtle()
shelly.shape('image.gif')
```
In this wrapper, the Sprite class inherits from Turtle and adds a number of useful methods allowing for the inclusion of "states" within the member. Adding/changing states is accomplished by calling those respective methods:
```
shelly = animations.Sprite()
shelly.add_state('idle', 100, ['idle01.gif', 'idle02.gif', 'idle03.gif'])
shelly.set_state('idle')
```
A Sprite can have as many states as desired, and they can alternatively be defined using a dictionary if there are a significant number of images for each state to rotate through:
```
states = {
  'idle' : {
      'delay' : 100,
      'shapes' : ['idle01.gif', 'idle02.gif', 'idle03.gif']
  }
}

shelly = animations.Sprite(states)
shelly.set_state('idle')
```
States have an identifier, a delay per frame, and a list of shapes to rotate through. The `Sprite.add_state()` method takes these three values, respectively, as arguments. In addition, in order for any of the shapes to change, the static method `update()` must be called inside of the main game loop:
```
shelly = animations.Sprite()
shelly.add_state('idle', 100, ['idle01.gif', 'idle02.gif', 'idle03.gif'])
shelly.set_state('idle')

while True:
    animations.update()
```
This method updates all Sprite's associated shape to the current state's shape, and is required purely because graphical elements cannot be manipulated outside of the main thread (i.e. on that used to update the state's shape).
