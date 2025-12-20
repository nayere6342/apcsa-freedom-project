# Entry #2: Level Creation For Pygame 
## Nayer Ebraheim
## 12/19/25

### Intro:

Previously, the main thing I talked about was that I have been working with the python-type game engine called `pygame`. Which uses python as a frame for this game engine. What this import does is it adds a new class which can be used for game objects. But one major thing I realized was that `pygame` isn't a game engine, but instead a game engine. It's actually a library. What a library in python does, it is just a large group of super classes in a series. To put that aside, the main thing that I will go over is making a level on the window. Which is something I will be using for my flappy bird remix.      

### Code Presentation:

To start off this 

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

```

### Design Process:

 

### Challenges & Takeaways:

* 

* 

* 

* 
 

---
### Links:

* 

---

[Previous](entry01.md) | [Next](entry03.md)

[Home](../README.md)


