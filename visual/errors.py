import tkinter as tk
from tkinter import messagebox
import bg


def info1():
    bg.playNotifSound()
    messagebox.showinfo("Information", "This is a test!")
def info2():
    bg.playErrorSound()
    messagebox.showerror("Error!", "Error testing!")
def setupfail():
    bg.playErrorSound()
    messagebox.showerror("Error!", "Setup couldn't continue, we're sorry!")