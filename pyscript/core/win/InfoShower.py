#带项目选择的信息展示框

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.tix as tix

class InfoShower():
  def __init__(self,root):
    self.root = root
    self.frame = tk.Frame(self.root)
    self.keys = tk.StringVar()
    
    self.klist = tk.Listbox(self.frame,listvariable=self.keys)
    self.klist.grid(row=1,column=1)
    self.vfram = tk.Frame(self.frame)
    self.vfram.grid(row=1,column=2)
  def getContainer(self):
    return self.frame
  def refresh(self,cont):
    '''刷新内容
    @params cont => {str <show_name>:tk.Frame <content>}
    '''
    self.cont = cont
    self.keys_arr = self.cont.keys()
    self.keys.set(self.keys_arr)
  def 
    
    
    
    
    