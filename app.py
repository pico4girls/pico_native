from appJar import gui
from utils import test_action

# create the GUI & set a title
app = gui("pico_native")

def songChanged(rb):
    print(app.getRadioButton(rb))

# add labels & entries
# in the correct row & column
#app.startLabelFrame("Simple", 0, 0)
#app.addImage("simple", "main_first.png")
#app.stopLabelFrame()

app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.setRadioButtonChangeFunction("song", songChanged)
app.addButton("Reset", test_action)

# start the GUI
app.go()