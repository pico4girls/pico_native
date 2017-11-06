from appJar import gui
import requests
#from utils import test_action, rfid_thread

# create the GUI & set a title
app = gui("pico_native")

def songChanged(rb):
    print(app.getRadioButton(rb))

import serial
'''
ser = serial.Serial('/dev/cu.usbserial-A6026SIM', 9600)

BAUD_RATE = 9600
RFID_BYTES = 12
START_CHAR = '\x02'
FOUND_TAG = ""
'''
def launch(win):
    app.showSubWindow(win)

'''
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
'''
def send_msg(data):
    print (data)
    print (app.getEntry("Send a Message:"))
    r = requests.post('https://roksonne.com/api/messages', 
                      data = {'rfid_tag':"88UIOIOH77", 'body':app.getEntry("Send a Message:")})
    print r
    app.addMessage("mess{}".format(0), app.getEntry("Send a Message:"))

def get_msgs():
    pass

# add labels & entries
# in the correct row & column
#app.startLabelFrame("Simple", 0, 0)
#app.addImage("simple", "main_first.png")
#app.stopLabelFrame()

msg_data = ''


app.startLabelFrame("Click Me", 0, 2)
app.addImage("main_image", "8.gif")
app.stopLabelFrame()

#app.thread(rfid_thread)

messages = ["Hi I think I might be pregnant - can you help?",
            "Yeah sure - when was your lasts period?"]

app.startSubWindow("Show Messages")
app.addLabel("l1", "Messages Window")
for i in messages:
    app.setFont(12)
    app.addMessage("mess{}".format(i), i)
    
app.addLabelEntry("Send a Message:")
app.addButton("Send", send_msg)
app.stopSubWindow()

app.addButtons(["Show Messages"], launch)

# start the GUI
app.go()


