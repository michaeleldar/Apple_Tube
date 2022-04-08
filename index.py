from urllib.request import urlopen
from sys import argv
import tkinter as tk
url = argv[1]
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
inbody = False
inh1 = False
intag = False
body_chars = ""
h1_chars = ""
cbody_chars = ""
body_contents = ""
for char in html:
    if char == "<":
        intag = True
    elif char == ">":
        intag = False
        if body_chars == "body":
            inbody = True
        elif cbody_chars == "/body":
            inbody = False
        else:
            body_chars = ""
    elif inbody:
        if not intag:
            body_contents += char
    elif intag:
        body_chars += char
        cbody_chars += char

window = tk.Tk()
greeting = tk.Label(text=body_contents)
greeting.pack()
window.mainloop()