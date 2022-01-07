# Importing required features
import webbrowser
import os

def input():
    userInput = self.txtText.get()
    f = open("customWebpage.html", "w")    



# Just in case, writing it in here
    html_template = """
    <html>
        <body>
        <head>
            <link rel="stylesheet" href="style.css">
        </head>
            <h1>"""+userInput+"""</h1>
        </body>
    </html>
    """
    f.write(html_template)

    f.close()
    webbrowser.open_new_tab("customWebpage.html")







