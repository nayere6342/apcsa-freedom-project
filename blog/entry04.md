# Entry #4: _The Use Of Sprite In PyGame_
## Flappy Bird: Absolute Remixed
## Nayer Ebraheim
## 3/13/26

### Intro:

    

### Code Presentation:



**Preview:**
```py
def main():
    # initialize and setup screen
    pg.init()
    screen = pg.display.set_mode((640, 480), pg.HWSURFACE | pg.DOUBLEBUF)

    # load image and quadruple
    imagename = os.path.join(main_dir, "data", "liquid.bmp")
    bitmap = pg.image.load(imagename)
    bitmap = pg.transform.scale2x(bitmap)
    bitmap = pg.transform.scale2x(bitmap)

    # get the image and screen in the same format
    if screen.get_bitsize() == 8:
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()

    # prep some variables
    anim = 0.0

    # mainloop
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



### Use Cases: 



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

[Previous](entry03.md) | [Next](entry05.md)

[Home](../README.md)
