from urllib.request import urlopen
from sys import argv
import tkinter as tk
window = tk.Tk()
url = argv[1]
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
inbody = False
inh1 = False
intag = False
body_chars = ""
h1_chars = ""
ch1_chars = ""
cbody_chars = ""
body_contents = ""
h1_contents = ""
for char in html:
    if char == "<":
        intag = True
    elif char == ">":
        intag = False
        if body_chars == "body":
            inbody = True
        elif cbody_chars == "/body":
            inbody = False

        elif h1_chars == "h1":
            inh1 = True
        elif ch1_chars == "/h1":
            inh1 = False
        else:
            body_chars = ""
    elif not intag:
        if inbody:
            body_contents += char
        elif inh1:
            h1_contents += char
    elif intag:
        body_chars += char
        cbody_chars += char
        h1_chars += char
        ch1_chars += char


greeting = tk.Label(text=body_contents)
greeting.pack()
window.mainloop()