from urllib.request import urlopen
from sys import argv
url = argv[1]
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
inbody = False
intag = False
body_chars = ""
cbody_chars = ""
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
            print(char, end="")
    elif intag:
        body_chars += char
        cbody_chars += char

