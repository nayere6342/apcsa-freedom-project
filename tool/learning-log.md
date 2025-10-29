# Tool Learning Log

## Tool: **Phython**

## Project: **Unnamed Utility Software**

---

### Section #1: (10/6/25)

Now one thing I had issues with was running the code bug free. So that got me to look into further and what I saw was that I needed a add-on type program to check for bugs in the code. That's why I wanted to do this to make sure I don't make any mistakes when I'm coding. I know that this code might look to simple to be useful but it helps me out. And if it can do that, I'm going to use the code. Here is the preview of the code if you want to know the logic on how it works to do all this:     

```py
from CODE import FUNCTION

def main(): # define the main part of list FIRST before testing the function
test_FUNCTION()

def test_FUNCTION():
if FUNCTION(VALUE1) != VALUE2:
print("ERROR: INCORRECT VALUE STATE") # error text if not true into terimal

if __name__ == "__main__"
main()
```

For some context, this program isn't apart perhaps but something to add on the code. How this code works is _like I said before,_ it just bug for bug by testing the function with `def test_FUNCTION():`. Then it checks if the first value _(that should be already set)_ isn't the same as what the code should be, print the statment: `ERROR: INCORRECT VALUE STATE`. Which is just a fancy way of saying something in the code is not right because I have all the values that are the right way of printing. 

### Challenges:

* One challenge that I had was figering out why I had error. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* Another challenge I faced was understanding the syntax of phython. Like I knew that java and phython are somewhat able to do the same tasks but phython's syntax at time is complex and hard to read.

* One other challenge I had was that I felt confused a lot thought the process of tinkering.         

---

### Section #2: (10/28/25)

Since, the last time I log my python code, I hadn't really gotten I big picture of how to really understand my code but one thing I did found out was how to get files to download on my computer using python. Which can be useful for any amount of file sharing. But ofcource I know this code might look simple on the surface at first but it is more complated on the inside of the code. This is because of the fact that it will check if the file is even on the user's computer and it will show a message for that respone. It will print out `Error fetching file from URL: {e}` if something went wrong with the code. _Whether it be by the download itself or and error with the code._ But if the code completed it's job than it will print `File '{local_filename}' downloaded successfully.` _{local_filename} i.e the file that just downloaded the on computer._ If you want to see the code, here is the full preview;

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

### Challenges:

* One challenge that I had was figering out why I had error. knew that the error is line 88 _for example_ but I wouldn't know if it was a syntax error or what because it wouldn't ever show me what went wrong.

* Another challenge I faced was understanding the syntax of phython. Like I knew that java and phython are somewhat able to do the same tasks but phython's syntax at time is complex and hard to read.

* One other challenge I had was that I felt confused a lot thought the process of tinkering.         


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
