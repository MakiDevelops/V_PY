''' Define File'''
''' This file has a lot of functions '''

import platform
import os
import time
from time import sleep
from tkinter import *
from tkinter import ttk
import tkinter
import pygame


def getimports():
    import platform
    import os
    import time
    from time import sleep
    import qt_er

def getos():
    print(platform.system())
    sleep(0.1)
    print(platform.processor())
    sleep(0.1)
    print(platform.architecture())
    sleep(0.1)
    print(platform.machine())
    sleep(0.1)
    print(platform.node())
    sleep(0.1)
    print(platform.platform())
    sleep(0.1)
def clear():
    if platform == 'darwin':
        os.system("clear")
    else:
        os.system('cls')
def playStartSound():
    pygame.init()
    pygame.mixer.music.load("STARTUP.wav")
    pygame.mixer.music.play()
def playNotifSound():
    pygame.init()
    pygame.mixer.music.load("DING.wav")
    pygame.mixer.music.play()
def playErrorSound():
    pygame.init()
    pygame.mixer.music.load("CHORD.wav")
    pygame.mixer.music.play()
def playShutdownSound():
    pygame.init()
    pygame.mixer.music.load("CHIMES.wav")
    pygame.mixer.music.play()
def startscreen():
    m = tkinter.Tk()
    m.mainloop()

def addbg():
    m = tkinter.Tk()
    m.title('V_Py')
    m.attributes('-fullscreen', True)
    m.configure(bg="blue")
    '''
    widgets are added here
    '''
    m.mainloop()






