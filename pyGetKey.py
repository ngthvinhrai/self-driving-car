from pynput.keyboard import *
import keyboard
from getkeys import key_check

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

def key_to_output(keys):
    output = [0,0,0,0,0,0,0,0,0]
    
    if keyboard.is_pressed('w'):
        output = w
    elif keyboard.is_pressed('s'):
        output = s
    elif keyboard.is_pressed('a'):
        output = a
    elif keyboard.is_pressed('d'):
        output = d
    elif keyboard.is_pressed('q'):
        output = wa
    elif keyboard.is_pressed('e'):
        output = wd
    elif keyboard.is_pressed('z'):
        output = sa
    elif keyboard.is_pressed('c'):
        output = sd
    else: 
        output = nk
    return output

while True:
    keys = keyboard.read_key()
    output = key_to_output(keys)
    print(output)
    if keyboard.is_pressed('p'): break
        
        
