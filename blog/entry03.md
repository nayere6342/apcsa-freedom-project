# Entry #2: _Sprite Creation In PyGame_
## Nayer Ebraheim
## 2/2/26

### Intro:

Previously, I had been learning about level creation in pygame and how to bulid one. So now that there is a level to the remix game there has to be things within the level to make it shine. Therefore this level need to objects to be able to work. That's what I'm going over here, about sprites in my game. I will be going over how classes will be able to draw sprites with a X and Y axis.      

### Code Presentation:

To start off this code presentation, - Here is the full preview of the code;     

**Preview:**
```py
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


class Static(pg.sprite.DirtySprite):
    images: List[pg.Surface] = []

    def __init__(self):
        pg.sprite.DirtySprite.__init__(self)
        self.image = Static.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 3 * screen_dims[0] // 4)
        self.rect.y = randint(0, 3 * screen_dims[1] // 4)
```

### Design Process:

Now to break down the code        

### Challenges & Takeaways:

* A challenge I had while working on this was that it was hard to read the code examples online because I thought that pygame was a one to one copy of python but there are a ton of differences to it even though it's just a library.  

* Another challenge that was a real issue was I couldn't find the things I wanted to do like for example a player sprite being able to walk off screen and back. 

* A takeaway I got from this was that I should really start watching more and more videos about `pygame` to really understand how to work with it.

* The last takeaway I got from this was that I needed to tinker with `pygame` to help me to understand how to use it.
 

---
### Links:

* [Pygame Docs](https://www.pygame.org/docs/)
  
    * [Pygame Full Repo](https://github.com/pygame)
      
* [Entry Documents _(if needed)_](https://docs.google.com/document/d/1ZktrQPOmXlntU3Xlj_Qs1HKXNNFs5WKf7y7Y-o1phM0/edit?tab=t.0)

* [APCSA Notes](https://docs.google.com/document/d/1T4-EjM0x1HFrLtcUZF7B3Krb1lLYcnjwKDmR2nVX4wE/edit?tab=t.0#heading=h.g70gkuk13014)
---

[Previous](entry02.md) | [Next](entry04.md)

[Home](../README.md)
