import pyperclip
from datetime import datetime
from time import sleep
import os
clip_history= ['']
while True:
    clip = pyperclip.paste()
    
    if clip == clip_history[-1] or len(clip_history)==0:
        pass
    else:
        clip_history.append(clip)
        os.system('clear')
        with open('paperclip_history.txt', 'a+') as f:
            f.write(clip+ '\n')
        print(f'clip history: {clip_history}')

    
    sleep(5)
    