# Tool Learning Log

## Tool: **Phython**

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

### Section #&: (11/18/25)

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

---

### Section #&: (&&/&/&&)

```py

```

### Challenges:

---

### Section #&: (&&/&/&&)

```py

```

### Challenges:

---



