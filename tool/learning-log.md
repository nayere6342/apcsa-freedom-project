# Tool Learning Log

## Tool: **Phython; Pygame**

## Project: **Flappy Bird Remix**

---

### Section #1: (10/6/25)

Now one thing I had issues with was running the code bug free. So that got me to look into further and what I saw was that I needed an add-on type program to check for bugs in the code. That's why I wanted to do this to make sure I don't make any mistakes when I'm coding. I know that this code might look too simple to be useful _but it helps me out._ And if it can do that, I'm going to use the code. Here is the preview of the code if you want to know the logic on how it works to do all this:     

```py
from CODE import FUNCTION

def main(): # define the main part of list FIRST before testing the function
test_FUNCTION()

def test_FUNCTION():
if FUNCTION(VALUE1) != VALUE2:
print("ERROR: INCORRECT VALUE STATE") # error text if not true into terminal

if __name__ == "__main__"
main()
```

For some context, this program isn't apart perhaps but something to add on the code. How this code works is _like I said before,_ it is just bug for bug by testing the function with `def test_FUNCTION():`. Then it checks if the first value _(that should be already set)_ isn't the same as what the code should be, print the statement: `ERROR: INCORRECT VALUE STATE`. Which is just a fancy way of saying something in the code is not right because I have all the values that are the right way of printing. 

### Challenges:

* One challenge that I had was figuring out why I had errors. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* Another challenge I faced was understanding the syntax of phython. Like I knew that java and phython are somewhat able to do the same tasks but python's syntax at times is complex and hard to read.

* One other challenge I had was that I felt confused a lot though the process of tinkering.         

---

### Section #2: (10/28/25)

Since the last time I logged into my python code, I hadn't really gotten the big picture of how to really understand my code but one thing I did find out was how to get files to download on my computer using python. Which can be useful for any amount of file sharing. But of course I know this code might look simple on the surface at first but it is more complete on the inside of the code. This is because of the fact that it will check if the file is even on the user's computer and it will show a message for that response. It will print out `Error fetching file from URL: {e}` if something went wrong with the code. _Whether it be by the download itself or an error with the code._ But if the code completed its job then it will print `File '{local_filename}' downloaded successfully.` _{local_filename} i.e the file that just downloaded the on computer._ If you want to see the code, here is the full preview;

