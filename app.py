from appJar import gui

# create the GUI & set a title
app = gui("Login Form")

# add labels & entries
# in the correct row & column
app.addLabel("userLab", "Username:", 0, 0)
app.addEntry("userEnt", 0, 1)
app.addLabel("passLab", "Password:", 1, 0)
app.addEntry("passEnt", 1, 1)
app.startLabelFrame("Simple", 0, 0)
app.addImage("simple", "main_first.png")
app.stopLabelFrame()

# start the GUI
app.go()