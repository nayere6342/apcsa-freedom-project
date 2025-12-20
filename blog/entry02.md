# Entry #2: Level Creation For Pygame 
## Nayer Ebraheim
## 12/19/25

### Intro:

Previously, the main thing I talked about was that I have been working with the python-type game engine called `pygame`. Which uses python as a frame for this game engine. What this import does is it adds a new class which can be used for game objects. But one major thing I realized was that `pygame` isn't a game engine, but instead a game engine. It's actually a library. What a library in python does, it is just a large group of super classes in a series. To put that aside, the main thing that I will go over is making a level on the window. Which is something I will be using for my flappy bird remix.      

### Code Presentation:

To start off this code presentation, what this code is meant to do is it will draw test sprites onto the screen. With these sprites on screen it needs info. For example an image id for that sprite will give it more character. The next thing that this sprite needs is a hitbox without a hitbox. It will not hit into anything. The last thing for this sprite will have to be its cords with the use of cords, that will be able to control where it gets drawn. Here is the full preview of the code;     

**Preview:**
```py
...
class Thingy(pg.sprite.DirtySprite):
    images: List[pg.Surface] = []

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

```

### Design Process:

Now to break down the code the main part of this code that leads the rest is the class itself. What it does is it first gives the sprite an image so that the player can see it, using: `self.image = Thingy.images[0]` to draw that sprite image onto the screen. Now the second thing that happens in this code is the hitbox, this gives the sprite the ability to hit into other things. By using: `self.rect.x = randint(0, screen_dims[0])` and `self.rect.y = randint(0, screen_dims[1])` it can determine the placement of it. The third part of the code that starts is the cords on the sprite. This gives the points where the sprite is supposed to go. And last if not final, the randomizer, it takes the sprite and draws it somewhere random. That's when it will give that sprite a set speed and once that sprite hits the edge of the screen it bounces off at the same speed. With the help of: `if nv >= screen_dims[i] or nv < 0: self.vel[i] = -self.vel[i] nv = self.rect[i] + self.vel[i] self.rect[i] = nv` it is able do that.       

### Challenges & Takeaways:

* A challenge I had while working on this was that it was hard to read the code examples online because I thought that pygame was a one to one copy of python but there are a ton of differences to it even though it's just a library.  

* Another challenge that was a real issue was I couldn't find the things I wanted to do like for example a player sprite being able to walk off screen and back. 

* A takeaway I got from this was that I should really start watching more and more videos about `pygame` to really understand how to work with it.

* The last takeaway I got from this was that I needed to tinker with `pygame` to help me to understand how to use it.
 

---
### Links:

* [Pygame Docs](https://www.pygame.org/docs/)
  
    * [Pygame Full Repo](https://github.com/pygame)
      
* [Entry Doc-Linked (if needed)](https://docs.google.com/document/d/1ZktrQPOmXlntU3Xlj_Qs1HKXNNFs5WKf7y7Y-o1phM0/edit?tab=t.0)

* [APCSA Notes](https://docs.google.com/document/d/1lbayMtmDyH7MgIe7xswbOX3LFzTGywgk4ORcd6p4cm0/edit?tab=t.0#heading=h.6o1f62qg6jz9)
---

[Previous](entry01.md) | [Next](entry03.md)

[Home](../README.md)