```py
import requests

url = "https://youtube.com/video_file.txt"
local_filename = "downloaded_file.txt"

try:
    response = requests.get(url, stream=True) 
    response.raise_for_status()  

    with open(local_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"File '{local_filename}' downloaded successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching file from URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

The first thing that the code does is that it first fetches the `url` in the line `url = "https://youtube.com/video_file.txt"` that it trying to download then it gives that file a name so that the user knows where it is going to be. In this case it is a file found on youtube and the file type is a text file _(`txt`)_ After that is done, it gives the user the finished file using `with open(local_filename, "wb") as f: for chunk in response.iter_content(chunk_size=8192): f.write(chunk)` which will open the file in the topbar. At the end of it all it will either give back a `downloaded successfully.` or an `An error occurred` if something somehow went wrong. 

### Challenges:

* One challenge that I had was figuring out why I had errors. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* Another challenge I faced was understanding how things worked to begin with using python. _For example,_ I'm always use to the syntax of Java & JS _since I have been using it for a while._

* One other challenge I had was that I felt confused a lot though the process of tinkering.         


---

### Section #3: (11/18/25)

One thing I have been trying to learn is better understanding the syntax of phython since I have been trying to learn it. It's kinda easy for me as of now, like I know how to write class in phython which can be a useful tool for me in the game. Which I used for my last game using just class. So here is the code to know how class work in phython; 

```py
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
del p1
```

First thing that happens the class with the value of 5. Due to the fact that it states the value by useing `x` as the parameter. Second part of the code is the `p1` element is addon to the value of 5. This will be used to store the class that has the value of `x = 5`. From that it meant sound easier to just have `p1` with the value of 5 instead of having it be a class. Because this works by asking to get the class which already has a value of 5. The very last thing that happens is the class which is stored in the `p1` element being deleted as soon as it gets printed out by the last line: `del p1`. Which will just delete `p1` and it will not delete the class since `p1` is just keeping a copy of the class value. So in the end of it all the class will not be affected.  

### Challenges:

* One challenge that I had was figuring out why I had errors. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* Another challenge I faced was understanding how things worked to begin with using python. _For example,_ I'm always use to the syntax of Java & JS _since I have been using it for a while._

* One other challenge I had was that I felt confused a lot though the process of tinkering.

* Last challenge I got from this was having the right time to do the work in time so that I don't mass anything up.  

---

### Section #4: (11/20/25)

For this log I have learn a lot in pygame at this point, I understand how the syntax of phython works so that I can use the knowledge for later. So in this part of the code how it works is it opens up a window. That's when this part of the code is ran. The full preview of will be shown here;  

```py
main_dir = os.path.split(os.path.abspath(__file__))[0]
image_name = os.path.join(main_dir, "data", "cursor.png")
image = pg.image.load(image_name)
image_cursor = pg.cursors.Cursor(
    (image.get_width() // 2, image.get_height() // 2), image
)


# Create a bitmap cursor from simple strings

# sized 24x24
thickarrow_strings = (
    "XX                      ",
    "XXX                     ",
    "XXXX                    ",
    "XX.XX                   ",
    "XX..XX                  ",
    "XX...XX                 ",
    "XX....XX                ",
    "XX.....XX               ",
    "XX......XX              ",
    "XX.......XX             ",
    "XX........XX            ",
    "XX........XXX           ",
    "XX......XXXXX           ",
    "XX.XXX..XX              ",
    "XXXX XX..XX             ",
    "XX   XX..XX             ",
    "     XX..XX             ",
    "      XX..XX            ",
    "      XX..XX            ",
    "       XXXX             ",
    "       XX               ",
    "                        ",
    "                        ",
    "                        ",
)

bitmap_cursor1 = pg.cursors.Cursor(
    (24, 24),
    (0, 0),
    *pg.cursors.compile(thickarrow_strings, black="X", white=".", xor="o"),
)
```

The very first thing that happens in the code is the the image logic. This tell the computer what the image is and where in the files it is in. By using `image_name = os.path.join(main_dir, "data", "cursor.png")` it know it's data type is a `png`. Once that is done, the second part of the code runs. It first has to go though a resizing process (it being 24 by 24 is why) Then it's get deplayed onto the screen. Which the last part of the code that gives color to the pixels on the screen. The preview of the image is called a bitmap. This is a simple way of showing a complated displays so that devlopers can see how a image will show to the user and it color. Which works well with black and white images to give it color. By the previewd shown above, `X` being the pixel set to black while, `.` being white. After that's is finalized, the image gets printed onto the screen.  

### Challenges:

* One challenge that I had was figuring out why I had errors. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* One other challenge I had was that I felt confused a lot though the process of tinkering.

* Last challenge I got from this was having the right time to do the work in time so that I don't mass anything up.

---

### Section #6: (12/9/25)



```py

```



### Challenges:

* One challenge that I had was figuring out why I had errors. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* One other challenge I had was that I felt confused a lot though the process of tinkering.

* Last challenge I got from this was having the right time to do the work in time so that I don't mass anything up.

---

### Section #5: (12/8/25)

At this point I understand how to piece together parts of the pygame library into making funcation for a game. Like what I'm doing for the flappy bird game. For a run down of the code, all it does is that it will give the ability to connect a joystick to the game that it's needed in. Here is the full preview of the code;      

```py
# ...

def main():
    # Set the width and height of the screen (width, height), and name the window.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    text_print = TextPrint()

    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((255, 255, 255))
        text_print.reset()

        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()

        text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
        text_print.indent()

        # For each joystick:
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()

            text_print.tprint(screen, f"Joystick {jid}")
            text_print.indent()

            # Get the name from the OS for the controller/joystick.
            name = joystick.get_name()
            text_print.tprint(screen, f"Joystick name: {name}")

            guid = joystick.get_guid()
            text_print.tprint(screen, f"GUID: {guid}")

            power_level = joystick.get_power_level()
            text_print.tprint(screen, f"Joystick's power level: {power_level}")


            # the other. Triggers count as axes.
            axes = joystick.get_numaxes()
            text_print.tprint(screen, f"Number of axes: {axes}")
            text_print.indent()

            for i in range(axes):
                axis = joystick.get_axis(i)
                text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")
            text_print.unindent()

            buttons = joystick.get_numbuttons()
            text_print.tprint(screen, f"Number of buttons: {buttons}")
            text_print.indent()

            for i in range(buttons):
                button = joystick.get_button(i)
                text_print.tprint(screen, f"Button {i:>2} value: {button}")
            text_print.unindent()

            hats = joystick.get_numhats()
            text_print.tprint(screen, f"Number of hats: {hats}")
            text_print.indent()

            # Hat position. All or nothing for direction, not a float like
            # get_axis(). Position is a tuple of int values (x, y).
            for i in range(hats):
                hat = joystick.get_hat(i)
                text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
            text_print.unindent()

            text_print.unindent()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


        clock.tick(30)


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
```

The very first thing the code does is it listens in if the user has pressed anything to later use for input onto the screen whatever the screen has. The input can be checked on by having a indecater on screen. For example a print statment can work here like; `print("Joystick button pressed.")` is a print statment that can be used here. The second thing that done is other event triggers like holding down a button to activate something on screen. Here is something that uses this method: `if event.type == pygame.JOYBUTTONUP: print("Joystick button released.")`. Which is needed if the game in question (like mine) The last part of the code that is needed for the joystick logic is a connection system for if the joystick turns on. Which is simple for this because it's only makes up two parts, first the it gets the instance of the joysticks AKA calling the joystick class shown here, `joysticks[joy.get_instance_id()] = joy` after that is done, it simply prints out the message: "Joystick + (the instance of the class) + connencted" `print(f"Joystick {joy.get_instance_id()} connencted")` After all of that is finished it draws the game pieces and ends the program.  

### Challenges:

* One challenge that I had was figuring out why I had errors. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* One other challenge I had was that I felt confused a lot though the process of tinkering.

* Last challenge I got from this was having the right time to do the work in time so that I don't mass anything up.

---

