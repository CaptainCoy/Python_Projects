# Importing required features
import webbrowser
import os

# define file path
f = open("C:\python_projects\web_page_generator\index.html", "w")

# Just in case, writing it in here
html_template = """
<html>
    <body>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
        <h1>
            "Text from gen_GUI should go here ideally"<br> *shrugs shoulders
        </h1>
    </body>
</html>
"""
f.write(html_template)

f.close()

# defining filename
filename = "C:\python_projects\web_page_generator\index.html"






