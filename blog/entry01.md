# Entry 1
Nayer Ebraheim 11/3/25

## **Intro:**

For my first blog entry, I have been working with the python-type game engine called `pygame`. Which uses python as a frame for this game engine. What this import does is it adds a new class which can be used for game objects. Such as player movement, small classes like that can be useful to make anything from a 2d platformer to an entire story based game. I know it might sound crazy coming from a simple python import but it can do so much. Since it can stand on its own two legs it will be useful for my _flappy bird remix_ style game.    

### **Code Presentation:**

For a bit of context, since this is earlier in development the code may seem unorganized. But I'm still fixing it and making changes to the code. Since I'm learning the basics of `pygame` I have to start small. So the first thing I did was that I needed to learn how to install `pygame` in the first place. After that I used `pip3` which is an updated version of `pip`. Once that was finished, I started learning how to make a window. Which is simple then it sounds. All I needed to do was get a class called `window = (...)` which is needed to define the entire game. Here is a quick preview of the code; 

**Preview:**
```py
window = Tk()
window.title("new pygame window")
window.resizable(False, False)
score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score))
window.mainloop()
```

### **Design Process:** 

The first thing that happens is creating a class that handles GUI. In this case using `tkinter` _`Tk()` for short_ in `window = Tk()`. After that, I have to give the window a name here this window's name is _"new pygame window"_ which has a fixed size so that the user can't control the window size by `window.title("new pygame window"), window.resizable(False, False)`. Once that is all done, the score is set to a value `0` then displayed onto the screen using `label = Label(window, text="Score:{}".format(score))`. 

### **Challenges & Takeaways:**

* One challenge that I got from this was that I issues installing `pip` onto my computer, the thing that help was getting `pip3` which is the updated version of `pip` 

* Other challenge I faced was that I had issues following the official documents by `pygame` itself

* A takeaway I got from this was that I should really start watching more and more videos about `pygame` to really understand how to work with it.

* Last takeaway I got from this was that I need to tinker with `pygame` to help me to understand how to use it.
 

---

[Next](entry02.md)

[Home](../README.md)








