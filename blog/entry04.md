# Entry #4: _Liquid Sims In PyGame_
## Flappy Bird: Absolute Remixed
## Nayer Ebraheim
## 3/13/26

### Intro:

Last entry I worked on the use of sprites in Adsolute Remixed, now I am talking about something that is similar too this. I will be talking about liquid sims. What they are is this: A liquid sim is a group of pixels that all have collision enabled to be able to move along there space. One question you may be asking is how will this affect the lag of the game? At a certain point it will start affecting lag but only if there are large sums of liquid on the space. One way I can render the liquid is by creating a ton of sprites in a small area. But this will cause the game to run slowly and may even crash the game itself. The way to be able to solve for this is by using a bitmap that stores compressed images in a way that doesn't cause lag. Another way I can also optimize the liquid sims is by only being rendered when the player in looking at it or       

### Code Presentation:


    
**Preview:**
```py
def main():

    pg.init()
    screen = pg.display.set_mode((640, 480), pg.HWSURFACE | pg.DOUBLEBUF)


    imagename = os.path.join(main_dir, "data", "liquid.bmp")
    bitmap = pg.image.load(imagename)
    bitmap = pg.transform.scale2x(bitmap)
    bitmap = pg.transform.scale2x(bitmap)


    if screen.get_bitsize() == 8:
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()


    anim = 0.0


    xblocks = range(0, 640, 20)
    yblocks = range(0, 480, 20)
    stopevents = pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN
    while True:
        for e in pg.event.get():
            if e.type in stopevents:
                return

        anim = anim + 0.02
        for x in xblocks:
            xpos = (x + (sin(anim + x * 0.01) * 15)) + 20
            for y in yblocks:
                ypos = (y + (sin(anim + y * 0.01) * 15)) + 20
                screen.blit(bitmap, (x, y), (xpos, ypos, 20, 20))

        pg.display.flip()
        time.sleep(0.01)
```

### Design Process:



### Skills: 



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

    * [Pygame Examples](https://github.com/pygame/pygame/tree/main/examples)

* [Pygame Patch Notes/Updates](https://www.pygame.org/news)

* [Pygame Wiki](https://www.pygame.org/wiki/)

* [Pygame Video Tutorials](https://www.youtube.com/@DaFluffyPotato/videos)

* [APCSA Notes](https://docs.google.com/document/d/1T4-EjM0x1HFrLtcUZF7B3Krb1lLYcnjwKDmR2nVX4wE/edit?tab=t.0#heading=h.g70gkuk13014)
---

[Previous](entry03.md) | [Next](entry05.md)

[Home](../README.md)
