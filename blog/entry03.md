# Entry #3: _The Use Of Sprite In PyGame_
## Flappy Bird Absolute Remixed!
## Nayer Ebraheim
## 2/2/26

### Intro:

Previously, I had been learning about level creation in pygame and how to build one. So now that there is a level to the remix game there has to be things within the level to make it shine. Therefore this level needs objects to be able to work. That's what I'm going over here, about sprites in my game. I will be going over how classes will be able to draw sprites with a X and Y axis. As well as how even, logic can be put into these sprites to turn it into an enemy character or maybe even an NPC character.      

### Code Presentation:

To start off this code presentation, this code is meant to be how sprites are drawn into a scene using a class. How it should work is that it first draws a sprite and gives it a texture _(in this case an img tag)_. After that is done, a random integer is picked between a set number. So that at the end of the code the user will be able to see sprites at random parts of the screen. Here is the full preview of the code to learn more;     

**Preview:**
```py
class Thingy(pg.sprite.DirtySprite):
    images: List[pg.Surface] = ["egg.png"]

    def __init__(self):
        ##        pg.sprite.Sprite.__init__(self)
        pg.sprite.DirtySprite.__init__(self)
        self.image = Thingy.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, screen_dims[0])
        self.rect.y = randint(0, screen_dims[1])
        # self.vel = [randint(-10, 10), randint(-10, 10)]
        self.vel = [randint(-1, 1), randint(-1, 1)]
        self.dirty = 2

    def update(self, *args, **kwargs):
        for i in [0, 1]:
            nv = self.rect[i] + self.vel[i]
            if nv >= screen_dims[i] or nv < 0:
                self.vel[i] = -self.vel[i]
                nv = self.rect[i] + self.vel[i]
            self.rect[i] = nv


class Static(pg.sprite.DirtySprite):
    images: List[pg.Surface] = ["bird.png"]

    def __init__(self):
        pg.sprite.DirtySprite.__init__(self)
        self.image = Static.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 3 * screen_dims[0] // 4)
        self.rect.y = randint(0, 3 * screen_dims[1] // 4)
```

### Design Process:

Now to break down the code to show how this works. The first thing that happens is the sprite texture for this example is going to use a `egg.png` to show where the sprite is by using `images: List[pg.Surface] = ["egg.png"]` To give it that texture. Now the second part of the code deals with the random X and Y axis of the sprite. So every time the scene gets reloaded the sprite ends up in a different place `self.vel = [randint(-1, 1), randint(-1, 1)]` which will pick a random number between -1 and 1. At the very end of the code is another class that does a lot of the same things as the first class. It has a texture, it has a random X and Y axis but this time the random value is determined using the screen dimensions. Which is a different way of outputting a random X and Y axis.     

### Use Cases: 

One use case I could use in my project is a loot drop system. Where randomly loot can be drawn into the scene if let's say if the player gets to a certain level in the game or maybe even change how the pipes are drawn into the scene. Like for example having the pipe gap be smaller the higher level a player gets in the game. Which works in this game since it is a remix of the original flappy bird game.     

### Challenges & Takeaways:

* A challenge I had while working on this was that it was hard to read the code examples online because I thought that pygame was a one to one copy of python but there are a ton of differences to it even though it's just a library.  

* Another challenge that was a real issue was I couldn't find the things I wanted to do like for example a player sprite being able to walk off screen and back. 

* A takeaway I got from this was that I should really start watching more and more videos about `pygame` to really understand how to work with it.

* Another takeaway was that I needed a clear plan of what this game was going to be about since I didn't have one.

* The last takeaway from this was that I needed to tinker with `pygame` to help me to understand how to use it.
 

---
### Links:

* [Pygame Docs](https://www.pygame.org/docs/)
  
    * [Pygame Full Repo](https://github.com/pygame)
      
* [Entry Documents _(if needed)_](https://docs.google.com/document/d/1ZktrQPOmXlntU3Xlj_Qs1HKXNNFs5WKf7y7Y-o1phM0/edit?tab=t.0)

* [APCSA Notes](https://docs.google.com/document/d/1T4-EjM0x1HFrLtcUZF7B3Krb1lLYcnjwKDmR2nVX4wE/edit?tab=t.0#heading=h.g70gkuk13014)
---

[Previous](entry02.md) | [Next](entry04.md)

[Home](../README.md)






