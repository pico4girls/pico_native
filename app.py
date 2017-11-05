from appJar import gui
from utils import test_action

# create the GUI & set a title
app = gui("pico_native")

def songChanged(rb):
    print(app.getRadioButton(rb))

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

BAUD_RATE = 9600
RFID_BYTES = 12
START_CHAR = '\x02'
FOUND_TAG = ""


#images = ['1.gif', '2.gif', '3.gif', '4.gif','5.gif', '6.gif', '7.gif', '8.gif','1.gif', '2.gif', '3.gif', '4.gif','1.gif', '2.gif', '3.gif', '4.gif',]
images = 14
# click function
clicked = False
count = 1


def rfid_thread():
    global FOUND_TAG
    global count
    #ser = serial.Serial('/dev/cu.usbserial-A6026SIM', 9600)
    print ('Wating for RFID Tag......')
    # Wait until a tag is read
    rfid = ser.read(RFID_BYTES)
    rfid = str(rfid.strip(START_CHAR))

    # Only act if we think we have a valid tag
    if len(rfid) == (RFID_BYTES - 1):
        print 'Tag Found', rfid
        FOUND_TAG = rfid
        app.queueFunction(app.setImage, "main_image", "2.gif")
        count+=1
    # Flush the bus
    ser.flushInput()



def changePic(btn):
    if btn == "main_image":
        global images
        global count
        #if clicked: app.setImage("clickme", "1.gif")
        #else: app.setImage("clickme", "2.gif")
        app.setImage("main_image", str(count)+".gif")
        #clicked = not clicked
        count+=1
        if count > images: count = 1



#app.startLabelFrame("Click Me", 0, 2)
app.addImage("main_image", "1.gif")
app.setImageSubmitFunction("main_image", changePic)
#app.stopLabelFrame()


app.thread(rfid_thread)

# start the GUI
app.go()
