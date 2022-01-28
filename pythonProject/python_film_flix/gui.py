
from guizero import App, Text, TextBox, PushButton, Picture, ButtonGroup


import sqlite3
conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()



app = App(title="Film Flix App", bg="blue", height=200, width= 400)

# pic = Picture(app, image="python_film_flix/pictures /puppy2.png")

# txtMovieId = Text(app, text="Display film ID ")
# txtBID = TextBox(app)
# txtMovie = Text(app, text="Search Film")
# txtMovie = TextBox(app)

def printAll():
    for row in cursor.execute("SELECT * FROM tblFilms"):
        print (row)    
# printAll()

txtDisplay = Text(app, text="Films display", color="black", bg="white")




txtDisplay.value = printAll()

showFilms = PushButton(app, command=printAll, text="show films")


# from guizero import App, Text, Picture
# app = App("Wanted!")
# app.bg = "#FBFBD0"
# wanted_text = Text(app, "WANTED")
# wanted_text.text_size = 50
# wanted_text.font = "Times New Roman"








app.display()
