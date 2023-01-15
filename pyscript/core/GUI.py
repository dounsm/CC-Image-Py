import tkinter as tk
import tkinter.ttk as ttk
import tkinter.tix as tix

import os.path as path
from core.settings import Settings
from core.version import *
from core.win.InfoShower import InfoShower

class App():
  def __init__(self,config,root=tix.Tk()):
    self.root=root
    self.config=config
    self.lang = Settings(path.join(
      self.config.getConfig("lang.home"),self.config.getConfig("lang.default")
      )).getSubSettings(["GUI",])
    
    self.root.mconf = self.config.getSubSettings(["GUI","main"])
    self.root.title(self.lang.gc("main.title"))
    self.root.geometry("{0}x{1}+{2}+{3}".format(
      self.root.mconf.gc("width"),
      self.root.mconf.gc("height"),
      self.root.mconf.gc("xoffset"),
      self.root.mconf.gc("yoffset"),
      ))
    
    self.nb = ttk.Notebook(self.root)
    self.nb.pack(fill=tk.BOTH)
    
    self.home()
    self.info()
    self.uplog()
  def home(self):
    #主页面
    self.phome = ttk.Frame(self.nb)
    self.nb.add(self.phome,text=self.lang.gc("home.title"))
  def info(self):
    #信息页面
    self.pinfo = ttk.Frame(self.nb)
    self.nb.add(self.pinfo,text=self.lang.gc("info.title"))
    
    self.infoshower = InfoShower(self.pinfo)
    self.infoshower.getContainer().pack(fill=tk.BOTH)
  def uplog(self):
    #更新日志界面
    self.puplog = ttk.Frame(self.nb)
    self.nb.add(self.puplog,text=self.lang.gc("uplog.title"))
  def mainloop(self):
    self.root.mainloop()