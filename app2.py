from appJar import gui
#from utils import test_action, rfid_thread

# create the GUI & set a title
app = gui("pico_native")

import serial

ser = serial.Serial('/dev/cu.usbserial-A6026SIM', 9600)

BAUD_RATE = 9600
RFID_BYTES = 12
START_CHAR = '\x02'
FOUND_TAG = ""


def rfid_thread():
    global FOUND_TAG
    #ser = serial.Serial('/dev/cu.usbserial-A6026SIM', 9600)
    print ('Wating for RFID Tag......')
    # Wait until a tag is read
    rfid = ser.read(RFID_BYTES)
    rfid = str(rfid.strip(START_CHAR))

    # Only act if we think we have a valid tag
    if len(rfid) == (RFID_BYTES - 1):
        print 'Tag Found', rfid
        FOUND_TAG = rfid
        app.queueFunction(app.setImage, "main_image", "9.gif")
    # Flush the bus
    ser.flushInput()

# add labels & entries
# in the correct row & column
#app.startLabelFrame("Simple", 0, 0)
#app.addImage("simple", "main_first.png")
#app.stopLabelFrame()

app.startLabelFrame("Click Me", 0, 2)
app.addImage("main_image", "8.gif")
app.stopLabelFrame()

app.thread(rfid_thread)

# start the GUI
app.go()
