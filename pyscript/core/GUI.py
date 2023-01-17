import tkinter as tk
import tkinter.ttk as ttk
import tkinter.tix as tix
import tkinter.scrolledtext as stext

import os.path as path
from core.settings import Settings
from core.version import *
from core.win.InfoShower import InfoShower

class App():
  def __init__(self,config,root=tix.Tk()):
    self.root=root
    self.config=config
    self.langFull = Settings(path.join(
      self.config.getConfig("lang.home"),self.config.getConfig("lang.default")
      ))
    self.lang = self.langFull.getSubSettings(["GUI",])
    
    self.root.mconf = self.config.getSubSettings(["GUI","main"])
    self.winconf = self.config.getSubSettings(["GUI","window"])
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
    
    # ------------ 软件介绍区 ----------------------------
    self.phome.descf = tk.LabelFrame(self.phome,text=self.lang.gc("home.descTitle"))
    self.phome.descf.grid(row=1,column=1)
    self.phome.descf.st = stext.ScrolledText(self.phome.descf,width=14,height=10,wrap=tk.WORD)
    self.phome.descf.st.insert(tk.END,self.langFull.gc("description"))
    self.phome.descf.st.pack(fill=tk.BOTH)
    
    # ------------ 按钮控制区 ----------------------------
    self.phome.btnf = ttk.LabelFrame(self.phome,text=self.lang.gc("home.btnFrame"))
    self.phome.btnf.grid(row=2,column=1,sticky="nsew")
    tk.Button(self.phome.btnf,text=self.lang.gc("home.btns.run")).pack(fill=tk.X)
    tk.Button(self.phome.btnf,text=self.lang.gc("home.btns.exit"),command=lambda:self.root.destroy()).pack(fill=tk.X)
    
    # ------------ 文件输入区 ----------------------------
    
  def info(self):
    #信息页面
    self.pinfo = ttk.Frame(self.nb)
    self.nb.add(self.pinfo,text=self.lang.gc("info.title"))
    
    self.infoshower = InfoShower(self.pinfo)
    self.infoshower.getContainer().pack(fill=tk.BOTH)
    
    infoma = {
      self.lang.gc("info.shower.author"):
        self.readonlyMultiText(self.infoshower,"DouNsM"),
      self.lang.gc("info.shower.version"):
        self.readonlyMultiText(self.infoshower,"{0}\n{1}".format(
          self.lang.gc("info.shower.vver")+VERSION["version"],
          self.lang.gc("info.shower.vdat")+VERSION["date"]
        ))
    }
    self.infoshower.refresh(infoma)
  
  def readonlyMultiText(self,infos,text):
    s = stext.ScrolledText(infos.getRoot(),
      width=self.winconf.gc("scrolledText.width"),
      height=self.winconf.gc("scrolledText.height"),
      
      )
    s.insert(tk.END,text)
    return s
  
  def uplog(self):
    #更新日志界面
    self.puplog = ttk.Frame(self.nb)
    self.nb.add(self.puplog,text=self.lang.gc("uplog.title"))
    self.uplogshower = InfoShower(self.puplog)
    self.uplogshower.getContainer().pack(fill=tk.BOTH)
    logs = {}
    rev_logs = list(UPDATE_LOG.items());
    rev_logs.reverse()
    for (k,v) in rev_logs:
      logs[k]=self.readonlyMultiText(self.uplogshower,v)
    self.uplogshower.refresh(logs)
    
  def mainloop(self):
    self.root.mainloop()