import tkinter as tk
import tkinter.ttk as ttk
import tkinter.tix as tix

class App():
  def __init__(self,config,root=tix.Tk()):
    self.root=root
    self.config=config
  def mainloop(self):
    self.root.mainloop()